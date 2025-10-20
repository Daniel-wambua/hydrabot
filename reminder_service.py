"""
Reminder Service - Core logic for parsing commands and managing reminders
Handles: creating reminders, cancelling, listing, and processing "done" responses
"""

import re
from datetime import datetime, timedelta
from typing import Optional, List, Tuple
from sqlalchemy.orm import Session
from models import User, Reminder, ReminderLog


class ReminderService:
    """Service for managing reminders and parsing user commands"""
    
    @staticmethod
    def get_or_create_user(db: Session, platform: str, platform_id: str) -> User:
        """Get existing user or create new one"""
        user = db.query(User).filter(User.platform_id == platform_id).first()
        if not user:
            user = User(platform=platform, platform_id=platform_id)
            db.add(user)
            db.commit()
            db.refresh(user)
        return user
    
    @staticmethod
    def parse_command(message: str) -> Tuple[str, dict]:
        """
        Parse user message and extract command type and parameters
        Returns: (command_type, parameters)
        
        Supported commands:
        - "remind me to drink water every 2 hours"
        - "remind me to call mom at 6pm"
        - "cancel water reminders"
        - "cancel all reminders"
        - "list reminders"
        - "stats"
        - "done"
        """
        message = message.strip().lower()
        
        # Check for "done" response
        if message == "done":
            return ("done", {})
        
        # Check for stats command
        if message in ["stats", "show stats", "my stats"]:
            return ("stats", {})
        
        # Check for list command
        if "list" in message and "reminder" in message:
            return ("list", {})
        
        # Check for cancel command
        if "cancel" in message:
            if "all" in message:
                return ("cancel_all", {})
            # Extract keyword to cancel specific reminders
            match = re.search(r"cancel\s+(.+?)\s+reminder", message)
            if match:
                keyword = match.group(1).strip()
                return ("cancel", {"keyword": keyword})
            return ("cancel_all", {})
        
        # Check for remind command with recurring interval
        # Pattern: "remind me to X every Y hours/minutes"
        recurring_match = re.search(
            r"remind\s+me\s+to\s+(.+?)\s+every\s+(\d+)\s+(hour|minute|min|hr)",
            message
        )
        if recurring_match:
            title = recurring_match.group(1).strip()
            interval = int(recurring_match.group(2))
            unit = recurring_match.group(3)
            
            # Convert to minutes
            if unit in ["hour", "hr"]:
                interval_minutes = interval * 60
            else:
                interval_minutes = interval
            
            return ("remind_recurring", {
                "title": title,
                "interval_minutes": interval_minutes
            })
        
        # Check for remind command with specific time
        # Pattern: "remind me to X at Y"
        time_match = re.search(r"remind\s+me\s+to\s+(.+?)\s+at\s+(.+)", message)
        if time_match:
            title = time_match.group(1).strip()
            time_str = time_match.group(2).strip()
            
            # Parse time (simplified - accepts formats like "6pm", "18:00", "6:30pm")
            scheduled_time = ReminderService._parse_time(time_str)
            
            return ("remind_once", {
                "title": title,
                "scheduled_time": scheduled_time
            })
        
        # Unknown command
        return ("unknown", {})
    
    @staticmethod
    def _parse_time(time_str: str) -> Optional[datetime]:
        """Parse time string into datetime object for today"""
        time_str = time_str.lower().strip()
        
        # Handle "6pm", "6:30pm" format
        match = re.search(r"(\d+)(?::(\d+))?\s*(am|pm)?", time_str)
        if match:
            hour = int(match.group(1))
            minute = int(match.group(2)) if match.group(2) else 0
            period = match.group(3)
            
            # Convert to 24-hour format
            if period == "pm" and hour != 12:
                hour += 12
            elif period == "am" and hour == 12:
                hour = 0
            
            # Create datetime for today
            now = datetime.now()
            scheduled = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            
            # If time has passed today, schedule for tomorrow
            if scheduled < now:
                scheduled += timedelta(days=1)
            
            return scheduled
        
        return None
    
    @staticmethod
    def create_recurring_reminder(db: Session, user: User, title: str, interval_minutes: int) -> Reminder:
        """Create a new recurring reminder"""
        now = datetime.now()
        next_send = now + timedelta(minutes=interval_minutes)
        
        reminder = Reminder(
            user_id=user.id,
            title=title,
            interval_minutes=interval_minutes,
            is_recurring=True,
            is_active=True,
            next_send_at=next_send
        )
        
        db.add(reminder)
        db.commit()
        db.refresh(reminder)
        
        # Log the creation
        log = ReminderLog(
            user_id=user.id,
            reminder_id=reminder.id,
            action="created",
            reminder_title=title,
            notes=f"Recurring every {interval_minutes} minutes"
        )
        db.add(log)
        db.commit()
        
        return reminder
    
    @staticmethod
    def create_one_time_reminder(db: Session, user: User, title: str, scheduled_time: datetime) -> Reminder:
        """Create a one-time reminder"""
        reminder = Reminder(
            user_id=user.id,
            title=title,
            scheduled_time=scheduled_time,
            is_recurring=False,
            is_active=True,
            next_send_at=scheduled_time
        )
        
        db.add(reminder)
        db.commit()
        db.refresh(reminder)
        
        # Log the creation
        log = ReminderLog(
            user_id=user.id,
            reminder_id=reminder.id,
            action="created",
            reminder_title=title,
            notes=f"Scheduled for {scheduled_time.strftime('%I:%M %p')}"
        )
        db.add(log)
        db.commit()
        
        return reminder
    
    @staticmethod
    def cancel_reminders(db: Session, user: User, keyword: Optional[str] = None) -> int:
        """Cancel reminders containing keyword (or all if keyword is None)"""
        query = db.query(Reminder).filter(
            Reminder.user_id == user.id,
            Reminder.is_active
        )
        
        if keyword:
            query = query.filter(Reminder.title.ilike(f"%{keyword}%"))
        
        reminders = query.all()
        count = len(reminders)
        
        for reminder in reminders:
            reminder.is_active = False
            log = ReminderLog(
                user_id=user.id,
                reminder_id=reminder.id,
                action="cancelled",
                reminder_title=reminder.title
            )
            db.add(log)
        
        db.commit()
        return count
    
    @staticmethod
    def list_active_reminders(db: Session, user: User) -> List[Reminder]:
        """Get all active reminders for a user"""
        return db.query(Reminder).filter(
            Reminder.user_id == user.id,
            Reminder.is_active
        ).all()
    
    @staticmethod
    def mark_reminder_done(db: Session, user: User) -> Optional[Reminder]:
        """
        Mark the most recent reminder as completed
        For recurring reminders, update next_send_at
        For one-time reminders, mark as inactive
        """
        # Find the most recently sent reminder
        reminder = db.query(Reminder).filter(
            Reminder.user_id == user.id,
            Reminder.is_active,
            Reminder.last_sent_at.is_not(None)
        ).order_by(Reminder.last_sent_at.desc()).first()
        
        if not reminder:
            return None
        
        # Log completion
        log = ReminderLog(
            user_id=user.id,
            reminder_id=reminder.id,
            action="completed",
            reminder_title=reminder.title
        )
        db.add(log)
        
        # Update reminder based on type
        if reminder.is_recurring:
            # Reset the interval from now
            now = datetime.now()
            reminder.next_send_at = now + timedelta(minutes=reminder.interval_minutes)
        else:
            # One-time reminder - mark as done
            reminder.is_active = False
        
        db.commit()
        db.refresh(reminder)
        
        return reminder
    
    @staticmethod
    def get_stats(db: Session, user: User) -> dict:
        """Get user stats: hydration streak, total completions, recent reminders"""
        # Get completion logs
        completion_logs = db.query(ReminderLog).filter(
            ReminderLog.user_id == user.id,
            ReminderLog.action == "completed"
        ).order_by(ReminderLog.timestamp.desc()).limit(100).all()
        
        # Calculate hydration streak (consecutive days with at least one completion)
        streak = 0
        if completion_logs:
            current_date = datetime.now().date()
            dates_with_completions = set()
            
            for log in completion_logs:
                dates_with_completions.add(log.timestamp.date())
            
            # Count consecutive days from today backwards
            check_date = current_date
            while check_date in dates_with_completions:
                streak += 1
                check_date -= timedelta(days=1)
        
        # Get recent activity (last 5 logs)
        recent_logs = db.query(ReminderLog).filter(
            ReminderLog.user_id == user.id
        ).order_by(ReminderLog.timestamp.desc()).limit(5).all()
        
        return {
            "total_completions": len(completion_logs),
            "hydration_streak_days": streak,
            "recent_logs": recent_logs,
            "active_reminders_count": len(ReminderService.list_active_reminders(db, user))
        }
    
    @staticmethod
    def get_due_reminders(db: Session) -> List[Reminder]:
        """Get all reminders that are due to be sent"""
        now = datetime.now()
        return db.query(Reminder).filter(
            Reminder.is_active,
            Reminder.next_send_at <= now
        ).all()
    
    @staticmethod
    def mark_reminder_sent(db: Session, reminder: Reminder):
        """Mark a reminder as sent and update timing"""
        now = datetime.now()
        reminder.last_sent_at = now
        
        # Update next_send_at for recurring reminders
        if reminder.is_recurring:
            reminder.next_send_at = now + timedelta(minutes=reminder.interval_minutes)
        
        # Log the send
        log = ReminderLog(
            user_id=reminder.user_id,
            reminder_id=reminder.id,
            action="sent",
            reminder_title=reminder.title
        )
        db.add(log)
        db.commit()

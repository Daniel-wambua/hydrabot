"""
Scheduler - APScheduler setup for sending reminders
Checks for due reminders every minute and sends them
"""

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import asyncio
from models import SessionLocal
from reminder_service import ReminderService
from messaging_service import MessagingService

# Global scheduler instance
scheduler = None
messaging_service = MessagingService()


def send_due_reminders():
    """
    Check for due reminders and send them
    This function is called by the scheduler every minute
    """
    db = SessionLocal()
    try:
        # Get all due reminders
        due_reminders = ReminderService.get_due_reminders(db)
        
        if due_reminders:
            print(f"📬 Found {len(due_reminders)} due reminder(s)")
        
        # Send each reminder
        for reminder in due_reminders:
            try:
                # Get user info
                user = reminder.user
                
                # Format reminder message
                message = f"⏰ Reminder: {reminder.title}\n\nReply 'done' when complete!"
                
                # Send message (handle async)
                success = asyncio.run(
                    messaging_service.send_message(
                        user.platform,
                        user.platform_id,
                        message
                    )
                )
                
                if success:
                    # Mark as sent and update timing
                    ReminderService.mark_reminder_sent(db, reminder)
                    print(f"✅ Sent reminder '{reminder.title}' to {user.platform_id}")
                else:
                    print(f"❌ Failed to send reminder '{reminder.title}' to {user.platform_id}")
            
            except Exception as e:
                print(f"❌ Error sending reminder {reminder.id}: {e}")
    
    except Exception as e:
        print(f"❌ Error in send_due_reminders: {e}")
    
    finally:
        db.close()


def start_scheduler():
    """Start the background scheduler"""
    global scheduler
    
    if scheduler is not None:
        print("⚠️  Scheduler already running")
        return
    
    scheduler = BackgroundScheduler()
    
    # Add job to check for due reminders every minute
    scheduler.add_job(
        func=send_due_reminders,
        trigger=IntervalTrigger(seconds=60),
        id="send_reminders",
        name="Check and send due reminders",
        replace_existing=True
    )
    
    scheduler.start()
    print("⏰ Scheduler started - checking for reminders every minute")


def stop_scheduler():
    """Stop the background scheduler"""
    global scheduler
    
    if scheduler is not None:
        scheduler.shutdown()
        scheduler = None
        print("⏹️  Scheduler stopped")


def get_scheduler_status() -> dict:
    """Get scheduler status and jobs info"""
    global scheduler
    
    if scheduler is None:
        return {"status": "stopped", "jobs": []}
    
    jobs = []
    for job in scheduler.get_jobs():
        jobs.append({
            "id": job.id,
            "name": job.name,
            "next_run": job.next_run_time.isoformat() if job.next_run_time else None
        })
    
    return {
        "status": "running",
        "jobs": jobs
    }

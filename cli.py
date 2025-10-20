#!/usr/bin/env python3
"""
HydraBot CLI - Command-line management tool
Usage: python cli.py [command] [options]
"""

import sys
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models import init_db, SessionLocal, User, Reminder, ReminderLog  # noqa: E402


def show_help():
    """Display help information"""
    print("""
HydraBot CLI - Management Tool

Usage:
  python cli.py [command]

Commands:
  init          Initialize database
  stats         Show overall stats
  users         List all users
  reminders     List all active reminders
  logs          Show recent logs
  clean         Clean up inactive reminders
  help          Show this help message

Examples:
  python cli.py init
  python cli.py stats
  python cli.py users
""")


def initialize_database():
    """Initialize or reset database"""
    print("🗄️  Initializing database...")
    init_db()
    print("✅ Database initialized successfully!")


def show_stats():
    """Show overall statistics"""
    db = SessionLocal()
    try:
        user_count = db.query(User).count()
        reminder_count = db.query(Reminder).filter(Reminder.is_active).count()
        total_reminders = db.query(Reminder).count()
        log_count = db.query(ReminderLog).count()
        completed_count = db.query(ReminderLog).filter(
            ReminderLog.action == "completed"
        ).count()
        
        print("\n📊 HydraBot Statistics")
        print("=" * 50)
        print(f"👥 Total Users:           {user_count}")
        print(f"📋 Active Reminders:      {reminder_count}")
        print(f"📝 Total Reminders Ever:  {total_reminders}")
        print(f"✅ Completed Actions:     {completed_count}")
        print(f"📜 Total Log Entries:     {log_count}")
        print("=" * 50)
        
    finally:
        db.close()


def list_users():
    """List all users"""
    db = SessionLocal()
    try:
        users = db.query(User).all()
        
        print(f"\n👥 Users ({len(users)} total)")
        print("=" * 80)
        
        for user in users:
            active_reminders = len([r for r in user.reminders if r.is_active])
            print(f"ID: {user.id:3d} | Platform: {user.platform:8s} | "
                  f"Platform ID: {user.platform_id:20s} | "
                  f"Active: {active_reminders:2d} | "
                  f"Created: {user.created_at.strftime('%Y-%m-%d')}")
        
        print("=" * 80)
        
    finally:
        db.close()


def list_reminders():
    """List all active reminders"""
    db = SessionLocal()
    try:
        reminders = db.query(Reminder).filter(Reminder.is_active).all()
        
        print(f"\n📋 Active Reminders ({len(reminders)} total)")
        print("=" * 100)
        
        for reminder in reminders:
            user = reminder.user
            interval_str = ""
            if reminder.is_recurring:
                hours = reminder.interval_minutes // 60
                minutes = reminder.interval_minutes % 60
                interval_str = f"{hours}h {minutes}m" if hours > 0 else f"{minutes}m"
            else:
                interval_str = reminder.scheduled_time.strftime("%I:%M %p") if reminder.scheduled_time else "N/A"
            
            next_send = reminder.next_send_at.strftime("%m/%d %I:%M%p") if reminder.next_send_at else "N/A"
            
            print(f"ID: {reminder.id:3d} | User: {user.platform_id:15s} | "
                  f"Title: {reminder.title:30s} | "
                  f"Interval: {interval_str:10s} | "
                  f"Next: {next_send}")
        
        print("=" * 100)
        
    finally:
        db.close()


def show_logs(limit=20):
    """Show recent logs"""
    db = SessionLocal()
    try:
        logs = db.query(ReminderLog).order_by(
            ReminderLog.timestamp.desc()
        ).limit(limit).all()
        
        print(f"\n📜 Recent Logs (last {limit})")
        print("=" * 100)
        
        for log in logs:
            user = log.user
            time_str = log.timestamp.strftime("%m/%d %I:%M%p")
            print(f"{time_str} | User: {user.platform_id:15s} | "
                  f"Action: {log.action:10s} | "
                  f"Reminder: {log.reminder_title or 'N/A':30s}")
        
        print("=" * 100)
        
    finally:
        db.close()


def clean_inactive():
    """Clean up old inactive reminders"""
    db = SessionLocal()
    try:
        # Find inactive reminders older than 7 days
        from datetime import timedelta
        cutoff = datetime.now() - timedelta(days=7)
        
        old_reminders = db.query(Reminder).filter(
            Reminder.is_active.is_(False),
            Reminder.created_at < cutoff
        ).all()
        
        count = len(old_reminders)
        
        if count == 0:
            print("✅ No old inactive reminders to clean up")
            return
        
        print(f"🧹 Found {count} old inactive reminders")
        confirm = input("Delete them? (yes/no): ")
        
        if confirm.lower() == "yes":
            for reminder in old_reminders:
                db.delete(reminder)
            db.commit()
            print(f"✅ Deleted {count} old reminders")
        else:
            print("❌ Cancelled")
        
    finally:
        db.close()


def main():
    """Main CLI entry point"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    commands = {
        "init": initialize_database,
        "stats": show_stats,
        "users": list_users,
        "reminders": list_reminders,
        "logs": show_logs,
        "clean": clean_inactive,
        "help": show_help,
    }
    
    if command in commands:
        try:
            commands[command]()
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"❌ Unknown command: {command}")
        print("Run 'python cli.py help' for usage information")


if __name__ == "__main__":
    main()

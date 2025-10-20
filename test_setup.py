"""
Quick test script to verify HydraBot setup
Run this after setup to check if everything is configured correctly
"""

import os
from dotenv import load_dotenv

load_dotenv()

print("🧪 Testing HydraBot Configuration\n")
print("=" * 50)

# Check Python modules
print("\n📦 Checking dependencies...")
try:
    import fastapi  # noqa: F401
    import uvicorn  # noqa: F401
    import sqlalchemy  # noqa: F401
    import apscheduler  # noqa: F401
    import twilio  # noqa: F401
    import telegram  # noqa: F401
    print("✅ All required packages installed")
except ImportError as e:
    print(f"❌ Missing package: {e}")
    print("Run: pip install -r requirements.txt")

# Check environment variables
print("\n🔧 Checking environment variables...")
platform = os.getenv("MESSAGING_PLATFORM")
print(f"Platform: {platform}")

if not platform:
    print("❌ MESSAGING_PLATFORM not set in .env")
elif platform == "telegram":
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if token and token != "your_telegram_bot_token_here":
        print("✅ Telegram bot token configured")
    else:
        print("❌ TELEGRAM_BOT_TOKEN not configured in .env")
elif platform == "twilio":
    sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth = os.getenv("TWILIO_AUTH_TOKEN")
    phone = os.getenv("TWILIO_PHONE_NUMBER")
    if all([sid, auth, phone]) and sid != "your_twilio_account_sid_here":
        print("✅ Twilio credentials configured")
    else:
        print("❌ Twilio credentials not configured in .env")
else:
    print(f"❌ Unknown platform: {platform}")

# Check database
print("\n🗄️  Checking database...")
try:
    from models import init_db, SessionLocal, User
    init_db()
    db = SessionLocal()
    count = db.query(User).count()
    db.close()
    print(f"✅ Database initialized ({count} users)")
except Exception as e:
    print(f"❌ Database error: {e}")

# Test command parsing
print("\n💬 Testing command parsing...")
try:
    from reminder_service import ReminderService
    
    test_commands = [
        "remind me to drink water every 2 hours",
        "remind me to call mom at 6pm",
        "list reminders",
        "cancel all reminders",
        "done",
        "stats"
    ]
    
    for cmd in test_commands:
        cmd_type, params = ReminderService.parse_command(cmd)
        print(f"  '{cmd}' → {cmd_type}")
    
    print("✅ Command parsing working")
except Exception as e:
    print(f"❌ Command parsing error: {e}")

print("\n" + "=" * 50)
print("\n✅ Configuration test complete!")
print("\nNext steps:")
print("1. If all checks passed, run: python main.py")
print("2. For local testing, use ngrok: ngrok http 8000")
print("3. Set up webhook for your chosen platform (see README.md)")

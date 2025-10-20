"""
Main FastAPI application for HydraBot
Handles webhooks, message processing, and scheduler setup
"""

from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

from models import init_db, get_db
from reminder_service import ReminderService
from messaging_service import (
    MessagingService,
    format_reminder_created_response,
    format_reminders_list_response,
    format_reminders_cancelled_response,
    format_done_response,
    format_stats_response,
    format_unknown_command_response
)
from scheduler import start_scheduler, stop_scheduler

load_dotenv()


# Lifespan context manager for startup/shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events"""
    # Startup
    print("🚀 Starting HydraBot...")
    init_db()
    start_scheduler()
    print("✅ HydraBot is running!")
    
    yield
    
    # Shutdown
    print("⏹️  Stopping HydraBot...")
    stop_scheduler()
    print("👋 HydraBot stopped")


# Initialize FastAPI app
app = FastAPI(
    title="HydraBot",
    description="Smart reminder assistant for health tracking and personal reminders",
    version="1.0.0",
    lifespan=lifespan
)

# Initialize messaging service
messaging_service = MessagingService()


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "running",
        "service": "HydraBot",
        "platform": os.getenv("MESSAGING_PLATFORM", "telegram")
    }


@app.post("/webhook/twilio")
async def twilio_webhook(request: Request, db: Session = Depends(get_db)):
    """Handle incoming SMS from Twilio"""
    try:
        form_data = await request.form()
        from_number = form_data.get("From")
        message_body = form_data.get("Body", "").strip()
        
        # Process the message
        response_text = await process_message(
            db=db,
            platform="twilio",
            platform_id=from_number,
            message=message_body
        )
        
        # Send response via Twilio's TwiML
        return PlainTextResponse(
            content=f"<?xml version='1.0' encoding='UTF-8'?><Response><Message>{response_text}</Message></Response>",
            media_type="application/xml"
        )
    
    except Exception as e:
        print(f"❌ Error in Twilio webhook: {e}")
        return PlainTextResponse(
            content="<?xml version='1.0' encoding='UTF-8'?><Response><Message>Sorry, an error occurred.</Message></Response>",
            media_type="application/xml"
        )


@app.post("/webhook/telegram")
async def telegram_webhook(request: Request, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """Handle incoming messages from Telegram"""
    try:
        data = await request.json()
        
        # Extract message info
        if "message" in data:
            message = data["message"]
            chat_id = str(message["chat"]["id"])
            text = message.get("text", "").strip()
            
            # Process the message in background
            background_tasks.add_task(
                process_and_respond_telegram,
                db=db,
                chat_id=chat_id,
                message=text
            )
        
        return {"ok": True}
    
    except Exception as e:
        print(f"❌ Error in Telegram webhook: {e}")
        return {"ok": False, "error": str(e)}


async def process_and_respond_telegram(db: Session, chat_id: str, message: str):
    """Process message and send response via Telegram"""
    response_text = await process_message(
        db=db,
        platform="telegram",
        platform_id=chat_id,
        message=message
    )
    
    # Send response
    await messaging_service.send_message("telegram", chat_id, response_text)


async def process_message(db: Session, platform: str, platform_id: str, message: str) -> str:
    """
    Core message processing logic
    Parses command, executes action, returns response text
    """
    # Get or create user
    user = ReminderService.get_or_create_user(db, platform, platform_id)
    
    # Parse command
    command_type, params = ReminderService.parse_command(message)
    
    # Execute command and generate response
    if command_type == "done":
        return handle_done_command(db, user)
    
    elif command_type == "stats":
        stats = ReminderService.get_stats(db, user)
        return format_stats_response(stats)
    
    elif command_type == "list":
        reminders = ReminderService.list_active_reminders(db, user)
        return format_reminders_list_response(reminders)
    
    elif command_type in ("cancel", "cancel_all"):
        return handle_cancel_command(db, user, command_type, params)
    
    elif command_type == "remind_recurring":
        return handle_remind_recurring(db, user, params)
    
    elif command_type == "remind_once":
        return handle_remind_once(db, user, params)
    
    else:
        return format_unknown_command_response()


def handle_done_command(db: Session, user) -> str:
    """Handle 'done' command"""
    reminder = ReminderService.mark_reminder_done(db, user)
    if reminder:
        return format_done_response(
            reminder.title,
            reminder.is_recurring,
            reminder.interval_minutes if reminder.is_recurring else None
        )
    return "No recent reminders to mark as done. Create a reminder first!"


def handle_cancel_command(db: Session, user, command_type: str, params: dict) -> str:
    """Handle cancel commands"""
    keyword = params.get("keyword") if command_type == "cancel" else None
    count = ReminderService.cancel_reminders(db, user, keyword)
    return format_reminders_cancelled_response(count, keyword)


def handle_remind_recurring(db: Session, user, params: dict) -> str:
    """Handle recurring reminder creation"""
    reminder = ReminderService.create_recurring_reminder(
        db, user,
        params["title"],
        params["interval_minutes"]
    )
    return format_reminder_created_response(
        reminder.title,
        interval_minutes=reminder.interval_minutes
    )


def handle_remind_once(db: Session, user, params: dict) -> str:
    """Handle one-time reminder creation"""
    if params["scheduled_time"]:
        reminder = ReminderService.create_one_time_reminder(
            db, user,
            params["title"],
            params["scheduled_time"]
        )
        time_str = reminder.scheduled_time.strftime("%I:%M %p")
        return format_reminder_created_response(
            reminder.title,
            scheduled_time=time_str
        )
    return "❌ Could not parse the time. Try formats like '6pm', '6:30pm', or '18:00'."


# Manual API endpoints for testing (optional)

@app.get("/api/reminders/{platform}/{platform_id}")
async def get_user_reminders(platform: str, platform_id: str, db: Session = Depends(get_db)):
    """Get all reminders for a user (for testing)"""
    user = ReminderService.get_or_create_user(db, platform, platform_id)
    reminders = ReminderService.list_active_reminders(db, user)
    
    return {
        "user": {"platform": platform, "platform_id": platform_id},
        "reminders": [
            {
                "id": r.id,
                "title": r.title,
                "is_recurring": r.is_recurring,
                "interval_minutes": r.interval_minutes,
                "next_send_at": r.next_send_at.isoformat() if r.next_send_at else None
            }
            for r in reminders
        ]
    }


@app.get("/api/stats/{platform}/{platform_id}")
async def get_user_stats(platform: str, platform_id: str, db: Session = Depends(get_db)):
    """Get stats for a user (for testing)"""
    user = ReminderService.get_or_create_user(db, platform, platform_id)
    stats = ReminderService.get_stats(db, user)
    
    return {
        "user": {"platform": platform, "platform_id": platform_id},
        "stats": {
            "total_completions": stats["total_completions"],
            "hydration_streak_days": stats["hydration_streak_days"],
            "active_reminders_count": stats["active_reminders_count"]
        }
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True
    )

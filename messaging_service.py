"""
Messaging Service - Handles Twilio SMS and Telegram Bot integrations
Provides unified interface for sending messages
"""

import os
from typing import Optional
from twilio.rest import Client
from telegram import Bot
from telegram.error import TelegramError
from dotenv import load_dotenv

load_dotenv()


class MessagingService:
    """Unified messaging service for SMS and Telegram"""
    
    def __init__(self):
        self.platform = os.getenv("MESSAGING_PLATFORM", "telegram").lower()
        
        # Initialize Twilio
        if self.platform == "twilio":
            self.twilio_client = Client(
                os.getenv("TWILIO_ACCOUNT_SID"),
                os.getenv("TWILIO_AUTH_TOKEN")
            )
            self.twilio_phone = os.getenv("TWILIO_PHONE_NUMBER")
        
        # Initialize Telegram
        elif self.platform == "telegram":
            self.telegram_bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
    
    async def send_message(self, platform: str, recipient: str, message: str) -> bool:
        """
        Send a message via the specified platform
        
        Args:
            platform: 'twilio' or 'telegram'
            recipient: phone number for SMS, chat_id for Telegram
            message: text message to send
        
        Returns:
            True if sent successfully, False otherwise
        """
        try:
            if platform == "twilio":
                return self._send_sms(recipient, message)
            elif platform == "telegram":
                return await self._send_telegram(recipient, message)
            else:
                print(f"❌ Unknown platform: {platform}")
                return False
        except Exception as e:
            print(f"❌ Error sending message: {e}")
            return False
    
    def _send_sms(self, phone_number: str, message: str) -> bool:
        """Send SMS via Twilio"""
        try:
            self.twilio_client.messages.create(
                body=message,
                from_=self.twilio_phone,
                to=phone_number
            )
            print(f"✅ SMS sent to {phone_number}")
            return True
        except Exception as e:
            print(f"❌ Error sending SMS: {e}")
            return False
    
    async def _send_telegram(self, chat_id: str, message: str) -> bool:
        """Send message via Telegram"""
        try:
            await self.telegram_bot.send_message(
                chat_id=chat_id,
                text=message
            )
            print(f"✅ Telegram message sent to {chat_id}")
            return True
        except TelegramError as e:
            print(f"❌ Error sending Telegram message: {e}")
            return False


# Helper functions for formatting responses

def format_reminder_created_response(title: str, interval_minutes: Optional[int] = None, scheduled_time: Optional[str] = None) -> str:
    """Format response when a reminder is created"""
    if interval_minutes:
        hours = interval_minutes // 60
        minutes = interval_minutes % 60
        if hours > 0 and minutes > 0:
            interval_str = f"{hours}h {minutes}m"
        elif hours > 0:
            interval_str = f"{hours} hour{'s' if hours > 1 else ''}"
        else:
            interval_str = f"{minutes} minute{'s' if minutes > 1 else ''}"
        
        return f"✅ Reminder set! I'll remind you to '{title}' every {interval_str}. Reply 'done' when you complete it."
    
    elif scheduled_time:
        return f"✅ Reminder set! I'll remind you to '{title}' at {scheduled_time}."
    
    return f"✅ Reminder set for '{title}'."


def format_reminders_list_response(reminders) -> str:
    """Format response listing active reminders"""
    if not reminders:
        return "You have no active reminders. Send a message like 'remind me to drink water every 2 hours' to create one!"
    
    response = "📋 Your active reminders:\n\n"
    for i, reminder in enumerate(reminders, 1):
        if reminder.is_recurring:
            hours = reminder.interval_minutes // 60
            minutes = reminder.interval_minutes % 60
            if hours > 0 and minutes > 0:
                interval_str = f"{hours}h {minutes}m"
            elif hours > 0:
                interval_str = f"{hours}h"
            else:
                interval_str = f"{minutes}m"
            response += f"{i}. {reminder.title} (every {interval_str})\n"
        else:
            time_str = reminder.scheduled_time.strftime("%I:%M %p") if reminder.scheduled_time else "pending"
            response += f"{i}. {reminder.title} (at {time_str})\n"
    
    return response


def format_reminders_cancelled_response(count: int, keyword: Optional[str] = None) -> str:
    """Format response when reminders are cancelled"""
    if count == 0:
        if keyword:
            return f"No active reminders found containing '{keyword}'."
        return "You have no active reminders to cancel."
    
    if keyword:
        return f"✅ Cancelled {count} reminder{'s' if count > 1 else ''} containing '{keyword}'."
    return f"✅ Cancelled all {count} reminder{'s' if count > 1 else ''}."


def format_done_response(reminder_title: str, is_recurring: bool, next_reminder_minutes: Optional[int] = None) -> str:
    """Format response when user marks reminder as done"""
    response = f"✅ Great job! Marked '{reminder_title}' as complete."
    
    if is_recurring and next_reminder_minutes:
        hours = next_reminder_minutes // 60
        minutes = next_reminder_minutes % 60
        if hours > 0 and minutes > 0:
            time_str = f"{hours}h {minutes}m"
        elif hours > 0:
            time_str = f"{hours} hour{'s' if hours > 1 else ''}"
        else:
            time_str = f"{minutes} minute{'s' if minutes > 1 else ''}"
        
        response += f" I'll remind you again in {time_str}."
    
    return response


def format_stats_response(stats: dict) -> str:
    """Format response for stats command"""
    response = "📊 Your HydraBot Stats:\n\n"
    response += f"🔥 Hydration streak: {stats['hydration_streak_days']} day{'s' if stats['hydration_streak_days'] != 1 else ''}\n"
    response += f"✅ Total completions: {stats['total_completions']}\n"
    response += f"📋 Active reminders: {stats['active_reminders_count']}\n"
    
    if stats['recent_logs']:
        response += "\n📝 Recent activity:\n"
        for log in stats['recent_logs'][:5]:
            time_str = log.timestamp.strftime("%m/%d %I:%M%p")
            response += f"  • {log.action}: {log.reminder_title or 'reminder'} ({time_str})\n"
    
    return response


def format_unknown_command_response() -> str:
    """Format response for unknown commands"""
    return (
        "❓ I didn't understand that command. Here's what you can do:\n\n"
        "• 'remind me to [task] every [X] hours' - Set recurring reminder\n"
        "• 'remind me to [task] at [time]' - Set one-time reminder\n"
        "• 'list reminders' - See all active reminders\n"
        "• 'cancel [keyword] reminders' - Cancel specific reminders\n"
        "• 'cancel all reminders' - Cancel all reminders\n"
        "• 'done' - Mark last reminder as complete\n"
        "• 'stats' - View your stats and streak\n\n"
        "Examples:\n"
        "• remind me to drink water every 2 hours\n"
        "• remind me to call mom at 6pm\n"
        "• cancel water reminders"
    )

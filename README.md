# 💧 HydraBot - Smart Reminder Assistant# 💧 HydraBot - Smart Reminder Assistant



A text-based smart reminder assistant that works via **SMS (Twilio)** or **Telegram**. Set reminders, track habits, and get notifications—all through simple text messages.A text-based smart reminder assistant that combines health tracking and personal reminders. Users interact entirely through SMS (Twilio) or Telegram to set, manage, and complete reminders.



---## ✨ Features



## 🌟 Features- **Text-based interaction** - No app required, just text messages

- **Recurring reminders** - "remind me to drink water every 2 hours"

- **📱 Text-Based Interaction** - No app required, just text messages- **One-time reminders** - "remind me to call mom at 6pm"

- **🔄 Recurring Reminders** - "remind me to drink water every 2 hours"- **Quick completion** - Reply "done" to mark reminders complete

- **⏰ One-Time Reminders** - "remind me to call mom at 6pm"- **Smart scheduling** - Recurring reminders reset when you respond "done"

- **✅ Quick Completion** - Reply "done" to mark reminders complete- **Stats tracking** - Track your hydration streak and completion history

- **🔥 Smart Scheduling** - Intervals reset when you respond "done"- **Dual platform support** - Works with both SMS (Twilio) and Telegram

- **📊 Stats Tracking** - Track hydration streaks and completion history

- **🎯 Natural Language** - Works with everyday language## 🚀 Quick Start



---### Prerequisites



## 🚀 Quick Start (5 Minutes)- Python 3.8+

- Twilio account (for SMS) OR Telegram Bot Token

### Prerequisites- SQLite (included with Python)

- Python 3.8+ (Python 3.13 supported)

- Telegram account OR Twilio account (for SMS)### Installation



### Installation1. **Clone and navigate to the project:**

```bash

```bashcd hydrabot

# 1. Clone/navigate to project```

cd hydrabot

2. **Create virtual environment:**

# 2. Run automated setup```bash

chmod +x setup.shpython -m venv venv

./setup.shsource venv/bin/activate  # On Windows: venv\Scripts\activate

```

# Or manual setup:

python3 -m venv venv3. **Install dependencies:**

source venv/bin/activate```bash

pip install -r requirements.txtpip install -r requirements.txt

cp .env.example .env```

```

4. **Set up environment variables:**

### Configuration```bash

cp .env.example .env

Edit `.env` file with your credentials:```



#### Option A: Telegram (Recommended - Free & Easy)Edit `.env` and add your API keys:



```env**For Telegram (recommended for testing):**

MESSAGING_PLATFORM=telegram```env

TELEGRAM_BOT_TOKEN=your_bot_token_hereMESSAGING_PLATFORM=telegram

```TELEGRAM_BOT_TOKEN=your_bot_token_here

```

**Get Telegram Token:**

1. Open Telegram, search for `@BotFather`**For Twilio (SMS):**

2. Send: `/newbot````env

3. Follow prompts, copy the tokenMESSAGING_PLATFORM=twilio

4. Paste into `.env`TWILIO_ACCOUNT_SID=your_account_sid

TWILIO_AUTH_TOKEN=your_auth_token

#### Option B: Twilio SMSTWILIO_PHONE_NUMBER=+1234567890

```

```env

MESSAGING_PLATFORM=twilio5. **Run the application:**

TWILIO_ACCOUNT_SID=your_account_sid```bash

TWILIO_AUTH_TOKEN=your_auth_tokenpython main.py

TWILIO_PHONE_NUMBER=+1234567890```

```

The server will start on `http://localhost:8000`

**Get Twilio Credentials:**

1. Sign up at https://www.twilio.com/try-twilio## 📱 Platform Setup

2. Get a phone number

3. Copy credentials from console### Option 1: Telegram (Easier for Testing)



### Start the Server1. **Create a bot:**

   - Message [@BotFather](https://t.me/botfather) on Telegram

```bash   - Send `/newbot` and follow instructions

source venv/bin/activate   - Copy the bot token

python main.py

```2. **Set webhook:**

```bash

You should see:curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://your-domain.com/webhook/telegram"

``````

🚀 Starting HydraBot...

✅ Database initialized successfully3. **For local testing, use ngrok:**

⏰ Scheduler started - checking for reminders every minute```bash

✅ HydraBot is running!ngrok http 8000

```# Use the ngrok URL for webhook

```

---

### Option 2: Twilio (SMS)

## 🌐 Webhook Setup (For Local Testing)

1. **Sign up at [Twilio](https://www.twilio.com/)**

### Using ngrok (Easiest)

2. **Get credentials:**

```bash   - Account SID

# Install ngrok   - Auth Token

sudo snap install ngrok   - Phone Number



# Authenticate (get token from https://dashboard.ngrok.com)3. **Configure webhook:**

ngrok config add-authtoken YOUR_NGROK_TOKEN   - Go to Phone Numbers → Active Numbers → Your Number

   - Under "Messaging", set webhook URL to: `https://your-domain.com/webhook/twilio`

# Start tunnel   - Set HTTP method to POST

ngrok http 8000

```## 💬 How to Use



Copy the `https://` URL (e.g., `https://abc123.ngrok-free.app`)### Basic Commands



### Configure Webhook**Create recurring reminder:**

```

**For Telegram:**remind me to drink water every 2 hours

```bashremind me to stretch every 30 minutes

curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://abc123.ngrok-free.app/webhook/telegram"```

```

**Create one-time reminder:**

**For Twilio:**```

1. Go to Twilio Console → Phone Numbers → Your Numberremind me to call mom at 6pm

2. Under "Messaging", set webhook to: `https://abc123.ngrok-free.app/webhook/twilio`remind me to take medication at 9:30am

3. HTTP Method: POST```



### Verify Webhook**Mark reminder complete:**

```

**Telegram:**done

```bash```

curl "https://api.telegram.org/bot<YOUR_TOKEN>/getWebhookInfo"(Send this in response to any reminder)

```

**List active reminders:**

**Twilio:**```

Check your Twilio console logs for webhook activity.list reminders

```

---

**Cancel specific reminders:**

## 💬 How to Use```

cancel water reminders

### Supported Commandscancel stretch reminders

```

| Command | Example | Description |

|---------|---------|-------------|**Cancel all reminders:**

| **Recurring Reminder** | `remind me to drink water every 2 hours` | Sets up automatic reminders |```

| **One-Time Reminder** | `remind me to call mom at 6pm` | Reminder at specific time |cancel all reminders

| **List Reminders** | `list reminders` | Shows all active reminders |```

| **Cancel Specific** | `cancel water reminders` | Cancels reminders with keyword |

| **Cancel All** | `cancel all reminders` | Removes all reminders |**View stats:**

| **Mark Complete** | `done` | Marks last reminder as done |```

| **View Stats** | `stats` | Shows streak & completion history |stats

```

### Example ConversationShows your hydration streak, total completions, and recent activity.



```## 🏗️ Architecture

You: remind me to drink water every 2 hours

```

Bot: ✅ Reminder set! I'll remind you to 'drink water' every 2 hours. hydrabot/

     Reply 'done' when you complete it.├── main.py                 # FastAPI application & webhooks

├── models.py               # SQLAlchemy database models

[2 hours later...]├── reminder_service.py     # Core reminder logic & parsing

├── messaging_service.py    # Twilio/Telegram integrations

Bot: ⏰ Reminder: drink water├── scheduler.py            # APScheduler for sending reminders

     Reply 'done' when complete!├── requirements.txt        # Python dependencies

├── .env.example           # Environment variables template

You: done└── README.md              # This file

```

Bot: ✅ Great job! Marked 'drink water' as complete. 

     I'll remind you again in 2 hours.### Key Components



You: stats1. **FastAPI Backend** - Handles webhooks and REST API

2. **SQLAlchemy ORM** - Database models for users, reminders, logs

Bot: 📊 Your HydraBot Stats:3. **APScheduler** - Background scheduler checks for due reminders every minute

     🔥 Hydration streak: 3 days4. **Messaging Service** - Unified interface for SMS/Telegram

     ✅ Total completions: 125. **Reminder Service** - Parses commands, manages reminders

     📋 Active reminders: 1

```## 📊 Database Schema



---**Users**

- `id`, `platform`, `platform_id`, `created_at`

## 🛠️ CLI Management Tool

**Reminders**

HydraBot includes a CLI for managing the database:- `id`, `user_id`, `title`, `interval_minutes`, `scheduled_time`

- `is_recurring`, `is_active`, `last_sent_at`, `next_send_at`

```bash

# View statistics**ReminderLogs**

python cli.py stats- `id`, `user_id`, `reminder_id`, `action`, `reminder_title`, `timestamp`



# List all users## 🔧 API Endpoints

python cli.py users

### Webhooks

# List active reminders- `POST /webhook/twilio` - Twilio SMS webhook

python cli.py reminders- `POST /webhook/telegram` - Telegram bot webhook



# View recent logs### Testing Endpoints

python cli.py logs- `GET /` - Health check

- `GET /api/reminders/{platform}/{platform_id}` - Get user reminders

# Clean up old inactive reminders- `GET /api/stats/{platform}/{platform_id}` - Get user stats

python cli.py clean

## 🚢 Deployment

# Get help

python cli.py help### Replit

```

1. Import repository

---2. Add secrets (environment variables)

3. Run `python main.py`

## 📊 Architecture4. Use Replit URL for webhooks



### Project Structure### Render



```1. Create new Web Service

hydrabot/2. Connect repository

├── main.py              # FastAPI app & webhooks3. Build Command: `pip install -r requirements.txt`

├── models.py            # Database models (SQLAlchemy)4. Start Command: `python main.py`

├── reminder_service.py  # Core logic & command parsing5. Add environment variables

├── messaging_service.py # Twilio/Telegram integrations6. Use Render URL for webhooks

├── scheduler.py         # Background reminder sender

├── cli.py              # Management CLI tool### Railway

├── test_setup.py       # Configuration validator

├── requirements.txt     # Dependencies1. New Project → Deploy from GitHub

├── .env                # Configuration (create from .env.example)2. Add environment variables

├── Dockerfile          # Container build3. Deploy

└── docker-compose.yml  # Docker orchestration4. Use Railway URL for webhooks

```

### Docker (Optional)

### Database Schema

```dockerfile

**Users**FROM python:3.11-slim

- Tracks users by platform (SMS/Telegram) and platform ID

- Links to reminders and activity logsWORKDIR /app

COPY requirements.txt .

**Reminders**RUN pip install -r requirements.txt

- Stores recurring and one-time reminders

- Tracks timing: `last_sent_at`, `next_send_at`COPY . .

- Active/inactive status

CMD ["python", "main.py"]

**ReminderLogs**```

- Complete audit trail

- Actions: created, sent, completed, cancelled```bash

- Used for stats and streak calculationdocker build -t hydrabot .

docker run -p 8000:8000 --env-file .env hydrabot

### How It Works```



```## 🧪 Testing

User sends message

      ↓### Local Testing with Telegram

Webhook receives message

      ↓1. Start the app: `python main.py`

parse_command() extracts intent2. Start ngrok: `ngrok http 8000`

      ↓3. Set webhook with ngrok URL

ReminderService creates/updates reminder4. Message your bot on Telegram

      ↓

Response sent back to user### Manual API Testing

      ↓

Scheduler checks every minute```bash

      ↓# Check health

Due reminders sent automaticallycurl http://localhost:8000

      ↓

User replies "done"# Get reminders for a user

      ↓curl http://localhost:8000/api/reminders/telegram/123456789

Reminder marked complete, interval resets

```# Get stats

curl http://localhost:8000/api/stats/telegram/123456789

---```



## 🚢 Deployment## 📝 Environment Variables



### Option 1: Replit (Easiest)| Variable | Description | Required |

|----------|-------------|----------|

1. Import repository to Replit| `PORT` | Server port (default: 8000) | No |

2. Add secrets (environment variables)| `HOST` | Server host (default: 0.0.0.0) | No |

3. Click Run| `MESSAGING_PLATFORM` | `telegram` or `twilio` | Yes |

4. Use Replit URL for webhook| `TELEGRAM_BOT_TOKEN` | Telegram bot token | If using Telegram |

| `TWILIO_ACCOUNT_SID` | Twilio account SID | If using Twilio |

### Option 2: Render| `TWILIO_AUTH_TOKEN` | Twilio auth token | If using Twilio |

| `TWILIO_PHONE_NUMBER` | Twilio phone number | If using Twilio |

1. Create new Web Service| `DATABASE_URL` | Database URL (default: sqlite:///./hydrabot.db) | No |

2. Connect GitHub repository

3. Build Command: `pip install -r requirements.txt`## 🐛 Troubleshooting

4. Start Command: `python main.py`

5. Add environment variables**Bot not responding:**

6. Use Render URL for webhook- Check webhook is set correctly

- Verify environment variables

### Option 3: Railway- Check server logs for errors



1. New Project → Deploy from GitHub**Reminders not sending:**

2. Add environment variables- Ensure scheduler is running (check startup logs)

3. Auto-deploy enabled- Verify database contains active reminders

4. Use Railway URL for webhook- Check messaging credentials



### Option 4: Docker**Database errors:**

- Delete `hydrabot.db` and restart (resets database)

```bash- Check SQLite permissions

# Build

docker build -t hydrabot .## 🔮 Future Enhancements



# Run- [ ] Multiple reminder types (water, medication, tasks)

docker run -d -p 8000:8000 --env-file .env hydrabot- [ ] Timezone support

- [ ] Reminder templates

# Or use docker-compose- [ ] Group reminders

docker-compose up -d- [ ] Web dashboard

```- [ ] Voice reminders

- [ ] Integration with health apps

### Option 5: VPS/Cloud Server

## 📄 License

```bash

# Install dependenciesMIT License - feel free to use and modify!

sudo apt update

sudo apt install python3-pip python3-venv## 🤝 Contributing



# Set up projectThis is an MVP. Contributions welcome! Focus areas:

git clone <your-repo>- Better time parsing

cd hydrabot- More command formats

python3 -m venv venv- UI improvements

source venv/bin/activate- Additional platforms (WhatsApp, Discord)

pip install -r requirements.txt- Testing suite



# Configure## 📞 Support

cp .env.example .env

nano .env  # Add your credentialsFor issues or questions, create an issue on GitHub.



# Run with systemd or supervisor---

# Or use screen/tmux for quick testing

```Built with ❤️ using FastAPI, SQLAlchemy, and APScheduler


---

## 🧪 Testing

### Quick Test

```bash
# Run configuration test
python test_setup.py

# Check server health
curl http://localhost:8000

# View API docs
open http://localhost:8000/docs
```

### Manual Testing Checklist

- [ ] Send: "remind me to test every 1 hour"
- [ ] Verify: Confirmation received
- [ ] Send: "list reminders"
- [ ] Verify: Test reminder appears
- [ ] Wait for reminder notification
- [ ] Send: "done"
- [ ] Verify: Completion confirmed
- [ ] Send: "stats"
- [ ] Verify: Stats show 1 completion
- [ ] Send: "cancel test reminders"
- [ ] Verify: Reminder cancelled

### API Endpoints

```bash
# Health check
GET /

# Get user reminders (testing)
GET /api/reminders/{platform}/{platform_id}

# Get user stats (testing)
GET /api/stats/{platform}/{platform_id}

# Webhooks
POST /webhook/telegram
POST /webhook/twilio
```

---

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `PORT` | Server port (default: 8000) | No |
| `HOST` | Server host (default: 0.0.0.0) | No |
| `MESSAGING_PLATFORM` | `telegram` or `twilio` | Yes |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token | If using Telegram |
| `TWILIO_ACCOUNT_SID` | Twilio account SID | If using Twilio |
| `TWILIO_AUTH_TOKEN` | Twilio auth token | If using Twilio |
| `TWILIO_PHONE_NUMBER` | Twilio phone number | If using Twilio |
| `DATABASE_URL` | Database URL (default: sqlite) | No |

---

## 🐛 Troubleshooting

### Bot Not Responding

**Check webhook:**
```bash
# Telegram
curl "https://api.telegram.org/bot<TOKEN>/getWebhookInfo"

# Should show your webhook URL and pending_update_count: 0
```

**Reset webhook:**
```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://your-url.com/webhook/telegram"
```

**Check logs:**
- Look for errors in terminal where `main.py` is running
- Verify ngrok is still running (URLs change on restart)

### Reminders Not Sending

**Check scheduler:**
- Look for "⏰ Scheduler started" in logs
- Check for "📬 Found X due reminder(s)" messages

**Check database:**
```bash
python cli.py reminders
```

**Verify timing:**
```bash
python cli.py stats
```

### Database Issues

**Reset database (WARNING: deletes all data):**
```bash
rm hydrabot.db
python -c "from models import init_db; init_db()"
```

**Check database:**
```bash
python cli.py stats
```

### Module Not Found Errors

**Ensure virtual environment is activated:**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### ngrok Issues

**Reinstall:**
```bash
sudo snap remove ngrok
sudo snap install ngrok
ngrok config add-authtoken YOUR_TOKEN
```

**Check if running:**
```bash
curl http://localhost:4040/api/tunnels
```

---

## 📈 Performance & Scalability

### Current Capabilities
- **Response Time:** < 500ms for commands
- **Reminder Accuracy:** ±60 seconds
- **Database:** SQLite (good for 1000s of users)
- **Concurrent Users:** 100+ with proper hosting

### Scaling Recommendations

**100+ users → PostgreSQL**
```env
DATABASE_URL=postgresql://user:password@host:5432/hydrabot
```
Add to requirements.txt: `psycopg2-binary`

**1000+ users → Redis + Celery**
- Replace APScheduler with Celery
- Use Redis for task queue
- Add worker processes

**Multiple servers → Load Balancer**
- Use nginx or cloud load balancer
- Share PostgreSQL database
- Centralize Redis queue

---

## 🔒 Security Notes

### Production Checklist
- [ ] Use environment variables (never commit `.env`)
- [ ] Enable HTTPS (required for webhooks)
- [ ] Add rate limiting (e.g., slowapi)
- [ ] Implement webhook signature verification
- [ ] Use PostgreSQL with SSL
- [ ] Set up proper logging and monitoring
- [ ] Regular security updates
- [ ] Backup database regularly

### Best Practices
```python
# Add to main.py for rate limiting
from slowapi import Limiter
limiter = Limiter(key_func=lambda: "global")
app.state.limiter = limiter

@app.post("/webhook/telegram")
@limiter.limit("10/minute")
async def telegram_webhook(...):
    ...
```

---

## 🎯 Roadmap / Future Features

- [ ] Multiple reminder types (water, medication, tasks)
- [ ] Timezone support
- [ ] Reminder templates
- [ ] Group/shared reminders
- [ ] Web dashboard
- [ ] Voice message support
- [ ] Integration with health apps (Fitbit, Apple Health)
- [ ] WhatsApp support
- [ ] Discord bot integration
- [ ] Smart scheduling (ML-based timing)

---

## 🤝 Contributing

Contributions welcome! Areas for improvement:

1. **Better NLP** - Improve command parsing
2. **More Platforms** - WhatsApp, Discord, Slack
3. **Testing** - Add unit and integration tests
4. **UI** - Web dashboard for managing reminders
5. **Features** - Implement roadmap items

---

## 📄 License

MIT License - feel free to use and modify!

---

## 💡 Tips & Tricks

### Power User Commands

```bash
# Morning hydration reminder
remind me to drink water every 2 hours

# Stretching breaks
remind me to stretch every 30 minutes

# Medication
remind me to take vitamins at 9am

# Work breaks
remind me to take a break every 90 minutes
```

### Batch Operations

```bash
# View all your reminders
list reminders

# Cancel multiple at once
cancel water reminders
cancel stretch reminders

# Check your streak
stats
```

### CLI Power Tools

```bash
# Export stats
python cli.py stats > my_stats.txt

# Monitor in real-time
watch -n 10 python cli.py stats

# Check recent activity
python cli.py logs | head -20
```

---

## 🆘 Support

**Having issues?**

1. Check this README's Troubleshooting section
2. Run `python test_setup.py` to verify configuration
3. Check server logs for errors
4. Verify webhook with curl commands
5. Try the CLI tool: `python cli.py help`

**Common Solutions:**
- Restart the server
- Restart ngrok (URL changes on restart, update webhook!)
- Check `.env` configuration
- Verify API credentials
- Ensure virtual environment is activated

---

## 🎉 Success Metrics

This MVP is successful when:
- ✅ Users can set reminders via text
- ✅ Reminders arrive on time (±60 seconds)
- ✅ "Done" responses work correctly
- ✅ No crashes during extended operation
- ✅ Setup takes < 10 minutes
- ✅ Code is readable and maintainable

---

**Built with ❤️ using FastAPI, SQLAlchemy, and APScheduler**

Ready to deploy and test with real users in under 10 minutes! 🚀

---

## Quick Reference Card

```
📱 SETUP
1. ./setup.sh
2. Edit .env
3. python main.py
4. ngrok http 8000
5. Set webhook

💬 COMMANDS
- remind me to X every Y hours
- remind me to X at Y
- list reminders
- done
- stats
- cancel X reminders

🛠️ CLI TOOLS
- python cli.py stats
- python cli.py users
- python cli.py reminders
- python cli.py logs

🐛 DEBUGGING
- curl localhost:8000
- python test_setup.py
- Check webhook: curl bot.api
- View logs: tail terminal
```

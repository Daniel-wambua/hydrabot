<h1 align="center">💧 HydraBot - Smart Reminder Assistant</h1># 💧 HydraBot - Smart Reminder Assistant# 💧 HydraBot - Smart Reminder Assistant

<p align="center">

<a href="https://github.com/Daniel-wambua/hydrabot"><img src="https://i.ibb.co/7JMXxbF/hydra.png" width="120" /><br /></a>

<i>A text-based smart reminder assistant that works via SMS or Telegram</i>

<br />A text-based smart reminder assistant that works via **SMS (Twilio)** or **Telegram**. Set reminders, track habits, and get notifications—all through simple text messages.A text-based smart reminder assistant that combines health tracking and personal reminders. Users interact entirely through SMS (Twilio) or Telegram to set, manage, and complete reminders.

<i>Set reminders, track habits, and get notifications—all through simple text messages</i>

<br />

<b>🌐 <a href="https://github.com/Daniel-wambua/hydrabot">github.com/Daniel-wambua/hydrabot</a></b> <br />

</p>---## ✨ Features



## Motive

To create a simple, text-based reminder system that anyone can use without installing an app. 

All interactions happen via SMS or Telegram messages. Set recurring reminders for hydration, medication, or any habit you want to track. The bot sends you timely reminders, and you simply reply "done" to mark them complete. Built this way so you don't need to f\*\*k around with complicated habit-tracking apps.## 🌟 Features- **Text-based interaction** - No app required, just text messages



<details>- **Recurring reminders** - "remind me to drink water every 2 hours"

  <summary>About the Developer</summary>

- **📱 Text-Based Interaction** - No app required, just text messages- **One-time reminders** - "remind me to call mom at 6pm"

> **Professional Background**<br>

> I'm an experienced, Principal-level full stack engineer with a passion for quality, performance, mentoring, technology and open source. I believe the best judge of a developer is their code, and while I cannot share proprietary work, I have many open source projects on my [GitHub](https://github.com/Daniel-wambua) and showcase my skills at [danielwambua.dev](https://danielwambua.dev).- **🔄 Recurring Reminders** - "remind me to drink water every 2 hours"- **Quick completion** - Reply "done" to mark reminders complete

>

> This HydraBot project reflects my philosophy: build practical tools that solve real problems with elegant, maintainable code. The entire system is designed for reliability, ease of deployment, and extensibility.- **⏰ One-Time Reminders** - "remind me to call mom at 6pm"- **Smart scheduling** - Recurring reminders reset when you respond "done"



</details>- **✅ Quick Completion** - Reply "done" to mark reminders complete- **Stats tracking** - Track your hydration streak and completion history



---- **🔥 Smart Scheduling** - Intervals reset when you respond "done"- **Dual platform support** - Works with both SMS (Twilio) and Telegram



## About- **📊 Stats Tracking** - Track hydration streaks and completion history



HydraBot is a Python-based reminder assistant powered by FastAPI and SQLAlchemy. The system features:- **🎯 Natural Language** - Works with everyday language## 🚀 Quick Start



- **Natural Language Processing** - Parse commands like "remind me to drink water every 2 hours"

- **Dual Platform Support** - Works with both Twilio (SMS) and Telegram

- **Smart Scheduling** - APScheduler handles background reminder dispatch---### Prerequisites

- **Streak Tracking** - Monitors consecutive-day hydration habits

- **Database Persistence** - SQLite for local deployments, easily upgradable to PostgreSQL

- **CLI Management** - Command-line tools for administration

- **Docker Ready** - Containerized deployment with docker-compose## 🚀 Quick Start (5 Minutes)- Python 3.8+



The architecture follows clean separation of concerns: webhooks in `main.py`, business logic in `reminder_service.py`, messaging abstraction in `messaging_service.py`, and background jobs in `scheduler.py`.- Twilio account (for SMS) OR Telegram Bot Token



Why? ...Because why spend 2 minutes setting a phone reminder, when you could build an entire reminder automation system, obviously!### Prerequisites- SQLite (included with Python)



---- Python 3.8+ (Python 3.13 supported)



## Features- Telegram account OR Twilio account (for SMS)### Installation



- 📱 **Text-Based Interaction** - No app required, just text messages

- 🔄 **Recurring Reminders** - "remind me to drink water every 2 hours"

- ⏰ **One-Time Reminders** - "remind me to call mom at 6pm"### Installation1. **Clone and navigate to the project:**

- ✅ **Quick Completion** - Reply "done" to mark reminders complete

- 🔥 **Smart Scheduling** - Intervals reset when you respond "done"```bash

- 📊 **Stats Tracking** - Track hydration streaks and completion history

- 🎯 **Natural Language** - Works with everyday language```bashcd hydrabot

- 🌐 **Multi-Platform** - SMS (Twilio) or Telegram support

# 1. Clone/navigate to project```

---

cd hydrabot

## Usage

2. **Create virtual environment:**

### Quick Start (5 Minutes)

# 2. Run automated setup```bash

1. Clone the repo

2. Install dependencieschmod +x setup.shpython -m venv venv

3. Configure platform (Telegram or Twilio)

4. Start the server./setup.shsource venv/bin/activate  # On Windows: venv\Scripts\activate

5. Set up webhook

```

<details><summary>Detailed Setup Instructions</summary>

# Or manual setup:

#### Prerequisites

- Python 3.8+ (Python 3.13 supported)python3 -m venv venv3. **Install dependencies:**

- Telegram account OR Twilio account (for SMS)

source venv/bin/activate```bash

#### Installation

pip install -r requirements.txtpip install -r requirements.txt

```bash

# Clone and navigatecp .env.example .env```

cd hydrabot

```

# Run automated setup

chmod +x setup.sh4. **Set up environment variables:**

./setup.sh

### Configuration```bash

# Or manual setup:

python3 -m venv venvcp .env.example .env

source venv/bin/activate

pip install -r requirements.txtEdit `.env` file with your credentials:```

cp .env.example .env

```



#### Configuration#### Option A: Telegram (Recommended - Free & Easy)Edit `.env` and add your API keys:



Edit `.env` file with your credentials:



**Option A: Telegram (Recommended - Free & Easy)**```env**For Telegram (recommended for testing):**



```envMESSAGING_PLATFORM=telegram```env

MESSAGING_PLATFORM=telegram

TELEGRAM_BOT_TOKEN=your_bot_token_hereTELEGRAM_BOT_TOKEN=your_bot_token_hereMESSAGING_PLATFORM=telegram

```

```TELEGRAM_BOT_TOKEN=your_bot_token_here

**Get Telegram Token:**

1. Open Telegram, search for `@BotFather````

2. Send: `/newbot`

3. Follow prompts, copy the token**Get Telegram Token:**

4. Paste into `.env`

1. Open Telegram, search for `@BotFather`**For Twilio (SMS):**

**Option B: Twilio SMS**

2. Send: `/newbot````env

```env

MESSAGING_PLATFORM=twilio3. Follow prompts, copy the tokenMESSAGING_PLATFORM=twilio

TWILIO_ACCOUNT_SID=your_account_sid

TWILIO_AUTH_TOKEN=your_auth_token4. Paste into `.env`TWILIO_ACCOUNT_SID=your_account_sid

TWILIO_PHONE_NUMBER=+1234567890

```TWILIO_AUTH_TOKEN=your_auth_token



#### Start the Server#### Option B: Twilio SMSTWILIO_PHONE_NUMBER=+1234567890



```bash```

source venv/bin/activate

python main.py```env

```

MESSAGING_PLATFORM=twilio5. **Run the application:**

You should see:

```TWILIO_ACCOUNT_SID=your_account_sid```bash

🚀 Starting HydraBot...

✅ Database initialized successfullyTWILIO_AUTH_TOKEN=your_auth_tokenpython main.py

⏰ Scheduler started - checking for reminders every minute

✅ HydraBot is running!TWILIO_PHONE_NUMBER=+1234567890```

```

```

#### Webhook Setup (For Local Testing)

The server will start on `http://localhost:8000`

**Using ngrok:**

**Get Twilio Credentials:**

```bash

# Install ngrok1. Sign up at https://www.twilio.com/try-twilio## 📱 Platform Setup

sudo snap install ngrok

2. Get a phone number

# Authenticate

ngrok config add-authtoken YOUR_NGROK_TOKEN3. Copy credentials from console### Option 1: Telegram (Easier for Testing)



# Start tunnel

ngrok http 8000

```### Start the Server1. **Create a bot:**



**For Telegram:**   - Message [@BotFather](https://t.me/botfather) on Telegram

```bash

curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://abc123.ngrok-free.app/webhook/telegram"```bash   - Send `/newbot` and follow instructions

```

source venv/bin/activate   - Copy the bot token

**For Twilio:**

1. Go to Twilio Console → Phone Numbers → Your Numberpython main.py

2. Under "Messaging", set webhook to: `https://abc123.ngrok-free.app/webhook/twilio`

3. HTTP Method: POST```2. **Set webhook:**



</details>```bash



---You should see:curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://your-domain.com/webhook/telegram"



### Commands``````



| Command | Example | Description |🚀 Starting HydraBot...

|---------|---------|-------------|

| **Recurring Reminder** | `remind me to drink water every 2 hours` | Sets up automatic reminders |✅ Database initialized successfully3. **For local testing, use ngrok:**

| **One-Time Reminder** | `remind me to call mom at 6pm` | Reminder at specific time |

| **List Reminders** | `list reminders` | Shows all active reminders |⏰ Scheduler started - checking for reminders every minute```bash

| **Cancel Specific** | `cancel water reminders` | Cancels reminders with keyword |

| **Cancel All** | `cancel all reminders` | Removes all reminders |✅ HydraBot is running!ngrok http 8000

| **Mark Complete** | `done` | Marks last reminder as done |

| **View Stats** | `stats` | Shows streak & completion history |```# Use the ngrok URL for webhook



### Example Conversation```



```---

You: remind me to drink water every 2 hours

### Option 2: Twilio (SMS)

Bot: ✅ Reminder set! I'll remind you to 'drink water' every 2 hours. 

     Reply 'done' when you complete it.## 🌐 Webhook Setup (For Local Testing)



[2 hours later...]1. **Sign up at [Twilio](https://www.twilio.com/)**



Bot: ⏰ Reminder: drink water### Using ngrok (Easiest)

     Reply 'done' when complete!

2. **Get credentials:**

You: done

```bash   - Account SID

Bot: ✅ Great job! Marked 'drink water' as complete. 

     I'll remind you again in 2 hours.# Install ngrok   - Auth Token



You: statssudo snap install ngrok   - Phone Number



Bot: 📊 Your HydraBot Stats:

     🔥 Hydration streak: 3 days

     ✅ Total completions: 12# Authenticate (get token from https://dashboard.ngrok.com)3. **Configure webhook:**

     📋 Active reminders: 1

```ngrok config add-authtoken YOUR_NGROK_TOKEN   - Go to Phone Numbers → Active Numbers → Your Number



---   - Under "Messaging", set webhook URL to: `https://your-domain.com/webhook/twilio`



## Deployment# Start tunnel   - Set HTTP method to POST



### Option #1 - Docker (Recommended)ngrok http 8000

1. Clone the repo

2. Update `.env` with your credentials```## 💬 How to Use

3. Run `docker-compose up -d`

4. Configure webhook with your domain



### Option #2 - Cloud PlatformsCopy the `https://` URL (e.g., `https://abc123.ngrok-free.app`)### Basic Commands



<details><summary>Platform-Specific Guides</summary>



#### Replit### Configure Webhook**Create recurring reminder:**

1. Import repository to Replit

2. Add secrets (environment variables)```

3. Click Run

4. Use Replit URL for webhook**For Telegram:**remind me to drink water every 2 hours



#### Render```bashremind me to stretch every 30 minutes

1. Create new Web Service

2. Connect GitHub repositorycurl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://abc123.ngrok-free.app/webhook/telegram"```

3. Build Command: `pip install -r requirements.txt`

4. Start Command: `python main.py````

5. Add environment variables

6. Use Render URL for webhook**Create one-time reminder:**



#### Railway**For Twilio:**```

1. New Project → Deploy from GitHub

2. Add environment variables1. Go to Twilio Console → Phone Numbers → Your Numberremind me to call mom at 6pm

3. Auto-deploy enabled

4. Use Railway URL for webhook2. Under "Messaging", set webhook to: `https://abc123.ngrok-free.app/webhook/twilio`remind me to take medication at 9:30am



#### VPS/Cloud Server3. HTTP Method: POST```

```bash

# Install dependencies

sudo apt update

sudo apt install python3-pip python3-venv### Verify Webhook**Mark reminder complete:**



# Set up project```

git clone https://github.com/Daniel-wambua/hydrabot.git

cd hydrabot**Telegram:**done

python3 -m venv venv

source venv/bin/activate```bash```

pip install -r requirements.txt

curl "https://api.telegram.org/bot<YOUR_TOKEN>/getWebhookInfo"(Send this in response to any reminder)

# Configure

cp .env.example .env```

nano .env  # Add your credentials

**List active reminders:**

# Run with systemd or supervisor

```**Twilio:**```



</details>Check your Twilio console logs for webhook activity.list reminders



---```



## Architecture---



### Project Structure**Cancel specific reminders:**



```## 💬 How to Use```

hydrabot/

├── main.py              # FastAPI app & webhookscancel water reminders

├── models.py            # Database models (SQLAlchemy)

├── reminder_service.py  # Core logic & command parsing### Supported Commandscancel stretch reminders

├── messaging_service.py # Twilio/Telegram integrations

├── scheduler.py         # Background reminder sender```

├── cli.py              # Management CLI tool

├── test_setup.py       # Configuration validator| Command | Example | Description |

├── requirements.txt     # Dependencies

├── .env                # Configuration (create from .env.example)|---------|---------|-------------|**Cancel all reminders:**

├── Dockerfile          # Container build

└── docker-compose.yml  # Docker orchestration| **Recurring Reminder** | `remind me to drink water every 2 hours` | Sets up automatic reminders |```

```

| **One-Time Reminder** | `remind me to call mom at 6pm` | Reminder at specific time |cancel all reminders

### How It Works

| **List Reminders** | `list reminders` | Shows all active reminders |```

```mermaid

flowchart LR| **Cancel Specific** | `cancel water reminders` | Cancels reminders with keyword |

    A[User sends message] --> B[Webhook receives]

    B --> C[Parse command]| **Cancel All** | `cancel all reminders` | Removes all reminders |**View stats:**

    C --> D[ReminderService]

    D --> E[Database update]| **Mark Complete** | `done` | Marks last reminder as done |```

    E --> F[Response sent]

    | **View Stats** | `stats` | Shows streak & completion history |stats

    G[Scheduler checks] --> H{Due reminders?}

    H -->|Yes| I[Send reminder]```

    H -->|No| G

    ### Example ConversationShows your hydration streak, total completions, and recent activity.

    I --> J[User replies 'done']

    J --> K[Mark complete]

    K --> L[Reset interval]

``````## 🏗️ Architecture



### Database SchemaYou: remind me to drink water every 2 hours



- **Users** - Tracks users by platform (SMS/Telegram) and platform ID```

- **Reminders** - Stores recurring and one-time reminders with timing info

- **ReminderLogs** - Complete audit trail for stats and streak calculationBot: ✅ Reminder set! I'll remind you to 'drink water' every 2 hours. hydrabot/



---     Reply 'done' when you complete it.├── main.py                 # FastAPI application & webhooks



## CLI Management Tool├── models.py               # SQLAlchemy database models



```bash[2 hours later...]├── reminder_service.py     # Core reminder logic & parsing

# View statistics

python cli.py stats├── messaging_service.py    # Twilio/Telegram integrations



# List all usersBot: ⏰ Reminder: drink water├── scheduler.py            # APScheduler for sending reminders

python cli.py users

     Reply 'done' when complete!├── requirements.txt        # Python dependencies

# List active reminders

python cli.py reminders├── .env.example           # Environment variables template



# View recent logsYou: done└── README.md              # This file

python cli.py logs

```

# Clean up old inactive reminders

python cli.py cleanBot: ✅ Great job! Marked 'drink water' as complete. 

```

     I'll remind you again in 2 hours.### Key Components

---



## Testing

You: stats1. **FastAPI Backend** - Handles webhooks and REST API

### Quick Test

2. **SQLAlchemy ORM** - Database models for users, reminders, logs

```bash

# Run configuration testBot: 📊 Your HydraBot Stats:3. **APScheduler** - Background scheduler checks for due reminders every minute

python test_setup.py

     🔥 Hydration streak: 3 days4. **Messaging Service** - Unified interface for SMS/Telegram

# Check server health

curl http://localhost:8000     ✅ Total completions: 125. **Reminder Service** - Parses commands, manages reminders



# View API docs     📋 Active reminders: 1

open http://localhost:8000/docs

``````## 📊 Database Schema



### Manual Testing Checklist



- [ ] Send: "remind me to test every 1 hour"---**Users**

- [ ] Verify: Confirmation received

- [ ] Send: "list reminders"- `id`, `platform`, `platform_id`, `created_at`

- [ ] Verify: Test reminder appears

- [ ] Wait for reminder notification## 🛠️ CLI Management Tool

- [ ] Send: "done"

- [ ] Verify: Completion confirmed**Reminders**

- [ ] Send: "stats"

- [ ] Verify: Stats show 1 completionHydraBot includes a CLI for managing the database:- `id`, `user_id`, `title`, `interval_minutes`, `scheduled_time`



---- `is_recurring`, `is_active`, `last_sent_at`, `next_send_at`



## Configuration```bash



### Environment Variables# View statistics**ReminderLogs**



| Variable | Description | Required |python cli.py stats- `id`, `user_id`, `reminder_id`, `action`, `reminder_title`, `timestamp`

|----------|-------------|----------|

| `PORT` | Server port (default: 8000) | No |

| `HOST` | Server host (default: 0.0.0.0) | No |

| `MESSAGING_PLATFORM` | `telegram` or `twilio` | Yes |# List all users## 🔧 API Endpoints

| `TELEGRAM_BOT_TOKEN` | Telegram bot token | If using Telegram |

| `TWILIO_ACCOUNT_SID` | Twilio account SID | If using Twilio |python cli.py users

| `TWILIO_AUTH_TOKEN` | Twilio auth token | If using Twilio |

| `TWILIO_PHONE_NUMBER` | Twilio phone number | If using Twilio |### Webhooks

| `DATABASE_URL` | Database URL (default: sqlite) | No |

# List active reminders- `POST /webhook/twilio` - Twilio SMS webhook

---

python cli.py reminders- `POST /webhook/telegram` - Telegram bot webhook

## Troubleshooting



<details><summary>Common Issues & Solutions</summary>

# View recent logs### Testing Endpoints

### Bot Not Responding

python cli.py logs- `GET /` - Health check

**Check webhook:**

```bash- `GET /api/reminders/{platform}/{platform_id}` - Get user reminders

# Telegram

curl "https://api.telegram.org/bot<TOKEN>/getWebhookInfo"# Clean up old inactive reminders- `GET /api/stats/{platform}/{platform_id}` - Get user stats

```

python cli.py clean

**Reset webhook:**

```bash## 🚢 Deployment

curl -X POST "https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://your-url.com/webhook/telegram"

```# Get help



**Check logs:**python cli.py help### Replit

- Look for errors in terminal where `main.py` is running

- Verify ngrok is still running (URLs change on restart)```



### Reminders Not Sending1. Import repository



- Look for "⏰ Scheduler started" in logs---2. Add secrets (environment variables)

- Check for "📬 Found X due reminder(s)" messages

- Run `python cli.py reminders` to verify database3. Run `python main.py`



### Database Issues## 📊 Architecture4. Use Replit URL for webhooks



**Reset database (WARNING: deletes all data):**

```bash

rm hydrabot.db### Project Structure### Render

python -c "from models import init_db; init_db()"

```



### Module Not Found Errors```1. Create new Web Service



```bashhydrabot/2. Connect repository

source venv/bin/activate

pip install -r requirements.txt├── main.py              # FastAPI app & webhooks3. Build Command: `pip install -r requirements.txt`

```

├── models.py            # Database models (SQLAlchemy)4. Start Command: `python main.py`

</details>

├── reminder_service.py  # Core logic & command parsing5. Add environment variables

---

├── messaging_service.py # Twilio/Telegram integrations6. Use Render URL for webhooks

## Performance & Scalability

├── scheduler.py         # Background reminder sender

### Current Capabilities

- **Response Time:** < 500ms for commands├── cli.py              # Management CLI tool### Railway

- **Reminder Accuracy:** ±60 seconds

- **Database:** SQLite (good for 1000s of users)├── test_setup.py       # Configuration validator

- **Concurrent Users:** 100+ with proper hosting

├── requirements.txt     # Dependencies1. New Project → Deploy from GitHub

### Scaling Recommendations

├── .env                # Configuration (create from .env.example)2. Add environment variables

**100+ users → PostgreSQL**

```env├── Dockerfile          # Container build3. Deploy

DATABASE_URL=postgresql://user:password@host:5432/hydrabot

```└── docker-compose.yml  # Docker orchestration4. Use Railway URL for webhooks



**1000+ users → Redis + Celery**```

- Replace APScheduler with Celery

- Use Redis for task queue### Docker (Optional)

- Add worker processes

### Database Schema

---

```dockerfile

## Roadmap

**Users**FROM python:3.11-slim

- [ ] Multiple reminder types (water, medication, tasks)

- [ ] Timezone support- Tracks users by platform (SMS/Telegram) and platform ID

- [ ] Reminder templates

- [ ] Group/shared reminders- Links to reminders and activity logsWORKDIR /app

- [ ] Web dashboard

- [ ] Voice message supportCOPY requirements.txt .

- [ ] Integration with health apps (Fitbit, Apple Health)

- [ ] WhatsApp support**Reminders**RUN pip install -r requirements.txt

- [ ] Discord bot integration

- [ ] Smart scheduling (ML-based timing)- Stores recurring and one-time reminders



---- Tracks timing: `last_sent_at`, `next_send_at`COPY . .



## Contributing- Active/inactive status



### Pull RequestsCMD ["python", "main.py"]

Contributions welcome! Areas for improvement:

- Better NLP for command parsing**ReminderLogs**```

- More platforms (WhatsApp, Discord, Slack)

- Unit and integration tests- Complete audit trail

- Web dashboard UI

- Additional features from roadmap- Actions: created, sent, completed, cancelled```bash



### Issues- Used for stats and streak calculationdocker build -t hydrabot .

Found a bug? Have a suggestion? Open an issue on GitHub!

docker run -p 8000:8000 --env-file .env hydrabot

---

### How It Works```

## Attribution



This project uses the following open-source libraries:

```## 🧪 Testing

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework

- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and ORMUser sends message

- [APScheduler](https://apscheduler.readthedocs.io/) - Task scheduling

- [Twilio](https://www.twilio.com/) - SMS API      ↓### Local Testing with Telegram

- [python-telegram-bot](https://python-telegram-bot.org/) - Telegram Bot API

Webhook receives message

---

      ↓1. Start the app: `python main.py`

## Contributors

parse_command() extracts intent2. Start ngrok: `ngrok http 8000`

- [Daniel Wambua](https://github.com/Daniel-wambua) - Creator & Maintainer

      ↓3. Set webhook with ngrok URL

---

ReminderService creates/updates reminder4. Message your bot on Telegram

## License

      ↓

> _**[Daniel-wambua/hydrabot](https://github.com/Daniel-wambua/hydrabot)** is licensed under [MIT](https://github.com/Daniel-wambua/hydrabot/blob/HEAD/LICENSE) © [Daniel Wambua](https://danielwambua.dev) 2025._<br>

> <sup align="right">For information, see <a href="https://tldrlegal.com/license/mit-license">TLDR Legal > MIT</a></sup>Response sent back to user### Manual API Testing



<details>      ↓

<summary>Expand License</summary>

Scheduler checks every minute```bash

```

The MIT License (MIT)      ↓# Check health

Copyright (c) Daniel Wambua <daniel@wambua.com>

Due reminders sent automaticallycurl http://localhost:8000

Permission is hereby granted, free of charge, to any person obtaining a copy 

of this software and associated documentation files (the "Software"), to deal       ↓

in the Software without restriction, including without limitation the rights 

to use, copy, modify, merge, publish, distribute, sub-license, and/or sell User replies "done"# Get reminders for a user

copies of the Software, and to permit persons to whom the Software is furnished 

to do so, subject to the following conditions:      ↓curl http://localhost:8000/api/reminders/telegram/123456789



The above copyright notice and this permission notice shall be included in all Reminder marked complete, interval resets

copies or substantial portions of the Software.

```# Get stats

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,

INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR Acurl http://localhost:8000/api/stats/telegram/123456789

PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT

HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION---```

OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE

SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```

## 🚢 Deployment## 📝 Environment Variables

</details>



---

### Option 1: Replit (Easiest)| Variable | Description | Required |

<!-- License + Copyright -->

<p align="center">|----------|-------------|----------|

  <i>© <a href="https://danielwambua.dev">Daniel Wambua</a> 2025</i><br>

  <i>Licensed under <a href="https://gist.github.com/Daniel-wambua/143d2ee01ccc5c052a17">MIT</a></i><br>1. Import repository to Replit| `PORT` | Server port (default: 8000) | No |

  <a href="https://github.com/Daniel-wambua"><img src="https://i.ibb.co/4KtpYxb/octocat-clean-mini.png" /></a><br>

  <sup>Thanks for visiting :)</sup>2. Add secrets (environment variables)| `HOST` | Server host (default: 0.0.0.0) | No |

</p>

3. Click Run| `MESSAGING_PLATFORM` | `telegram` or `twilio` | Yes |

<!-- Dinosaur -->

<!-- 4. Use Replit URL for webhook| `TELEGRAM_BOT_TOKEN` | Telegram bot token | If using Telegram |

                        . - ~ ~ ~ - .

      ..     _      .-~               ~-.| `TWILIO_ACCOUNT_SID` | Twilio account SID | If using Twilio |

     //|     \ `..~                      `.

    || |      }  }              /       \  \### Option 2: Render| `TWILIO_AUTH_TOKEN` | Twilio auth token | If using Twilio |

(\   \\ \~^..'                 |         }  \

 \`.-~  o      /       }       |        /    \| `TWILIO_PHONE_NUMBER` | Twilio phone number | If using Twilio |

 (__          |       /        |       /      `.

  `- - ~ ~ -._|      /_ - ~ ~ ^|      /- _      `.1. Create new Web Service| `DATABASE_URL` | Database URL (default: sqlite:///./hydrabot.db) | No |

              |     /          |     /     ~-.     ~- _

              |_____|          |_____|         ~ - . _ _~_-_2. Connect GitHub repository

-->

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
---

**Built with ❤️ using FastAPI, SQLAlchemy, and APScheduler**

Ready to deploy and test with real users in under 10 minutes! 🚀

---
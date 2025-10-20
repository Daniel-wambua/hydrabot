<h1 align="center">💧 HydraBot</h1>
<p align="center">
<a href="https://github.com/Daniel-wambua/hydrabot"><img src="https://i.ibb.co/7JMXxbF/hydra.png" width="120" /><br /></a>
<i>Smart text-based reminder assistant via SMS or Telegram</i>
<br />
<i>Never miss hydration, medication, or important tasks</i>
<br />
<b>🌐 <a href="https://github.com/Daniel-wambua/hydrabot">github.com/Daniel-wambua/hydrabot</a></b> <br />
</p>

## Motive
Why spend hours managing reminders when you can automate them with a simple text message?
HydraBot eliminates the need for complicated apps. Just text commands like "remind me to drink water every 2 hours" and reply "done" when complete. Built this way so you don't need to f**k around with app installations and accounts.

<details>
  <summary>About the Developer</summary>

> **Professional Background**<br>
> I'm an experienced, Principal-level full stack engineer with a passion for quality, performance, mentoring, technology and open source. I believe the best judge of a developer is their code, and while I cannot share proprietary work, I have many open source projects on my [GitHub](https://github.com/Daniel-wambua) and showcase my skills at [danielwambua.dev](https://danielwambua.dev).

</details>

---

## About

HydraBot is a Python-based reminder assistant that works entirely through text messages. No app downloads, no complex setup—just pure text-based interaction.

**Core Features:**
- 📱 SMS (Twilio) or Telegram support
- 🔄 Recurring reminders with smart intervals
- ⏰ One-time scheduled reminders
- ✅ Simple "done" responses
- 📊 Habit streak tracking
- 🗄️ SQLite database (PostgreSQL ready)

**Tech Stack:**
- FastAPI for webhooks
- SQLAlchemy ORM
- APScheduler for background jobs
- Docker-ready deployment

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/Daniel-wambua/hydrabot.git
cd hydrabot

# Setup
./setup.sh

# Configure (edit .env with your API keys)
cp .env.example .env

# Run
python main.py
```

<details><summary>Deployment Options</summary>

- **Docker**: `docker-compose up -d`
- **Replit**: Import repo, add secrets, run
- **Render/Railway**: Connect repo, deploy
- **VPS**: Clone, setup, run with systemd

</details>

---

## Usage

| Command | Example |
|---------|---------|
| Set recurring | `remind me to drink water every 2 hours` |
| Set one-time | `remind me to call mom at 6pm` |
| Mark complete | `done` |
| View stats | `stats` |
| List all | `list reminders` |
| Cancel | `cancel water reminders` |

**Example Flow:**
```
You: remind me to drink water every 2 hours
Bot: ✅ Reminder set! I'll remind you every 2 hours.

[2 hours later...]
Bot: ⏰ Reminder: drink water

You: done
Bot: ✅ Great! I'll remind you again in 2 hours.
```

---

## Architecture

```
hydrabot/
├── main.py              # FastAPI webhooks
├── models.py            # Database schemas
├── reminder_service.py  # Business logic
├── messaging_service.py # SMS/Telegram
├── scheduler.py         # Background jobs
└── cli.py              # Admin tools
```

**How It Works:**
```
Message → Webhook → Parse → Database → Response
                                ↓
                    Scheduler → Send Reminders
```

---

## Contributing

Contributions welcome! Fork, improve, and submit a PR.

**Ideas for enhancement:**
- WhatsApp/Discord support
- Web dashboard
- Voice commands
- Smart scheduling with ML

---

## License

> _**[Daniel-wambua/hydrabot](https://github.com/Daniel-wambua/hydrabot)** is licensed under [MIT](https://github.com/Daniel-wambua/hydrabot/blob/HEAD/LICENSE) © [Daniel Wambua](https://danielwambua.dev) 2025._<br>
> <sup align="right">For information, see <a href="https://tldrlegal.com/license/mit-license">TLDR Legal > MIT</a></sup>

<details>
<summary>Expand License</summary>

```
The MIT License (MIT)
Copyright (c) Daniel Wambua <daniel@wambua.com>

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sub-license, and/or sell 
copies of the Software, and to permit persons to whom the Software is furnished 
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

</details>

---

<!-- License + Copyright -->
<p align="center">
  <i>© <a href="https://danielwambua.dev">Daniel Wambua</a> 2025</i><br>
  <i>Licensed under <a href="https://gist.github.com/Daniel-wambua/143d2ee01ccc5c052a17">MIT</a></i><br>
  <a href="https://github.com/Daniel-wambua"><img src="https://i.ibb.co/4KtpYxb/octocat-clean-mini.png" /></a><br>
  <sup>Thanks for visiting :)</sup>
</p>

<!-- ASCII Art -->
<!-- 
                    🌊 Stay Hydrated 🌊
                    
         _____
        /     \
       | () () |    "Drink water!"
        \  ^  /
         |||||
         |||||
         
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       H Y D R A B O T   2 0 2 5
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

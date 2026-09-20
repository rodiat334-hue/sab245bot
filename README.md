# បក្សីកីឡា-24 Telegram Bot

Simple, fast, and ad-friendly Telegram bot for **បក្សីកីឡា-24**.

## ✨ Features
- 🇰🇭 Bilingual welcome (Khmer + English)
- 🔘 Inline menu buttons (Sports / Betting Tips / Channel / Contact)
- 🔗 Direct channel & contact links
- 💬 Auto-reply to any text (keeps bot active for Telegram Ads)
- 🔁 Auto-restart on failure (Railway)
- 🚀 24/7 worker process (never sleeps)

## 🛠 Requirements
- Python 3.11+
- Telegram Bot Token from [@BotFather](https://t.me/BotFather)
- Railway account
- GitHub account

## 📦 Project Files
```
bot.py             → Main bot logic
requirements.txt   → Dependencies
Procfile           → Railway process definition
railway.json       → Railway deployment config
runtime.txt        → Python version
.env.example       → Environment variable template
.gitignore         → Ignore rules
Dockerfile         → Optional container build
README.md          → This file
```

## 🚀 Deploy on Railway

### 1. Create your bot
- Open [@BotFather](https://t.me/BotFather)
- `/newbot` → follow prompts
- Copy your **BOT_TOKEN**

### 2. Push to GitHub
```bash
git init
git add .
git commit -m "Initial bot for បក្សីកីឡា-24"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/telegram-bot.git
git push -u origin main
```

### 3. Deploy on Railway
1. Go to [railway.app](https://railway.app) → **New Project**
2. **Deploy from GitHub repo** → select your repo
3. Add **Variables**:
   | Key | Value |
   |---|---|
   | `BOT_TOKEN` | your bot token |
   | `CHANNEL_URL` | `https://t.me/yourchannel` |
   | `CONTACT_URL` | `https://t.me/yourcontact` |
4. Click **Deploy**
5. Check **Deploy Logs** → look for:
   ```
   🚀 បក្សីកីឡា-24 Bot is running...
   ```

### 4. Test
Open `https://t.me/your_bot_username` → send `/start` ✅

## 📋 BotFather Setup (for Telegram Ads)
```
/setdescription  → បក្សីកីឡា-24 | ព័ត៌មានកីឡា និង Tips ប្រចាំថ្ងៃ ⚽
/setabouttext    → ឆានែលកីឡាដ៏ល្អបំផុត | Best sports channel
/setuserpic      → upload your logo
/setcommands     → paste:
start - ចាប់ផ្តើម / Start
help - ជំនួយ / Help
menu - មឺនុយ / Menu
contact - ទំនាក់ទំនង / Contact
```

## 💡 Telegram Ads Tips
| Tip | Why |
|---|---|
| Inline buttons → instant reply | Higher engagement = lower ad cost |
| Khmer + English text | Wider reach in Cambodia |
| Channel button inside bot | Convert ad traffic → subscribers |
| Set bot profile picture | Trust → more clicks |
| `drop_pending_updates=True` | Avoid spam bursts after restart |
| Railway `ON_FAILURE` restart | Bot never stays down |

## 📄 License
MIT — see `LICENSE`

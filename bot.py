import os
import logging
from datetime import datetime
import pytz
from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
)
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    filters, ContextTypes, CallbackQueryHandler
)
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')
TIMEZONE = pytz.timezone('Asia/Phnom_Penh')

user_data = {}

def now_str():
    return datetime.now(TIMEZONE).strftime("%d/%m/%Y • %I:%M %p")

# ---------- MENU ----------
def main_menu():
    keyboard = [
        [InlineKeyboardButton("📅 ការប្រកួតថ្ងៃនេះ", callback_data='fights')],
        [InlineKeyboardButton("🏆 ផ្សាយផ្ទាល់", callback_data='live')],
        [InlineKeyboardButton("📊 លទ្ធផល", callback_data='results')],
        [InlineKeyboardButton("🎥 មើលផ្សាយ", callback_data='watch')],
        [InlineKeyboardButton("💬 ចូលរួមក្រុម", callback_data='community')],
        [InlineKeyboardButton("📞 ទំនាក់ទំនង", callback_data='contact')],
    ]
    return InlineKeyboardMarkup(keyboard)

# ---------- COMMANDS ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.id not in user_data:
        user_data[user.id] = {
            'name': user.first_name,
            'username': user.username,
            'joined': now_str()
        }

    text = f"""
🐓 *សូមស្វាគមន៍មកកាន់ បក្សីកីឡា-24!* 🐓

សួស្តី {user.first_name}! អ្នកបានភ្ជាប់ទៅកាន់មជ្ឈមណ្ឌលបក្សីកីឡាលេខ ១។

*អ្វីដែលអ្នកទទួលបាន:*
📅 កាលវិភាគប្រកួត
🏆 ព័ត៌មានផ្សាយផ្ទាល់
📊 លទ្ធផលភ្លាមៗ
🎥 តំណភ្ជាប់ផ្សាយ

🕐 បើក ២៤ ម៉ោង

សូមជ្រើសរើសជម្រើសខាងក្រោម 👇
"""
    await update.message.reply_text(
        text, reply_markup=main_menu(), parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
📖 *ពាក្យបញ្ជា*

/start – ម៉ឺនុយមេ
/fights – ការប្រកួតថ្ងៃនេះ
/live – ផ្សាយផ្ទាល់
/results – លទ្ធផល
/watch – មើលផ្សាយ
/community – ចូលរួមក្រុម
/contact – ទំនាក់ទំនង
/help – ជំនួយ

💡 ចុចប៊ូតុងម៉ឺនុយបានគ្រប់ពេល!
"""
    await update.message.reply_text(text, parse_mode='Markdown')

async def fights(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = f"""
📅 *ការប្រកួតថ្ងៃនេះ*
_{now_str()}_

🏟️ *កម្មវិធីចម្បង — ភ្នំពេញ*
🕐 ១:០០ រសៀល — ដេរី ៥ ជុំ
🕐 ៤:០០ រសៀល — ជុំជើងឯក

🏟️ *កម្មវិធីបន្ថែម — ស្តាតអូឡាំពិក*
🕐 ២:៣០ រសៀល — ដេរី ៣ ជុំ

📌 កាលវិភាគធ្វើបច្ចុប្បន្នភាពរៀងរាល់ម៉ោង។
"""
    kb = [[InlineKeyboardButton("⬅️ ត្រឡប់", callback_data='menu')]]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

async def live(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🏆 *ការផ្សាយផ្ទាល់*

🔴 *ភ្នំពេញ* — ជុំទី ៣
👥 អ្នកទស្សនា ១២,៤០០ នាក់

🔴 *ស្តាតអូឡាំពិក* — កម្មវិធីចម្បង
👥 អ្នកទស្សនា ៨,២០០ នាក់

⚠️ ការផ្សាយបើក ១៥ នាទីមុនប្រកួត។
"""
    kb = [[InlineKeyboardButton("🎥 មើលផ្សាយ", callback_data='watch')],
          [InlineKeyboardButton("⬅️ ត្រឡប់", callback_data='menu')]]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

async def results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
📊 *លទ្ធផលចុងក្រោយ*

🥇 *ប្រកួតទី ១២* — មាន់ក្រហម ឈ្នះ
⏱️ ជុំទី ២ • ៤:១២

🥇 *ប្រកួតទី ១១* — ផ្គរលាន់ ឈ្នះ
⏱️ ជុំទី ១ • ២:៤៥

🥇 *ប្រកួតទី ១០* — ឥន្ទ្រីមាស ឈ្នះ
⏱️ ជុំទី ៣ • ៦:៣០

_បច្ចុប្បន្នភាពប៉ុន្មានវិនាទីមុន។_
"""
    kb = [[InlineKeyboardButton("⬅️ ត្រឡប់", callback_data='menu')]]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

async def watch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🎥 *មើលផ្សាយផ្ទាល់*

▶️ [ផ្សាយ ១ – HD](https://example.com/stream1)
▶️ [ផ្សាយ ២ – បម្រុង](https://example.com/stream2)
▶️ [Facebook Live](https://facebook.com/example)
▶️ [YouTube Live](https://youtube.com/example)

📶 ប្រើ Wi-Fi សម្រាប់ការមើលរលូន។
"""
    kb = [[InlineKeyboardButton("⬅️ ត្រឡប់", callback_data='menu')]]
    await update.message.reply_text(
        text, reply_markup=InlineKeyboardMarkup(kb),
        parse_mode='Markdown', disable_web_page_preview=True
    )

async def community(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
💬 *ចូលរួមក្រុម*

• [ក្រុមមេ](https://t.me/yourgroup)
• [ឆានែល](https://t.me/yourchannel)
• [Facebook](https://facebook.com/yourpage)

តាមដានរាល់ការប្រកួត! 🐓
"""
    kb = [[InlineKeyboardButton("⬅️ ត្រឡប់", callback_data='menu')]]
    await update.message.reply_text(
        text, reply_markup=InlineKeyboardMarkup(kb),
        parse_mode='Markdown', disable_web_page_preview=True
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
📞 *ទំនាក់ទំនង*

• ជំនួយ: @your_username
• អ៊ីមែល: support@example.com
• ម៉ោង: ២៤ ម៉ោង

យើងឆ្លើយតបរហ័ស! ⚡
"""
    kb = [[InlineKeyboardButton("⬅️ ត្រឡប់", callback_data='menu')]]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

# ---------- TEXT HANDLER ----------
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()

    if any(w in msg for w in ['hi', 'hello', 'hey', 'សួស្តី', 'ជំរាបសួរ']):
        reply = "🐓 សូមស្វាគមន៍! ចុច /start ដើម្បីមើលម៉ឺនុយ។"
    elif any(w in msg for w in ['fight', 'schedule', 'ប្រកួត']):
        reply = "📅 ចុច /fights សម្រាប់ការប្រកួតថ្ងៃនេះ!"
    elif any(w in msg for w in ['live', 'watch', 'ផ្សាយ', 'មើល']):
        reply = "🎥 ចុច /watch សម្រាប់តំណផ្សាយ។"
    elif any(w in msg for w in ['result', 'លទ្ធផល']):
        reply = "📊 ចុច /results សម្រាប់លទ្ធផល។"
    elif any(w in msg for w in ['price', 'fee', 'តម្លៃ', 'ថ្លៃ']):
        reply = "💰 សូមទាក់ទង @your_username សម្រាប់តម្លៃ។"
    else:
        reply = "🐓 ខ្ញុំបានទទួលសារ! សាកល្បង /fights, /live, /results ឬ /watch។"

    await update.message.reply_text(reply, parse_mode='Markdown')

# ---------- BUTTONS ----------
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    data = q.data

    if data == 'menu':
        await q.edit_message_text(
            "🐓 *ម៉ឺនុយមេ*\nសូមជ្រើសរើស 👇",
            reply_markup=main_menu(), parse_mode='Markdown'
        )
    elif data == 'fights':
        await q.edit_message_text("📅 ប្រើ /fights", parse_mode='Markdown')
    elif data == 'live':
        await q.edit_message_text("🏆 ប្រើ /live", parse_mode='Markdown')
    elif data == 'results':
        await q.edit_message_text("📊 ប្រើ /results", parse_mode='Markdown')
    elif data == 'watch':
        await q.edit_message_text("🎥 ប្រើ /watch", parse_mode='Markdown')
    elif data == 'community':
        await q.edit_message_text("💬 ប្រើ /community", parse_mode='Markdown')
    elif data == 'contact':
        await q.edit_message_text("📞 ប្រើ /contact", parse_mode='Markdown')

# ---------- ERROR ----------
async def error_handler(update, context):
    logger.warning(f"Update {update} caused error {context.error}")

# ---------- MAIN ----------
async def post_init(app: Application):
    await app.bot.set_my_commands([
        BotCommand("start", "🏠 ម៉ឺនុយមេ"),
        BotCommand("fights", "📅 ការប្រកួតថ្ងៃនេះ"),
        BotCommand("live", "🏆 ផ្សាយផ្ទាល់"),
        BotCommand("results", "📊 លទ្ធផល"),
        BotCommand("watch", "🎥 មើលផ្សាយ"),
        BotCommand("community", "💬 ចូលរួមក្រុម"),
        BotCommand("contact", "📞 ទំនាក់ទំនង"),
        BotCommand("help", "📖 ជំនួយ"),
    ])

def main():
    app = (Application.builder()
           .token(BOT_TOKEN)
           .post_init(post_init)
           .build())

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("fights", fights))
    app.add_handler(CommandHandler("live", live))
    app.add_handler(CommandHandler("results", results))
    app.add_handler(CommandHandler("watch", watch))
    app.add_handler(CommandHandler("community", community))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.add_error_handler(error_handler)

    logger.info("🐓 បក្សីកីឡា-24 bot starting...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

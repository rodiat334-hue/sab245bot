import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

# ---------- Config ----------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_URL = os.environ.get("CHANNEL_URL", "https://t.me/bakseykila24")
CONTACT_URL = os.environ.get("CONTACT_URL", "https://t.me/bakseykila24")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


# ---------- Keyboards ----------
def main_menu():
    keyboard = [
        [InlineKeyboardButton("⚽ កីឡា / Sports", callback_data="sports")],
        [InlineKeyboardButton("🎯 ភ្នាល់បាល់ / Betting Tips", callback_data="tips")],
        [InlineKeyboardButton("📢 ឆានែល / Channel", url=CHANNEL_URL)],
        [InlineKeyboardButton("📞 ទំនាក់ទំនង / Contact", url=CONTACT_URL)],
    ]
    return InlineKeyboardMarkup(keyboard)


def back_menu():
    keyboard = [
        [InlineKeyboardButton("⬅️ ត្រឡប់ក្រោយ / Back", callback_data="back")]
    ]
    return InlineKeyboardMarkup(keyboard)


# ---------- Handlers ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = (
        f"សូមស្វាគមន៍ {user.first_name}! 👋\n\n"
        "🎉 សូមស្វាគមន៍មកកាន់ *បក្សីកីឡា-24* ផ្លូវការ!\n"
        "Welcome to *បក្សីកីឡា-24* official bot!\n\n"
        "👇 សូមជ្រើសរើសជម្រើសខាងក្រោម៖\n"
        "Choose an option below:"
    )
    await update.message.reply_text(
        text, reply_markup=main_menu(), parse_mode="Markdown"
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *របៀបប្រើប្រាស់ / How to use*\n\n"
        "/start - ចាប់ផ្តើម / Start\n"
        "/help - ជំនួយ / Help\n"
        "/menu - មឺនុយ / Menu\n"
        "/contact - ទំនាក់ទំនង / Contact",
        parse_mode="Markdown",
    )


async def menu_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📋 មឺនុយ / Menu:", reply_markup=main_menu())


async def contact_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📞 ទំនាក់ទំនងពួកយើង / Contact us:\n{CONTACT_URL}",
        disable_web_page_preview=True,
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "back":
        await query.edit_message_text(
            "📋 មឺនុយមេ / Main Menu:", reply_markup=main_menu()
        )
    elif data == "sports":
        await query.edit_message_text(
            "⚽ *កីឡា / Sports*\n\n"
            "ព័ត៌មានកីឡាថ្មីៗ និងលទ្ធផលបាល់ទាត់។\n"
            "Latest sports news and football results.\n\n"
            "👉 តាមដានបន្ថែមនៅឆានែលរបស់យើង!",
            reply_markup=back_menu(),
            parse_mode="Markdown",
        )
    elif data == "tips":
        await query.edit_message_text(
            "🎯 *ភ្នាល់បាល់ / Betting Tips*\n\n"
            "ទទួលបានការវិភាគ និងការណែនាំភ្នាល់ប្រចាំថ្ងៃ។\n"
            "Get daily analysis and betting recommendations.\n\n"
            "👉 ចូលរួមឆានែលសម្រាប់ Tips ប្រចាំថ្ងៃ!",
            reply_markup=back_menu(),
            parse_mode="Markdown",
        )


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🙏 អរគុណសម្រាប់សារ! សូមជ្រើសរើសពីមឺនុយខាងក្រោម៖\n"
        "Thanks for your message! Please choose from the menu below:",
        reply_markup=main_menu(),
    )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error("Exception while handling an update:", exc_info=context.error)


# ---------- Main ----------
def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is not set!")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("menu", menu_cmd))
    app.add_handler(CommandHandler("contact", contact_cmd))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    app.add_error_handler(error_handler)

    logger.info("🚀 បក្សីកីឡា-24 Bot is running...")
    app.run_polling(
        allowed_updates=Update.ALL_TYPES, drop_pending_updates=True
    )


if __name__ == "__main__":
    main()

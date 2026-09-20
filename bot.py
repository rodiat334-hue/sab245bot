async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = (
        f"សូមស្វាគមន៍ {user.first_name}! 👋\n\n"
        "🎉 សូមស្វាគមន៍មកកាន់ *Baksey24 Sports*!\n"
        "Welcome to *Baksey24 Sports*!\n\n"
        "👇 សូមជ្រើសរើសជម្រើសខាងក្រោម៖\n"
        "Choose an option below:"
    )
    await update.message.reply_text(
        text, reply_markup=main_menu(), parse_mode="Markdown"
    )

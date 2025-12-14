import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

# پیام شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📥 دانلود 480p", callback_data="480")],
        [InlineKeyboardButton("📥 دانلود 720p", callback_data="720")],
        [InlineKeyboardButton("📥 دانلود 1080p", callback_data="1080")],
    ]
    text = (
        "⚠️ توجه\n\n"
        "فایل‌ها فقط **10 ثانیه** نمایش داده می‌شوند.\n"
        "لطفاً سریع ذخیره کنید.\n\n"
        "کیفیت مورد نظر را انتخاب کنید:"
    )
    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

# هندل دکمه‌ها
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # لینک‌های کیفیت (بعداً راحت عوض می‌کنی)
    links = {
        "480": "https://t.me/c/2970237111/16",
        "720": "https://t.me/c/2970237111/17",
        "1080": "https://t.me/c/2970237111/18",
    }

    quality = query.data
    link = links.get(quality)

    if link:
        msg = await query.message.reply_text(
            f"🎬 لینک دانلود کیفیت {quality}p:\n{link}\n\n⏳ این پیام تا 10 ثانیه دیگر حذف می‌شود."
        )
        # حذف بعد 10 ثانیه
        context.job_queue.run_once(
            lambda ctx: ctx.bot.delete_message(chat_id=msg.chat_id, message_id=msg.message_id),
            10
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    app.run_polling()

if __name__ == "__main__":
    main()

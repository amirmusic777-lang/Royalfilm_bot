import logging
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# -----------------------------
# تنظیمات
TOKEN = "8318214493:AAF9ijJmmqr7s7jr2wWkNubSWU6RNSeWCkg"   # توکن را اینجا بگذار

# لینک‌های کیفیت‌ها
LINK_480 = "https://t.me/c/2970237111/16"
LINK_720 = "https://t.me/c/2970237111/17"
LINK_1080 = "https://t.me/c/2970237111/18"

# -----------------------------
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📥 دانلود 480", callback_data="480")],
        [InlineKeyboardButton("📥 دانلود 720", callback_data="720")],
        [InlineKeyboardButton("📥 دانلود 1080", callback_data="1080")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎬 یکی از کیفیت‌های زیر را انتخاب کن.\n\n⚠️ فایل پس از 10 ثانیه به صورت خودکار حذف می‌شود.",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "480":
        await query.message.reply_text(LINK_480)
    elif query.data == "720":
        await query.message.reply_text(LINK_720)
    elif query.data == "1080":
        await query.message.reply_text(LINK_1080)

    # حذف پیام بعد از 10 ثانیه
    await asyncio.sleep(10)
    await query.message.delete()

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()

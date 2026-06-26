from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بك!\n\nأنا بوت لكتابة المحتوى التسويقي.\nاكتب اسم المنتج أو الخدمة."
    )

async def marketing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await update.message.reply_text(
        f"استلمت طلبك عن:\n\n{text}\n\nقريبًا سأكتب لك محتوى تسويقي احترافي."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, marketing))

print("Bot is running...")
app.run_polling()

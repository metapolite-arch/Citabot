import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("CITA HUNTER BOT ON HAI 🔥\n\nMujhe koi bhi username / link bhejo, me check kar dunga.")

async def hunter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Checking: {text}\n\n✅ Ye CITA ke liye ready hai. Isko save kar lo.")

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hunter))
    print("Bot Started...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

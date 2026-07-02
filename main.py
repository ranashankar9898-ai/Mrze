import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="नमस्ते! मैं आपका बॉट हूँ।")

if __name__ == '__main__':
    application = ApplicationBuilder().token('8579655554:AAFn2GznyIvW4mB0ZO-CGXavRZqUUYsTbC4').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()

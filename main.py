import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="नमस्ते! मैं आपका बॉट हूँ!")

async def instacheck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="यह इंस्टाचेक का जवाब है।")

async def otp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="यह ओटीपी सेवाओं का जवाब है।")

async def moviedownload(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="यह मूवी डाउनलोड का जवाब है।")

async def allinone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="यह ऑल-इन-वन सेवाओं का जवाब है।")

if __name__ == '__main__':
    application = ApplicationBuilder().token('8579655554:AAFn2GznyIvW4mB0ZO-CGXavRZqUUYsTbC4').build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('instacheck', instacheck))
    application.add_handler(CommandHandler('otp', otp))
    application.add_handler(CommandHandler('moviedownload', moviedownload))
    application.add_handler(CommandHandler('allinone', allinone))

    application.run_polling()

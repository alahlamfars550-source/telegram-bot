import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Get your token and group ID from Render environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

async def save_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    
    # Forward any file/photo/video/audio/voice to the group
    await message.forward(chat_id=GROUP_ID)

    # Reply to user
    await message.reply_text("Your file has been saved in the group!")

app = ApplicationBuilder().token(BOT_TOKEN).build()

# Handle all file types
file_handler = MessageHandler(
    filters.Document.ALL |
    filters.PHOTO |
    filters.VIDEO |
    filters.AUDIO |
    filters.VOICE,
    save_file
)

app.add_handler(file_handler)

# Start the bot
app.run_polling()

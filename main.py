from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import logging
from apscheduler.schedulers.background import BackgroundScheduler
import ss_jadwal  # Import the ss_jadwal module
from datetime import datetime

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram bot token
TOKEN = '7473429203:AAH_SA2JlEtIZZfQ9m7ysh0bLgAsduy1exo'

# Initialize the scheduler
scheduler = BackgroundScheduler()

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Bot is online! Use /schedule to schedule a screenshot.')

async def schedule(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    if context.args:
        time_str = context.args[0]
        
        try:
            # Parse the input time string in HH:MM format
            schedule_time = datetime.strptime(time_str, "%H:%M")
            hour = schedule_time.hour
            minute = schedule_time.minute
            
            # Schedule the screenshot at the specified hour and minute
            scheduler.add_job(ss_jadwal.take_screenshot, 'cron', hour=hour, minute=minute, args=[chat_id])
            scheduler.start()
            await update.message.reply_text(f'Screenshot scheduled daily at {time_str}.')
        
        except ValueError:
            await update.message.reply_text('Invalid time format. Please use HH:MM format (e.g., 09:30).')
    else:
        await update.message.reply_text('Usage: /schedule <HH:MM>')

async def stop(update: Update, context: CallbackContext):
    scheduler.shutdown()
    await update.message.reply_text('Scheduler stopped.')

def main():
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()
    
    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("schedule", schedule))
    application.add_handler(CommandHandler("stop", stop))
    
    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()

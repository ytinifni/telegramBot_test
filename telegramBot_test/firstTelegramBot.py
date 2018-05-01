from telegram.ext import Updater, CommandHandler
import logging

updater = Updater(token='571475831:AAEd5PtYoHNXV9H84-SOOCA8BMgm1ARRTZw')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s \
- %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot,\
     please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

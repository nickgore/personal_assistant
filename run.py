import os
import re
import requests

from telegram.ext import Updater, CommandHandler
from telegram.ext.dispatcher import run_async

import google_api

API_TOKEN = os.environ.get('API_TOKEN')



def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


@run_async
def bop(update, context):
    url = get_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def google_calendar(update, context):
    chat_id = update.message.chat_id
    text = google_api.get_events()
    context.bot.sendMessage(chat_id=chat_id, text=text)


def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('events', google_calendar))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

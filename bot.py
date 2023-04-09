# Python 3.10
# Developer : Github.com/alireza536

# Importing ... 
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageFilter
from telegram.ext import Filters

from telegram.chataction import ChatAction

from telegram import Update
from telegram import ReplyKeyboardMarkup

from time import sleep , time

Messages = {
    'msg_start' : '{} درود'
}

def Start_Handller( update : Update , context : CallbackContext ):
    name = update.message.chat.first_name
    update.message.reply_text(Messages['msg_start'].format(name))


# Main
if __name__ == '__main__' :
    # Get API Token
    TOKEN = open('Token.txt' , 'r').readline()
    
    # Updater
    updater = Updater(token=TOKEN)

    # #  # Commands ... # # #

    updater.dispatcher.add_handler(CommandHandler('start' , Start_Handller))


    # Start Bot
    updater.start_polling()
    updater.idle()
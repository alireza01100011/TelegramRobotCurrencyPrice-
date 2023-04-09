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





# Main
if __name__ == '__main__' :
    # Get API Token
    TOKEN = open('Token.txt' , 'r').readline()
    
    # Updater
    updater = Updater(TOKEN)


    # Start Bot
    updater.start_polling()
    updater.idle()
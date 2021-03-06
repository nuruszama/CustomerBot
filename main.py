import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = 'Your token from BotFather'
"""replace bot token here"""
# Create the Updater and pass it your bot's token.
# Make sure to set use_context=True to use the new context based callbacks
# Post version 12 this will no longer be necessary
updater = Updater(TOKEN, use_context=True)

# Get the dispatcher to register handlers
dp_add = updater.dispatcher.add_handler
my_id = xxx
"""replace xxx with your chat_id so that bot can send yyou updates"""
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

#Send a welcome message when the command /start is issued along with sending their details to you
def start(update, context):
    i = 0
    if i == 0:
        i+=1
        update.message.reply_text('Hi! I am a telegram bot')
    if i == 1:
        user = update.message.from_user
        context.bot.send_message (chat_id = 688872009, text =
        "Someone started a chat with me. Here is the details\n\n"
        "Username    : @{}\nFull Name     : {} {}\nUser Id         : {}"
        .format(user['username'], user['first_name'], user['last_name'], user['id'])
        )
dp_add(CommandHandler("start", start))

#Send a message when the command /help is issued.
def help(update, context):
    update.message.reply_text('Help! I can only chat with you'
    )
dp_add(CommandHandler("help", help))

#Replying to user using bot
"""eg. /send your msg+chat_id to which you are sending msg"""
def send(update: Update, context: CallbackContext):
    text = context.args
    msgs = ' '.join([str(item) for item in text])
    msg = msgs.split('+')
    context.bot.send_message(text=msg[0], chat_id=msg[1]
    )
dp_add(CommandHandler("send", send))

#To delete messages send by bot in someone's chat
"""eg. /delete chat_id+message_id"""
def delete(update, context):
    text = context.args
    msgs = ' '.join([str(item) for item in text])
    msg = msgs.split('+')
    context.bot.delete_message(chat_id=msg[0],
                               message_id=msg[1])
dp_add(CommandHandler('delete', delete))

def ask(update, context):
    i = 0
    chat = update.message.chat_id
    msgid = update.message.message_id
    if i == 0:
        i+=1
        context.bot.forward_message(chat_id = my_id,
                                from_chat_id=update.message.chat_id,
                                message_id=update.message.message_id)
    if i == 1:
        context.bot.send_message(chat_id = my_id,
                                 text = f" chat_id = {chat} and message_id = {msgid}")
dp_add(MessageHandler(Filters.text, ask))

# log all errors
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
updater.dispatcher.add_error_handler(error)

def main():
    """Start the bot."""
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()

from typing import Final
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters

#inizializziamo le costanti
TOKEN : Final = "<TOKEN>"
BOTUSARNAME : Final= "<@username_bot>"


async def start_command(update, context):
    await update.message.reply_text("ciao")

async def help_command(update, context):
    await update.message.reply_text("ciao posso aiutarti?")


async def pong(update, context)->str:
    text : str = update.message.text
    if text == 'ping':
        await update.message.reply_text("pong")


if __name__ == "__main__":

#avvio del bot
    print("Avvio del bot")
    app = Application.builder().token(TOKEN).build()

#gestione comando
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(MessageHandler(filters.TEXT, pong))

#eseguiamo il loop infinito dell'applicazione
    print("Polling...")
    app.run_polling(poll_interval=3)


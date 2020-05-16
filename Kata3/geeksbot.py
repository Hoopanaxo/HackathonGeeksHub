"""

Primer bot de prueba, es necesario crear el ficher bot_token
"""
from telegram.ext import Updater, CommandHandler


def main():
    #añadir token pedido a BotFather ( en telegram )
    updater = Updater(token=open("./bot_token").read(), use_context=True)
    
    #añade el manejador para el comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))
    
    #añade manejador para el comando /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    updater.dispatcher.add_handler(CommandHandler("suma", suma))
    #Empezamos a pedir notificaciones
    updater.start_polling()

    #capturamos señales de parada
    updater.idle()

def start(update, context):
    update.message.reply_text("Hello world")
    
def repite(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    suma = int(context.args[0]) + int(context.args[1])
    update.message.reply_text(f"El resultado es: {suma}")

main()
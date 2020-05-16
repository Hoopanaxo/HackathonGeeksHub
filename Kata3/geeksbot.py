from telegram.ext import Updater, CommandHandler


def main():
    #añadir token pedido a BotFather ( en telegram )
    updater = Updater(token=open("./bot_token").read(), use_context=True)
    
    #añade el manejador para el comando start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    #Empezamos a pedir notificaciones
    updater.start_polling()

    #capturamos señales de parada
    updater.idle()

def start(update, context):
    update.message.reply_text("Hello world")
    pass

main()
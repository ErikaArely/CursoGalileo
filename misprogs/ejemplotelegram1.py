from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
import time
import mraa
led =mraa.Gpio(13)
led.dir(mraa.DIR_OUT)
#led = grove.GroveLed(4)
def iniciar(bot, update):
	bot.sendMessage(update.message.chat_id, text='Hola prueba LED')
def enciende(bot, update):
	led.write(1)
def apagado(bot, update):
	led.write(0)
def echo(boyt, update):
	bot.sendMessage(update.message.chat_id, 
text=update.message.text)

def error(bot, update, error):
	print 'La actualizacion "%s" causo el error "%s"' % (update, 
error)

updater = Updater("394417601:AAGf9ahadKg_MBPmYz1NBDVMsytd0hIv4s4")
dp = updater.dispatcher
dp.add_handler(CommandHandler("start",iniciar))
dp.add_handler(CommandHandler("on",enciende))
dp.add_handler(CommandHandler("off",apagado))
dp.add_handler(MessageHandler([Filters.text],echo))
dp.add_error_handler(error)
updater.start_polling()
updater.idle()
 
#while True:
#  entrada1 = pin2.read()
#  entrada2 = pin4.read()
#  salida = entrada1 & entrada2
#  print salida
#  led.write(salida)
#  time.sleep(1) 
 

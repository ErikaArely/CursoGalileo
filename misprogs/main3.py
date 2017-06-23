from telegram.ext import Updater, CommandHandler, MessageHandler, 
Filters
import pyupm_grove as grove

led = grove.GroveLed(4)
def iniciar(bot, update):
	bot.sendMessage(update.message.chat_id, text='Hola prueba LED')
def enciende(bot, update):
	led
def apagado(bot, update):


while True:
  entrada1 = pin2.read()
  entrada2 = pin4.read()
  salida = entrada1 & entrada2
  print salida
  led.write(salida)
  time.sleep(1) 
 

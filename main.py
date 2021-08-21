import os
import telebot
import requests

API_KEY = os.getenv('API_KEY')
LOG_URL = os.getenv('LOG_URL')
bot = telebot.TeleBot(API_KEY)

def hello_request(message):
  return message.text.lower() == "show last test"

@bot.message_handler(func=hello_request)
def show_last_test(message):
  r = requests.get(LOG_URL, allow_redirects=True)
  lastSpeedTest = r.text.splitlines()[-4:]
  
  bot.send_message(message.chat.id, "\n".join(lastSpeedTest))


@bot.message_handler(commands=['last_test'])
def last_test(message):
  r = requests.get(LOG_URL, allow_redirects=True)
  lastSpeedTest = r.text.splitlines()[-4:]
  
  bot.send_message(message.chat.id, "\n".join(lastSpeedTest))

bot.polling()
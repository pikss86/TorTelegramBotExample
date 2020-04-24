from torpy.http.requests import tor_requests_session
import telebot
from telebot import apihelper

with tor_requests_session() as s:  # returns requests.Session() object

    apihelper.session = s
    bot = telebot.TeleBot("TOKEN")

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")


    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        bot.reply_to(message, message.text)

    bot.polling()
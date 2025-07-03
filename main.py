import os
import telebot

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Привет, брат! Я работаю!")

bot.polling()

import telebot
from telebot.types import Message

bot = telebot.TeleBot("708520039:AAHPECDwonStXQyeI3_q5jlLfb_oqfxKOLk")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello Mazafaka")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "HELP!!!!!!")


@bot.message_handler(func=lambda message: True)
def LolOrAue(message: Message):
    if message.text.lower() == 'лол':
        bot.reply_to(message, 'Го лол гей!')
    else:
        bot.reply_to(message, 'Ауе!')


bot.polling()


# -*- coding: utf-8 -*-
#import telebot
from telebot import *

bot = TeleBot("920710380:AAG8uT7mRjpMXDkY13v4OZyrxt2jMV0JE6Y")

#клавиши
button_location = KeyboardButton('Отправить местоположение')
button_pre_inst = KeyboardButton('Стартовый отчет')
button_post_inst = KeyboardButton('Финальный отчет')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! I am HabrahabrExampleBot. How can i help you?")

    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")

    else:
        bot.send_message(message.from_user.id, "Sorry, i dont understand you.")

bot.polling(none_stop=True, interval=0)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_location)

# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start'])
async def handle_start_help(message):
    await message.reply("старт", reply_markup=kb.keyboard1)

 # Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    pass

bot.polling(none_stop=True, interval=1)

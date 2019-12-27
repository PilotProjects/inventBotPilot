# -*- coding: utf-8 -*-
import os
import telebot
from telebot import types
from flask import Flask, request




TOKEN = "920710380:AAG8uT7mRjpMXDkY13v4OZyrxt2jMV0JE6Y"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, message.from_user.first_name + ', я вас категорически приветствую')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def name(message):
    bot.reply_to(message,message.text)

@server.route("/920710380:AAG8uT7mRjpMXDkY13v4OZyrxt2jMV0JE6Y", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
	bot.remove_webhook()
	bot.set_webhook(url="https://iventbot.herokuapp.com/920710380:AAG8uT7mRjpMXDkY13v4OZyrxt2jMV0JE6Y")
	return "!", 200


server.run(host="127.0.0.1", port=os.environ.get('PORT',5000))
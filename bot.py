# -*- coding: utf-8 -*-
import os
import telebot
from telebot import types
from flask import Flask, request
#import dj_database_url
#import psycorg

#DATABASELINK = "postgress://tolwlqcvqtkwlm:dc04a811d45709f407be52ed65f92099f60feaa9a422e4638132816dd9023331@ec2-79-125-2-142.eu-west-1.compute.amazonaws.com:5432/dcdkaur1106ah5"

#db_info = dj_database_url.config(default=DATABASELINK)
#connection = psycorg2.connect(database=db_info.get('NAME'),
#	user=db_info.get('USER'),
#	password=db_info.get('PASSWORD'),
#	host=db_info.get('HOST'),
#	port=db_info.get('PORT'))
#cursor = connection.cursor()



TOKEN = "920710380:AAG8uT7mRjpMXDkY13v4OZyrxt2jMV0JE6Y"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, message.from_user.first_name + ', я вас fкатегорически приветствую')

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


server.run(host="0.0.0.0", port=os.environ.get('PORT'))
# -*- coding: utf-8 -*-
import telebot
import json
import requests
from keyboards import *

user_id=[]
chat_id=[]
photos=[]
location=[]
score=[]
answers=[]

# answers.append(answer)
# tracking_menu[str(chat_id)]['posision']=answers
# print(chat_id,tracking_menu[str(chat_id)]['posision'])
# with open('tracking_menu.json', 'w') as file:
#     json.dump(tracking_menu, file)


with open('tracking_menu.json', 'r') as file:
    tracking_menu = json.loads(file.read())

bot = telebot.TeleBot("920710380:AAG8uT7mRjpMXDkY13v4OZyrxt2jMV0JE6Y")

def save_position(chat_id,answer):
    len_pos=len(tracking_menu[str(chat_id)]['posision'])
    if len_pos!=0:
        tracking_menu[str(chat_id)]['posision']=answers
    else:
        pass

def main_menu(message):
    key = telebot.types.ReplyKeyboardMarkup(True,False)
    key.add(telebot.types.KeyboardButton('Отправить местоположение', request_location=True))
    # key.add(telebot.types.KeyboardButton('start_report', callback_data="yes"))
    # key.add('final_report')

    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Стартовый отчёт", callback_data=str(message.chat.id) +" start_report"+" Стартовый-отчёт")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Финальный отчёт", callback_data=str(message.chat.id) +" final_report")
    inlineKey.add(callback_button)

    send = bot.send_message(message.chat.id, "Выберите вариант: ", reply_markup=inlineKey)
    send = bot.send_message(message.chat.id, "==================", reply_markup=key)

    tracking_menu[str(message.chat.id)]['posision']=gap
    with open('tracking_menu.json', 'w') as file:
        json.dump(tracking_menu, file)



##### Функции для начало отчёта и конца отчёта, тут нужно нарисовать инлайн кнопки #####
def start_report(chat_id,to_menu):
    print("start")
    yes_no(chat_id,to_menu,'start')

def final_report(chat_id,to_menu):
    print("fin")
    yes_no(chat_id,to_menu,'fin')

def database(chat_id,answer):
    pass

# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start'])
def handle_start_help(message):
    main_menu(message)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    to_menu=message.text
    #now_menu=tracking_menu[str(message.chat.id)]['posision']
    print(message.text)
    eval(to_menu+'(message)')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    calback_data=call.data.split(' ')
    chat_id=calback_data[0]
    to_menu=calback_data[1]
    answer=calback_data[2]

    save_position(chat_id,answer)
    eval(to_menu+'(chat_id,to_menu)')

    # try:
    #     eval(to_menu+'(chat_id,to_menu)')
    #     answers=append(answer)
    #     print(answers)
    # except: # эксепт вылазит когда введена неожидаемая строка
    #     print("exept")
    #     #eval(now_menu+'(message)') # отправляется то меню, в котором находился человек последний раз
    #     pass

 # Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    #photos=append()
    print("фотка получена")
    pass

@bot.message_handler(content_types=['location'])
def handle_loc(message):
    payload = str(message.location.longitude) + ',' + str(message.location.latitude)
    url = 'https://geocode-maps.yandex.ru/1.x/?apikey=7b6e026e-a615-4157-a55c-9c7e9b90fa1a&format=json&geocode=' + payload
    r = requests.get(url)
    data = r.json()
    second=data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
    send = bot.send_message(message.chat.id, second)
    location.append(second)

bot.polling(none_stop=True, interval=1)

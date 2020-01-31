# -*- coding: utf-8 -*-
import telebot
import json
import requests
import datetime as d
import os
from keyboards import *
import transliterate
from queryToDataBase import *
import sqlite3



def  get_datetime():
    a = d.datetime.today().strftime("%Y%m%d")
    today = d.datetime.today()
    datetime=today.strftime("%Y-%m-%d-%H-%M-%S")
    return datetime


user_id=[]
chat_id=[]
photos=[]
location=[]
score=[]
answers=[]
photos_list=[]

# tracking_menu[str(chat_id)]['posision']=answers
# print(chat_id,tracking_menu[str(chat_id)]['posision'])

with open('BD.json', 'r') as file:
    tracking_menu = json.loads(file.read())

bot = telebot.TeleBot("920710380:AAG8uT7mRjpMXDkY13v4OZyrxt2jMV0JE6Y")

def save_position(chat_id,answers):
    tracking_menu['answers']=answers
    with open('BD.json', 'w') as gap:
        json.dump(tracking_menu, gap)

# Вызов главного меню с кнопкой местоположения, а также стартового инлайн меню
def main_menu(message):
    key = telebot.types.ReplyKeyboardMarkup(True,False)
    key.add(telebot.types.KeyboardButton('Отправить местоположение', request_location=True))
    #print(message.from_user.id)
    # key.add(telebot.types.KeyboardButton('start_report', callback_data="yes"))
    # key.add('final_report')

    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Старт отчёт", callback_data=str(message.chat.id) +" start_report"+" Старт-отчёт ")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Финальный отчёт", callback_data=str(message.chat.id) +" final_report"+" Финальный-отчёт ")
    inlineKey.add(callback_button)

    send = bot.send_message(message.chat.id, "Выберите вариант: ", reply_markup=inlineKey)
    send = bot.send_message(message.chat.id, "==================", reply_markup=key)

    # tracking_menu[str(message.chat.id)]['posision']=gap
    # with open('tracking_menu.json', 'w') as file:
    #     json.dump(tracking_menu, file)



##### Функции для начало отчёта и конца отчёта, тут нужно нарисовать инлайн кнопки #####
def start_report(chat_id,to_menu):
    location.clear()
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

    eval(to_menu+'(chat_id,to_menu)')
    translit = transliterate.translit(answer, reversed=True)
    answers.append(translit)

    if to_menu == 'to_main_menu':
        print("if con")
        new_location=str(location).replace("'"," ").replace("["," ").replace(","," ").replace("]"," ").replace("  "," ")
        new_answers=str(answers).replace("'"," ").replace("["," ").replace(","," ").replace("]"," ").replace("  "," ")
        #save_position(chat_id,answers)
        writeToDbJson(new_location, new_answers, int(chat_id), get_datetime(), photos_list[0], photos_list[1], photos_list[2], photos_list[3], photos_list[4])
        answers.clear()
        location.clear()
        photos_list.clear()

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
    print("get photo")
    file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    list_of_dir=os.listdir('/home/tester-vmn/projects/inventBotPilot/operface/main_oper_face/static/photos_instal/')

    if str(message.from_user.id) not in list_of_dir:
        print("no exist")
        os.mkdir('/home/tester-vmn/projects/inventBotPilot/operface/main_oper_face/static/photos_instal/'+str(message.from_user.id))
        src='/home/tester-vmn/projects/inventBotPilot/operface/main_oper_face/static/photos_instal/'+str(message.from_user.id)+'/'+get_datetime()+'.jpg'
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        photos_list.append(src.replace('/home/tester-vmn/projects/inventBotPilot/operface/main_oper_face/static/photos_instal/',''))
    else:
        print("exist")
        src='/home/tester-vmn/projects/inventBotPilot/operface/main_oper_face/static/photos_instal/'+str(message.from_user.id)+'/'+get_datetime()+'.jpg'
        print(src)
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        photos_list.append(src.replace('/home/tester-vmn/projects/inventBotPilot/operface/main_oper_face/static/photos_instal/',''))

    print(photos_list)
    bot.send_message(message.chat.id, "фото сохранено")

@bot.message_handler(content_types=['location'])
def handle_loc(message):
    print("location")
    payload = str(message.location.longitude) + ',' + str(message.location.latitude)
    url = 'https://geocode-maps.yandex.ru/1.x/?apikey=7b6e026e-a615-4157-a55c-9c7e9b90fa1a&format=json&geocode=' + payload
    r = requests.get(url)
    data = r.json()
    second=data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
    send = bot.send_message(message.chat.id, second)
    location.append(second)


bot.polling(none_stop=True, interval=1)

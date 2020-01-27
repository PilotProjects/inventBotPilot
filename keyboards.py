import telebot


bot = telebot.TeleBot("920710380:AAG8uT7mRjpMXDkY13v4OZyrxt2jMV0JE6Y")

def save_position(chat_id,to_menu):
    tracking_menu[str(chat_id)]['posision']=to_menu
    with open('tracking_menu.json', 'w') as file:
        json.dump(tracking_menu, file)

def to_main_menu(chat_id,to_menu):
    key = telebot.types.ReplyKeyboardMarkup(True,False)
    key.add(telebot.types.KeyboardButton('main_menu'))
    send = bot.send_message(chat_id, "Чтобы отправить данные нажмите  'main_menu' ", reply_markup=key)

############НАЧАЛЬНЫЙ ОТЧЁТ############
def func6(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Полный комплект", callback_data=chat_id+" to_main_menu"+" Полный-комплект")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Неполный комплект", callback_data=chat_id+" to_main_menu"+" Неполный-комплект")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Отсутствует", callback_data=chat_id+" to_main_menu"+" Отсутствует")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Абонентское оборудование в наличие? (сделать фото)', reply_markup=inlineKey)


def func5(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Необходимо сделать", callback_data=chat_id+" func6"+" Необходимо-сделат")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Присутствуют", callback_data=chat_id+" func6"+" Присутствуют")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Дополнительные отверстия в помещении (сделать фото)', reply_markup=inlineKey)

def func4(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Уже проложен", callback_data=chat_id+" func5"+" Уже-проложен")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Необходимо проложить", callback_data=chat_id+" func5"+" Необходимо-проложит")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Прокладка кабеля в помещении (сделать фото)', reply_markup=inlineKey)

def func3(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Имеется", callback_data=chat_id+" func4"+" Имеется")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Отсутствует", callback_data=chat_id+" func4"+" Отсутствует")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Вводное отверстие (сделать фото)', reply_markup=inlineKey)


def func2(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func3"+" Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func3"+" Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Проложен ли кабель в подъезде абонента? (сделать фото)', reply_markup=inlineKey)


def func1(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Отправил фото", callback_data=chat_id+" func2"+" Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет, ОКР", callback_data=chat_id+" func2"+" Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Состояние ОКР (сделать фото)', reply_markup=inlineKey)


# def main_menu(message):
#     key = telebot.types.ReplyKeyboardMarkup(True,False)
#     key.add(telebot.types.KeyboardButton('Отправить местоположение', request_location=True))
#     # key.add(telebot.types.KeyboardButton('start_report', callback_data="yes"))
#     # key.add('final_report')
#
#     inlineKey = telebot.types.InlineKeyboardMarkup()
#     callback_button = telebot.types.InlineKeyboardButton(text="Стартовый отчёт", callback_data=str(message.chat.id) +" start_report")
#     inlineKey.add(callback_button)
#     callback_button = telebot.types.InlineKeyboardButton(text="Финальный отчёт", callback_data=str(message.chat.id) +" final_report")
#     inlineKey.add(callback_button)
#
#     send = bot.send_message(message.chat.id, "Выберите вариант: ", reply_markup=inlineKey)
#     send = bot.send_message(message.chat.id, "==================", reply_markup=key)


def yes_no(chat_id,to_menu,report):
    if report=='start':
        func1(chat_id,to_menu)
    else:
        func1_fin(chat_id,to_menu)


############КОНЕЧНЫЙ ОТЧЁТ############
def func4_fin(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" to_main_menu"+" yes")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" to_main_menu"+" no")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Прокладка кабеля? (сделать фото)', reply_markup=inlineKey)


def func3_fin(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Имеется", callback_data=chat_id+" func4_fin"+" yes")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Отсутствует", callback_data=chat_id+" func4_fin"+" no")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Вводное отверстие (сделать фото)', reply_markup=inlineKey)


def func2_fin(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func3_fin"+" yes")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func3_fin"+" no")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Проложен ли кабель в подъезде абонента? (сделать фото)', reply_markup=inlineKey)


def func1_fin(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Сделал", callback_data=chat_id+" func2_fin"+" yes")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет, ОКР", callback_data=chat_id+" func2_fin"+" no")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Состояние ОКР (сделать фото)', reply_markup=inlineKey)


# def main_menu(message):
#     key = telebot.types.ReplyKeyboardMarkup(True,False)
#     key.add(telebot.types.KeyboardButton('Отправить местоположение', request_location=True))
#     # key.add(telebot.types.KeyboardButton('start_report', callback_data="yes"))
#     # key.add('final_report')
#
#     inlineKey = telebot.types.InlineKeyboardMarkup()
#     callback_button = telebot.types.InlineKeyboardButton(text="Стартовый отчёт", callback_data=str(message.chat.id) +" start_report"+" Стартовый-отчёт")
#     inlineKey.add(callback_button)
#     callback_button = telebot.types.InlineKeyboardButton(text="Финальный отчёт", callback_data=str(message.chat.id) +" final_report")
#     inlineKey.add(callback_button)
#
#     send = bot.send_message(message.chat.id, "Выберите вариант: ", reply_markup=inlineKey)
#     send = bot.send_message(message.chat.id, "==================", reply_markup=key)

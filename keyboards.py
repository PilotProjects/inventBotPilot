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

def start_final_report(chat_id,to_menu):
    func1_fin(chat_id,to_menu)
    # key = telebot.types.ReplyKeyboardMarkup(True,False)
    # key.add(telebot.types.KeyboardButton('main_menu'))
    # send = bot.send_message(chat_id, "Чтобы отправить данные нажмите  'main_menu' ", reply_markup=key)

############НАЧАЛЬНЫЙ ОТЧЁТ############

def func7(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" start_final_report"+" Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" to_main_menu"+" Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Клиенту необходима вторая ТВ приставка?', reply_markup=inlineKey)

def func6(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Определил абонент", callback_data=chat_id+" func7"+" Определил абонент")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Определил инсталлятор", callback_data=chat_id+" func7"+" Определил инсталлятор")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Расположение точки доступа Wi-Fi', reply_markup=inlineKey)

def func5(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func6"+" Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func6"+" Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Абонент хочет воспользоваться PLC адаптером?', reply_markup=inlineKey)

def func4(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func5"+" Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func5"+" Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Необходимо ли проделать доп. отверстие в помещении? (сделать фото)', reply_markup=inlineKey)

def func3(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func4"+" Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func4"+" Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Необходимо ли проделать доп. отверстие для ввода кабеля в жилое помещение? (сделать фото)', reply_markup=inlineKey)


def func2(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Выполнена с коробом", callback_data=chat_id+" func3"+" Выполнена с коробом")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Выполнена без короба", callback_data=chat_id+" func3"+" Выполнена без короба")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет проводки кабеля", callback_data=chat_id+" func3"+" Нет проводки кабеля")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Выполнена ли проводка кабеля в подъезде? (сделать фото)', reply_markup=inlineKey)


def func1(chat_id,to_menu):
    print("func1_1")
    inlineKey = telebot.types.InlineKeyboardMarkup()
    print("func1_2")
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func2"+" Да")
    print("func1_3")
    inlineKey.add(callback_button)
    print("func1_4")
    callback_button = telebot.types.InlineKeyboardButton(text="Нет (оборудование РТ)", callback_data=chat_id+" func2"+" Нет (оборудование РТ)")
    print("func1_5")
    inlineKey.add(callback_button)
    print("func1_6")
    callback_button = telebot.types.InlineKeyboardButton(text="Невозможно настроить оборудование", callback_data=chat_id+" func2"+" Невозможно настроить оборудование")
    print("func1_7")
    inlineKey.add(callback_button)
    print("func1_8",inlineKey)
    bot.send_message(chat_id,'Клиент желает настроить своё оборудование?', reply_markup=inlineKey)

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
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func4_fin"+" Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func4_fin"+" Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Абонент ознакомлен с основными моментами пользования Интернет, IPTV, OTA?', reply_markup=inlineKey)


def func2_fin(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func3_fin"+" Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func3_fin"+" Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Продемонстрирована работоспособность всех услуг?', reply_markup=inlineKey)


def func1_fin(chat_id,to_menu):
    print("финальный первая функция")
    # inlineKey = telebot.types.InlineKeyboardMarkup()
    # callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func2_fin"+" Да")
    # inlineKey.add(callback_button)
    # callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func2_fin"+" Нет")
    # inlineKey.add(callback_button)
    # bot.send_message(chat_id,'Логин и пароль от Wi-Fi сети наклеен на оборудование?(сделать фото)', reply_markup=inlineKey)


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

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

def final(chat_id,to_menu):
    key = telebot.types.ReplyKeyboardMarkup(True,False)
    key.add(telebot.types.KeyboardButton('start_final_report'))
    send = bot.send_message(chat_id, "Чтоб начать стартовый отчёт нажмите 'start_final_report' ", reply_markup=key)

############НАЧАЛЬНЫЙ ОТЧЁТ############

def func7(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" final"+" start_Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" final"+" start_Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Клиенту необходима вторая ТВ приставка?', reply_markup=inlineKey)

def func6(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Определил абонент", callback_data=chat_id+" func7"+" start_абонент")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Определил инсталлятор", callback_data=chat_id+" func7"+" start_инсталлятор")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Расположение точки доступа Wi-Fi', reply_markup=inlineKey)

def func5(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func6"+" start_Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func6"+" start_Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Абонент хочет воспользоваться PLC адаптером?', reply_markup=inlineKey)

def func4(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func5"+" start_Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func5"+" start_Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Необходимо ли проделать доп. отверстие в помещении? (сделать фото)', reply_markup=inlineKey)

def func3(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func4"+" start_Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func4"+" start_Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Необходимо ли проделать доп. отверстие для ввода кабеля в жилое помещение? (сделать фото)', reply_markup=inlineKey)


def func2(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Выполнена с коробом", callback_data=chat_id+" func3"+" start_Выполнена с коробом")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Выполнена без короба", callback_data=chat_id+" func3"+" start_Выполнена без короба")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет проводки кабеля", callback_data=chat_id+" func3"+" start_Нет проводки кабеля")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Выполнена ли проводка кабеля в подъезде? (сделать фото)', reply_markup=inlineKey)


def func1(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func2"+" start_Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет (оборудование РТ)", callback_data=chat_id+" func2"+" start_оборудование РТ")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Невозможно настроить оборудование", callback_data=chat_id+" func2"+" start_Невозможно настроить")
    inlineKey.add(callback_button)
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
def func7_fin(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" to_main_menu"+" final_Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" to_main_menu"+" final_Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Абонент зарегестрирован в личном кабинете?', reply_markup=inlineKey)

def func6_fin(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func7_fin"+" final_Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func7_fin"+" final_Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Продемонстрирована скорость подключения?(сделать фото)', reply_markup=inlineKey)


def func5_fin(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func6_fin"+" final_Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func6_fin"+" final_Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Клиент ознакомлен с доп. сервисами и функциями ИТВ?', reply_markup=inlineKey)

def func4_fin(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func5_fin"+" final_Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func5_fin"+" final_Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Произведена настройка пульта дист. управления STB?', reply_markup=inlineKey)


def func3_fin(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func4_fin"+" final_Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func4_fin"+" final_Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Абонент ознакомлен с основными моментами пользования Интернет, IPTV, OTA?', reply_markup=inlineKey)


def func2_fin(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func3_fin"+" final_Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func3_fin"+" final_Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Продемонстрирована работоспособность всех услуг?', reply_markup=inlineKey)


def func1_fin(chat_id,to_menu):
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Да", callback_data=chat_id+" func2_fin"+" final_Да")
    inlineKey.add(callback_button)
    callback_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data=chat_id+" func2_fin"+" final_Нет")
    inlineKey.add(callback_button)
    bot.send_message(chat_id,'Логин и пароль от Wi-Fi сети наклеен на оборудование?(сделать фото)', reply_markup=inlineKey)


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

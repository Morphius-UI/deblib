import time
from webbrowser import Error

import telebot
from pyexpat.errors import messages
from telebot import types
import backup
import pars_info



checker = False
token = '7475078721:AAHUczpsSz63r1AB736Yhz1ME5q8F7rpUhA'
bot = telebot.TeleBot(token)
students = []
adm = {}
adm_propusk = 0
hash1 = open('admin.txt', 'w')
hash1.write('admin ')
hash1.write(str(hash(' ')))
hash1.close()
with open('admin.txt') as file:
    for line in file:
        key, *value = line.split()
        adm[key] = value

pagesshop = 2
pagenow = 1
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Учитель")
    item2 = types.KeyboardButton("Ученик")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Кто вы?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def cheak0(message):
    if message.text == 'Ученик':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        log = types.KeyboardButton("Войти")
        reg = types.KeyboardButton("Регистрация")
        back = types.KeyboardButton('Назад')
        markup.add(log, reg, back)
        bot.send_message(message.chat.id, 'Вход/регистрация', reply_markup=markup)
        bot.register_next_step_handler(message, child)

    if message.text == 'Учитель':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Назад')
        markup.add(back)
        bot.send_message(message.chat.id, 'Логин:', reply_markup=markup)
        bot.register_next_step_handler(message, cheak1)

    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Учитель")
        item2 = types.KeyboardButton("Ученик")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Кто вы?', reply_markup=markup)




def cheak1(message):
    gan = True
    while gan == True:
        if message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Учитель")
            item2 = types.KeyboardButton("Ученик")
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Кто вы?', reply_markup=markup)
            gan = False
            break

        if message.text != 'admin':
            bot.send_message(message.chat.id, 'Логин неверный')
            bot.register_next_step_handler(message, cheak1)
            break

        else:
            gan = False
            bot.register_next_step_handler(message, admin_base_login)
            bot.send_message(message.chat.id, 'Введите пароль')

def admin_base_login(message):
    gan = True
    string = ''.join(map(str, adm.get('admin')))
    while gan == True:
        if str(hash(message.text)) != string:
            bot.send_message(message.chat.id, 'Пароль неверный')
            bot.register_next_step_handler(message, admin_base_login)
            break
        else:
            gan = False
            bot.send_message(message.chat.id, 'Добро пожаловать, admin!')
            adm_propusk = 1
            print('Вход выполнен, admin, ' + str(message.chat.id))

def child(message):
    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Учитель")
        item2 = types.KeyboardButton("Ученик")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Кто вы?', reply_markup=markup)
        bot.register_next_step_handler(message, cheak0)

    if message.text == 'Войти':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Назад")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Введите логин и пароль в формате:\n'
                                          'Логин Пароль', reply_markup=markup)
        bot.register_next_step_handler(message, auth)
    if message.text== "Регистрация":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Назад")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Введите свои данные в формате:\n ФИО(ваше ФИО)/Логин(может быть любым)/Класс(Ваш класс)/Пароль(Главное запомните)', reply_markup=markup)
        bot.register_next_step_handler(message, register_child)


def auth(message):
    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Войти")
        item2 = types.KeyboardButton("Регистрация")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Вход/регистрация', reply_markup=markup)
        bot.register_next_step_handler(message, child)

    else:
        try:
            login, password = message.text.split()
            cheak = pars_info.cheaklogin(login)
            print(cheak)
            with open('students.txt') as file:
                for line in file:
                    key, value = line.split()
                    students.append(key and value)
                    if key == login and str(value) == password and cheak == True:
                        bot.send_message(message.chat.id, 'Добро пожаловать, ' + login)
                        time.sleep(1)
                        global fiola
                        global log
                        global klassin
                        fiola = pars_info.cheakfio(key)
                        log = key
                        klassin = pars_info.cheakklass(key)

                        menu(message)

                        #, startapp
                    else:
                        print(login, password, key, value)
                        continue
        except Error:
            bot.send_message(message.chat.id, 'Неправильный формат или неверные данные, попробуйте еще раз')
            bot.register_next_step_handler(message, auth)  # , startapp




def register_child(message):
    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Войти")
        item2 = types.KeyboardButton("Регистрация")
        item3 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Вход/регистрация', reply_markup=markup)
        bot.register_next_step_handler(message, child)
    else:
        try:
            list = []
            exel = []
            fio, login, klass, password = message.text.split('/')
            list.append(fio)
            list.append(int(klass))
            list.append(False)
            if pars_info.cheaklogin(login) == False:
                if backup.cheakreg(list) == True:
                    a = open('students.txt', 'a')
                    exel.append(login)
                    exel.append(fio)
                    exel.append(klass)
                    global fiola
                    global log
                    global klassin
                    fiola = fio
                    log = login
                    klassin = klass
                    a.write("\n" + login + ' ' + password)
                    backup.register(exel)
                    #backup.cheakreg(fio, 0)
                    bot.send_message(message.chat.id, 'Добро пожаловать, ' + login)
                    time.sleep(1)
                    menu(message)

                else:
                    bot.send_message(message.chat.id, 'Вы уже зарегистрированы')
                    bot.register_next_step_handler(message, register_child)


            else:
                bot.send_message(message.chat.id, 'Данный логин уже занят, выберете другой')
                bot.register_next_step_handler(message, register_child)


        except Error:
            bot.send_message(message.chat.id, 'Неправильный формат, попробуйте еще раз')
            bot.register_next_step_handler(message, register_child)  # , startapp



def menu(message):
    global pagenow
    global pagesshop
    markup = types.InlineKeyboardMarkup()
    magaz = types.InlineKeyboardButton("💼Магазин", callback_data="magaz")
    minigame = types.InlineKeyboardButton("⚽️Мини-игры", callback_data="minigame")
    score = types.InlineKeyboardButton("🎖Мой профиль", callback_data="score")
    markup.add(magaz, minigame, score)
    bot.send_message(message.chat.id,"<b>Добро пожаловать в Ldod score!😁</b>\nЗдесь вы можете получить награды за хорошие отметки..\nЗа каждую четвертную отметку вы получаете очки, которые вы можете потратить на призы в разделе 'Магазин'😌\nТакже вы получаете возможность самостоятельно накопить на данные награды с помощью раздела 'Мини-игры'..\nИграйте, развивайтесь и получайте призы😎", reply_markup=markup, parse_mode='HTML')
    bot.register_next_step_handler(message, answermenu)

@bot.callback_query_handler(func=lambda call: True)
def answermenu(call):
    global pagesshop
    global pagenow
    global chat_id
    global message_id
    global fiola
    global klassin
    global log
    message_id = call.message.message_id
    chat_id = call.message.chat.id
    if call.data == 'magaz':
        markup = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text="Назад в меню", callback_data='back')
        t1 = types.InlineKeyboardButton(text="Товар", callback_data='t1')
        markup.add(back, t1)
        textmagaz = 'Добро пожаловать в магазин💼\nЗдесь вы можете преобрести товары за ваши поинты.\nВаши поинты:' #+ points
        bot.edit_message_text(textmagaz, reply_markup = markup, chat_id=call.message.chat.id, message_id=call.message.message_id)

    if call.data == 'back':
        bot.delete_message(call.message.chat.id, call.message.id)
        menu(call.message)

    if call.data == "t1":
        markup = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text="Назад в меню", callback_data='back')
        markup.add(back)
        bot.edit_message_text("Товар пока недоступен", reply_markup=markup, chat_id=chat_id, message_id=message_id)

    if call.data == 'minigame':
        markup = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text="Назад в меню", callback_data='back')
        g1 = types.InlineKeyboardButton(text="Крестики нолики", callback_data='g1')
        g2 = types.InlineKeyboardButton(text="4 в ряд", callback_data='g2')
        g3 = types.InlineKeyboardButton(text="Морской бой", callback_data='g3')
        markup.add(g1, g2, g3, back)
        textminigame = 'Добро пожаловать в магазин💼\nЗдесь вы можете преобрести товары за ваши поинты.\nВаши поинты:'  # + points
        bot.edit_message_text(textminigame, reply_markup=markup, chat_id=call.message.chat.id, message_id=call.message.message_id)
    if call.data == 'g1':
        markup = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text="Назад в меню", callback_data='back')
        lvl1 = types.InlineKeyboardButton(text="Легкий", callback_data='lvl1')
        lvl2 = types.InlineKeyboardButton(text="Средний", callback_data='lvl2')
        lvl3 = types.InlineKeyboardButton(text="Тяжелый", callback_data='lvl3')
        lvl4 = types.InlineKeyboardButton(text="Невозможный", callback_data='lvl4')
        markup.add(lvl1, lvl2, lvl3, lvl4, back)
        bot.edit_message_text("<b>🎓ИГРА КРЕСТИКИ НОЛИКИ🎓</b>\nПравила: вы играете с искусственным интеллектом, ваша задача обыграть его😁\nВ случае победы вы получаете"
                              "ваши токены + к этому награда за игру\n<b>Играть вы можете всего 5 раз в день</b>\n\n<b>Легкий</b>\nВзнос на игру:10токенов\nВозможный выйгрыш:10 токенов\n"
                              "\n<b>Средний</b>\nВзнос на игру:15токенов\nВозможный выйгрыш:15 токенов\n"
                              "\n<b>Тяжелый</b>\nВзнос на игру:20токенов\nВозможный выйгрыш:20 токенов\n"
                              "\n<b>Невозможный</b>\nВзнос на игру:40токенов\nВозможный выйгрыш:99999 токенов", reply_markup=markup, chat_id=chat_id, message_id=message_id, parse_mode='HTML')
    if call.data == 'score':
        markup = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text="Назад в меню", callback_data='back')
        cheaktruth = types.InlineKeyboardButton(text="Проверить вычисления ваших поинтов", callback_data='cheaktruth')
        markup.add(cheaktruth, back)
        profile = f'<b>Ваш профиль</b>\n\nВаше фио:<b>{fiola}</b>\n\nВаш логин:<b>{log}</b>\n\nВаш класс:<b>{klassin}</b>\n\nВаши поинты:n'  # + points
        bot.edit_message_text(profile, reply_markup=markup, chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="HTML")




bot.infinity_polling()


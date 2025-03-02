import requests
import telebot
from telebot import types
import time
import random
import requests
import re
from peewee import *
from datetime import date
import calendar
import threading

Token = '7854708699:AAEXpUSOfUYyLrqb0X9X1zx65KCDQkKn1hc'
root = telebot.TeleBot(Token)

#chat_member = root.get_chat_member(message_id, message_id).user.username


k = 0
db = SqliteDatabase('fof.sqlite')


class MoonveilFaucet:
    def __init__(
            self,
            rpc: str = "https://faucet.testnet.moonveil.gg/api/claim",
            address: str = "",
            proxy=None
    ):
        self.rpc = rpc
        self.address = address
        self.proxy = proxy

    def classic(self):
        url = f'{self.rpc}'
        json_data = {
            'address': self.address
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': 'https://faucet.testnet.moonveil.gg/',
            'Content-Type': 'application/json',
            'Origin': 'https://faucet.testnet.moonveil.gg',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'DNT': '1',
            'Priority': 'u=0',
            'TE': 'trailers'}

        request = requests.post(url, json=json_data, headers=headers,
                                proxies={'http': self.proxy, 'https': self.proxy}).json()
        return request["msg"]





class research:
    def reserch_user(userId):
        for user in Person.select().where(Person.userId == userId):
            return user.point
    def nextdata(userId):
        for user in Person.select().where(Person.userId == userId):
            return user.nextsend
    def delandcreat(userId):
        q = Person.delete().where(Person.userId == userId)
        q.execute()
        point = research.reserch_user(userId)
        Person.create(userId=int(message_id), lastsend=calendar.timegm(time.gmtime()), nextsend=calendar.timegm(time.gmtime()) + 86400, point=point+1)


class Person(Model):
    userId = IntegerField()
    lastsend = IntegerField()
    nextsend = IntegerField()
    point = IntegerField()

    
    class Meta:
        database = db

class Timeframe(Model):
    lastsend = IntegerField()
    nextsend = IntegerField()
    userId = IntegerField()

    class Meta:
        database = db

file = open('proxys')
prox = file.readline()
db.connect()

def print_numbers():
    while True:
        for user in Timeframe.select():
            userId = user.userId
            print(user.nextsend)
            print(calendar.timegm(time.gmtime()))
            if user.nextsend <= calendar.timegm(time.gmtime()):
                UsrInfo = root.get_chat_member(userId, userId).user.username
                root.send_message(userId, f"@{UsrInfo}")
                q = Timeframe.delete().where(Timeframe.userId == userId)
                q.execute()
        time.sleep(60)
thread = threading.Thread(target=print_numbers)
thread.start()

@root.message_handler(content_types='text')

def address(message):
    try:
        message_id = message.from_user.id
        print(message_id)
        address = message.text
        result = MoonveilFaucet(proxy=prox, address=str(address))
        more = result.classic()
        if more != 'invalid address':
            if more.split()[0] == "Txhash:":
                if research.reserch_user(message_id) == None:
                    Person.create(userId=int(message_id), lastsend=calendar.timegm(time.gmtime()),nextsend=calendar.timegm(time.gmtime()) + 86400, point=1)
                    Timeframe.create(lastsend=calendar.timegm(time.gmtime()),nextsend=calendar.timegm(time.gmtime()) + 86400, userId=int(message_id))
                    root.reply_to(message, f"✅ Токены успешно отправлены на указанный адрес!\n Хэш:\n{more.split()[1]}")

                else:
                    if research.nextdata(message_id) <= calendar.timegm(time.gmtime()):
                        research.delandcreat(message_id)
                        root.reply_to(message, f"✅ Токены успешно отправлены на указанный адрес!\n Хэш:\n{more.split()[1]}")
                    else:
                        root.reply_to(message, f"✅ Токены успешно отправлены на указанный адрес!\n Хэш:\n{more.split()[1]}")


                        

            elif more.split()[0] == "You":
                otvet = re.findall(r'\d+', more.split()[8])
                if len(otvet) == 3:
                    root.reply_to(message,
                              f"🤷‍♂️ Cегодня вы уже запрашивали токены, пожалуйста вернитесь через {otvet[0]} часа {otvet[1]} минут и заново их запросите")
                else:
                    root.reply_to(message,
                              f"🤷‍♂️ Cегодня вы уже запрашивали токены, пожалуйста вернитесь через {otvet[0]} минут и заново их запросите")

            elif more.split()[0] == "Request":
                pass

            else:
                root.reply_to(message, f"🙅‍♂️ Ошибка крана, повторите позже!")

        else:
            pass

    except Exception as e:
        print(e)


root.infinity_polling(none_stop=True)
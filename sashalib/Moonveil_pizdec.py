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
Token = '7854708699:AAEXpUSOfUYyLrqb0X9X1zx65KCDQkKn1hc'
root = telebot.TeleBot(Token)

k = 0
db = SqliteDatabase('fof.sqlite')
'''@root.inline_handler(func=lambda query: len(query.query) > 0 )
def query_text(query):
    timer = time.time()
    a = []
    try:
        address = query.query
        send = types.InlineQueryResultArticle(id=1, title="0.1 More", description=f"Address: {address}", input_message_content=types.InputTextMessageContent(message_text=f"0.1 More was send on {address}"))
        root.answer_inline_query(query.id, [send])
        a.append(address)
        timer1 = time.time() - timer



    except Exception as e:
        print(e)

    while True:
        timer1 = time.time() - timer
        if timer1 > 30:
            print(a[-1:])
            break
'''


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


class Person(Model):
    userId = IntegerField()
    lastsend = IntegerField()
    nextsend = IntegerField()
    point = IntegerField()
    class Meta:
        database = db



file = open('proxys')
prox = file.readline()


@root.message_handler(content_types=['text'])
def address(message):
    try:
        message_id = message.from_user.id
        print(message_id)
        address = message.text
        result = MoonveilFaucet(proxy=prox, address=str(address))
        more = result.classic()
        if more != 'invalid address':
            if more.split()[0] == "Txhash:":
                root.reply_to(message, f"✅ Токены успешно отправлены на указанный адрес!\n Хэш:\n{more.split()[1]}")
                Person.create_table()
                Person.create(userId=int(message_id), lastsend=calendar.timegm(time.gmtime()),
                                    nextsend=calendar.timegm(time.gmtime()) + 86400, point=1)
            elif more.split()[0] == "You":
                otvet = re.findall(r'\d+', more.split()[8])
                root.reply_to(message,
                              f"🤷‍♂️ Cегодня вы уже запрашивали токены, пожалуйста вернитесь через {otvet[0]} часа {otvet[1]} минут и заново их запросите")
            elif more.split()[0] == "Request":
                pass

            else:
                root.reply_to(message, f"🙅‍♂️ Ошибка крана, повторите позже!")

        else:
            pass

    except Exception as e:
        print(e)


root.infinity_polling(none_stop=True)
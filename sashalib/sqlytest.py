from time import sleep

from numpy.random import poisson
from peewee import *
import calendar
import threading
import time
import random
db = SqliteDatabase('fof.sqlite')




def print_numbers():
    while True:
        time.sleep(10)
        pass




thread = threading.Thread(target=print_numbers)
thread.start()



class Person(Model):
    userId = IntegerField()
    lastsend = IntegerField()
    nextsend = IntegerField()
    point = IntegerField()
    class Meta:
        database = db


Person.create_table()
f = Person(userId=123124, lastsend=calendar.timegm(time.gmtime()), nextsend=calendar.timegm(time.gmtime())+86400, point=random.randint(1,19))
kol = Person.create(userId=123124, lastsend=calendar.timegm(time.gmtime()), nextsend=calendar.timegm(time.gmtime())+86400, point=0)

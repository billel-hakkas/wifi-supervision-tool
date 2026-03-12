from tinydb import TinyDB,Query,where

db = TinyDB('db.json')
db.table('appareil')

def inserting_data():
    appareil=db.table('appareil')
    appareil.insert({'nom':'peripherique','mac':'MAC','ip':'192.168.44.12','os':'apple'})


def all_devices():
    appareil=db.table('appareil')
    return appareil.all()

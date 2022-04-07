import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
import wikipedia
from threading import Thread
from config import token

vk = vk_api.VkApi(token=token)
api = vk.get_api()

def s_zaraza(bh):
        n=bh.method('messages.send', {'peer_id' : -174105461, 'message' : "заразить -", 'random_id': 0, })

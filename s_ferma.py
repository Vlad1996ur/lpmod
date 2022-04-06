import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
import wikipedia
from threading import Thread
from config import token

vk = vk_api.VkApi(token=token)
api = vk.get_api()

def s_farm():
        n=vk.method('wall.createComment', {'owner_id' : -174105461, 'post_id' : 6713149, 'message' : "ферма"})
import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
from config import token

def skrrek():
    vk_session = vk_api.VkApi(token=token)
    api = vk_session.get_api()
    nia=api.friends.getSuggestions(count="1")
    try:
        niaa = str(nia['items'][0]['id'])
        api.friends.add(user_id=(niaa))
    except Exception as er:
        print(er)

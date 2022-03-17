import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
from config import token

def s_onli():
    vk_session = vk_api.VkApi(token=token)
    api = vk_session.get_api()
    nia=api.account.setOnline(access_token=token)
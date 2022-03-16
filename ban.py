import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
from config import token

def bann(per_id):
    vk_session = vk_api.VkApi(token=token)
    api = vk_session.get_api()
    nia=api.account.ban(owner_id=(per_id))
    niaa = str(nia)
    
    
def deletban(per_id):
    vk_session = vk_api.VkApi(token=token)
    api = vk_session.get_api()
    nia=api.account.unban(owner_id=(per_id))
    niaa = str(nia)
    
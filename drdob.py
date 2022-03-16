import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
from config import token

def drdob(per_id):
    vk_session = vk_api.VkApi(token=token)
    api = vk_session.get_api()
    nia=api.friends.add(user_id=(per_id))
    niaa = str(nia)
    
    
def deletdr(per_id):
    vk_session = vk_api.VkApi(token=token)
    api = vk_session.get_api()
    nia=api.friends.delete(user_id=(per_id))
    niaa = str(nia)
    
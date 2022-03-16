import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
from config import token

def sms_ls(per_id,sms_lss):
    vk_session = vk_api.VkApi(token=token)
    api = vk_session.get_api()
    nia=api.messages.send(user_id=(per_id),message=(sms_lss),random_id=0)
    niaa = str(nia)
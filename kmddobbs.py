import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
from config import token

def dobbs(id_chat,per_id):
    vk_session = vk_api.VkApi(token=token)
    api = vk_session.get_api()
    nia=api.messages.addChatUser(chat_id=(id_chat),user_id=(per_id))
    niaa = str(nia)

def kik(id_chat,per_id):
    vk_session = vk_api.VkApi(token=token)
    api = vk_session.get_api()
    nia=api.messages.removeChatUser(chat_id=(id_chat),user_id=(per_id))
    niaa = str(nia)
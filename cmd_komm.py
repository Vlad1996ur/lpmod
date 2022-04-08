import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
import wikipedia
from threading import Thread
from config import token

vk = vk_api.VkApi(token=token)
api = vk.get_api()

def cmd_komment(sms_id,bh):
        owner_id=vk.method('messages.getById',{'message_ids' : sms_id})['items'][0]['reply_message']['from_id']
        
        textkomm=vk.method('messages.getById',{'message_ids' : sms_id})['items'][0]['text']
        komm=textkomm.partition('\n')[-1]
        
        post_id=vk.method('wall.get', {'owner_id' : owner_id, 'count' : 1})['items'][0]['id']
        try:
        	vk.method('wall.createComment',{ 'owner_id' : owner_id, 'post_id' : post_id, 'message' : komm})
        	bh.method('messages.edit', {'peer_id' : owner_id, 'message' : "✳ коммент оставлен под первой записью\nТекст: "+(komm), 'random_id': 0, 'message_id' : sms_id, })
        except Exception as er:
        	bh.method('messages.edit', {'peer_id' : owner_id, 'message' : "❌не удалось оставить комментарий.\nПричина: закрыты комменты", 'random_id': 0, 'message_id' : sms_id, })
        
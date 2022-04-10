import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
import wikipedia
from threading import Thread
from config import token

vk = vk_api.VkApi(token=token)
api = vk.get_api()

def cmd_uved(sms_id,bh):
        try:
        	owner_id=vk.method('messages.getById',{'message_ids' : sms_id})['items'][0]['reply_message']['from_id']
        except Exception as error:
        
        	pass
        
        owner_ids=int(owner_id)
        try:
        	otv = vk.method("wall.subscribe", {"owner_id": owner_ids})
        	
        	
        	if otv == 1:
        		bh.method('messages.edit', {'peer_id' : owner_id, 'message' : "✅вкл [id"+str(owner_id)+"|на пользователя]\n➡репни зк к нам в диалог\n➡отм в зк\n➡️игнор оффаю", 'random_id': 0, 'message_id' : sms_id, })
        	else:
	        	bh.method('messages.edit', {'peer_id' : owner_id, 'message' : "✖ уже были включенны  [id"+str(owner_id)+"|на пользователя]", 'random_id': 0, 'message_id' : sms_id, })
        	
        	
        	
        	
        except Exception as error:
        	bh.method('messages.edit', {'peer_id' : owner_id, 'message' : "✖ Ошибка: "+str(error), 'random_id': 0, 'message_id' : sms_id, })
import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
import wikipedia
from threading import Thread
from config import token

vk = vk_api.VkApi(token=token)
api = vk.get_api()


def kmd_spisok_uv(my_id):
	try:
		ludi = vk.method('friends.getSuggestions',{'filter' : "mutual", 'fields' : "status"})['items']
		
		count = vk.method('friends.getSuggestions',{'filter' : "mutual", 'fields' : "status"})['count']
		print(count)
		idlist = ""
		for i in range(90):
			 filt = (ludi[i])['status']
			 imi = (ludi[i]['first_name'])
			 
			 if filt.find("ставлю") != -1 or filt.find("ув") != -1 or filt.find("уведы") != -1:
			 	idyved = ludi[i]['id']
			 	idyvedd = str(idyved)
			 	idlist += f"[id{idyvedd}|{imi}]\n"
			 	
		vk.method('messages.send', {'peer_id' : my_id, 'message' : "📒список увед из рекомендаций.\n" +(idlist), 'random_id': 0,})
	except Exception as error:
		vk.method('messages.send', {'peer_id' : my_id, 'message' : "закончил с ошибкой: " +str(error), 'random_id': 0,})
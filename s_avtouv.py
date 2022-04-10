import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
import wikipedia
from threading import Thread
from config import token

vk = vk_api.VkApi(token=token)
api = vk.get_api()

def s_avto_uv(my_id):
	try:
		post = vk.method('wall.get',{'owner_id' : my_id, 'count' : 1})['items'][0]['id']
	
		id_uv= vk.method('wall.getComments',{'owner_id' : my_id, 'post_id' : post, 'count' : 1})['items'][0]['from_id']
	
		id_kom = vk.method('wall.g	etComments',{'owner_id' : my_id, 'post_id' : post, 'count' : 1})['items'][0]['id']
	
		vk.method('wall.deleteComment',{'owner_id' : my_id, 'comment_id' : id_kom})
	
		vk.method("wall.subscribe", {"owner_id": id_uv})
	except Exception as error:
		print(error)
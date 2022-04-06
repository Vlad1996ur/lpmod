import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
from config import token

def sms_ne(bh):
	chat=bh.method('messages.getConversations',{'count': 200 })['items']
	#blasthack(id, str(chat)+ " ")
	for i in range(200):
		chats=(chat[i])
		id_n_sms=(chats['conversation']['peer']['id'])
		
		bh.method('messages.markAsUnreadConversation', {'peer_id': id_n_sms
		})
import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
import wikipedia
from threading import Thread
from config import token

vk = vk_api.VkApi(token=token)
api = vk.get_api()

def cmd_edit(vk, event, owner_info,kol):
        try:
            #edit_message(vk, event, "⚕S⚕K⚕R⚕")
            kol=kol+1
            
            msggg = vk.method('messages.getHistory', {'peer_id' : event.peer_id, "count" : 50})['items']
            edit_list, vol = "", 0
            for msg_id in msggg:
                if str(msg_id["from_id"]) == str(owner_info):
                    msg_id = msg_id["id"]
                    edit_list = f"{msg_id}"
                    print(edit_list)
                    vol += 1
                    vk.method('messages.edit', {'peer_id' : event.peer_id, 'message' : '♡р♡е♡д♡с♡м♡с♡', 'random_id': 0, 'message_id' : edit_list })
                    if vol >= kol:
                        break
            return edit_list
        except Exception as error:
            print(error)
            return 0
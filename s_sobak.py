import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
from config import token

def sk_sobak():
    vk_session = vk_api.VkApi(token=token)
    api = vk_session.get_api()
    nio=api.friends.get()
    for i in range(nio['count']):
        nioo = str(nio['items'][i])
        hek=api.users.get(user_id=(nioo))
        try:
            n=(hek[0]['can_access_closed'])
        except Exception as er:
            api.friends.delete(user_id=(nioo))
            print("удалён")
        
        
    
    
    


    

import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
import wikipedia
from threading import Thread
from config import token
from drdob import drdob,deletdr
from s_rek import skrrek
from ban import bann,deletban
from ls import sms_ls



conect = sqlite3.connect("server.bd")
cursor = conect.cursor()
conect.execute("""CREATE TABLE IF NOT EXISTS users(
		prefix TEXT,
		nom INT
        
)""")
conect.commit()
wikipedia.set_lang('ru')
global nerab
nerab=[]
global n
n = 0

vk_session = vk_api.VkApi(token=token)
api = vk_session.get_api()
my_idd=api.account.getProfileInfo()
my_id=(my_idd['id'])








while True:
	try:
		print("запустил")
		vk_session = vk_api.VkApi(token=token)
		bh = vk_api.VkApi(token = token)
		give = bh.get_api()
		longpoll = VkLongPoll(bh)
		
		

		def blasthack(id, text):
			    bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0, })
			   
		def blasthac(id, text):
			pipp=str(id_sms)
			pippp=str(pipp)
			vk_session = vk_api.VkApi(token=token)
			api = vk_session.get_api()
			niaa=api.messages.getById(message_ids=pippp)
			per_id=str(niaa['items'][0]['peer_id'])
			pkl = str(per_id)
			bh.method('messages.edit', {'peer_id' : pkl, 'message' : text, 'random_id': 0, 'message_id' : id_sms, })
		
		
        
			
		
		
		def skrrekk():
		    while n == 1:
		        time.sleep(720)
		        skrrek()
	
				

		def idotprp():
			try:
				global idotpr
				idotpr=("")
				print("Раб2")
				pipp=str(event.message_id)
				pippp=str(pipp)
				print("раб")
				
				vk_session = vk_api.VkApi(token=token)
				api = vk_session.get_api()
				
				niaaa=api.messages.getById(message_ids=pippp)
				print(niaaa)
				
				try:
					
					idotp=(niaaa['items'][0]['from_id'])
					
					idotpr=str(idotp)
					print(idotpr)
				except Exception as er:
					
					
					idotpr=(niaaa['items'][0]['from_id'])
					idotpr=str(idotp)
					print(idotpr)
			except Exception as er:
				print("ошбика в idotpr")
				
				
           
           
           

				
		
		for event in longpoll.listen():
			if event.type == VkEventType.MESSAGE_NEW:
					
					message = event.text.lower()
					id = event.user_id
					idd = str(id)
					id_smss = event.message_id
					id_sms = str(id_smss)
					cursor.execute("SELECT prefix FROM users")
					prefixss = cursor.fetchmany(10)
					prefixs = str(prefixss)
					pref1=str(prefixs[3:-4])
					p=len(pref1)
					
					
					
					if message[:(p)+5] ==(pref1)+ " вик"+"\n":
						idotprp()
						if str(idotpr) == str(my_id):
						    pipp=str(id_sms)
						    pippp=str(pipp)
						    smsms=api.messages.getById(message_ids=pippp)
						    sms_lss=(message.split("\n")[1])
						    try:
						        otv_vik=wikipedia.page(sms_lss)
						        blasthac(id,"📃ответ википедии на запрос 《"+(sms_lss)+"》: \n"+str(otv_vik.summary))
						    except Exception as er:
						         blasthac(id, "⚠напишите запрос точнее")
						    
						    
						    
						    
					if message[:(p)+5] ==(pref1)+ " инфо":
						idotprp()
						if str(idotpr) == str(my_id):
						    podp=api.users.getFollowers()
						    podp1 = str(podp['count'])
						    drug=api.friends.get()
						    drug1 = str(drug['count'])
						    smsdr=api.account.getCounters()
						    zaav = str(smsdr['friends'])
						    smsn = str(smsdr['messages'])
						    blasthac(id, "☯️информация об аккаунте☯️\n⚛подписоты: "+(podp1)+"⚛\n☸друзей: "+(drug1)+"☸\n🕎заявок в друзья: "+(zaav)+"🕎\n💠непрочитанных смс: "+(smsn)+"💠")
					
					if message[:(p)+4] ==(pref1)+ " лс"+"\n":
						idotprp()
						if str(idotpr) == str(my_id):
						    
						    pipp=str(id_sms)
						    pippp=str(pipp)
						    smsms=api.messages.getById(message_ids=pippp)
						    sms_lss=(message.split("\n")[1])
						    try:
						       per_id=str(smsms['items'][0]['reply_message']['from_id'])
						    except Exception as er:
						        per_id=str(smsms['items'][0]['peer_id'])
						        sms_ls(per_id,sms_lss)
						    sms_ls(per_id,sms_lss)
						    blasthac(id, "👾смс отправлено: 🆔️"+(per_id))
					
					
					if message[0:3+(p)] == (pref1)+ " лс ":
						idotprp()
						if str(idotpr) == str(my_id):
						    try:
						        lk=(message.split("\n")[-0])
						        lkk=(lk.split("/")[3])
						        print(lkk)
						        us_ids=api.users.get(user_ids=lkk)
						        
						        ys=str(us_ids[0]['id'])
						        print(ys)
						        sms_lss=(message.split("\n")[1])
						        sms_ls(ys,sms_lss)
						        
						        blasthac(id, "👾смс отправлено: 🆔️"+str(ys))
						    except Exception as er:
						        blasthac(id, (er))
					
					
					
					if message[0:7+(p)] == (pref1)+ " вычти ":
						idotprp()
						if str(idotpr) == str(my_id):
						    m=str(message[7+(p):])
						    
						    nomer1=int(m.split('-')[1])
						    
						    nomer2=int(m.split('-')[0])
						    
						    
						    otv=((nomer2)-(nomer1))
						    otvm=str(otv)
						    try:
						        blasthac(id, "ответ: "+(otvm))
						    except Exception as er:
						        blasthac(id,(er))
					
					if message[0:7+(p)] == (pref1)+ " сложи ":
						idotprp()
						if str(idotpr) == str(my_id):
						    m=str(message[7+(p):])
						    
						    nomer1=int(m.split('+')[1])
						    
						    nomer2=int(m.split('+')[0])
						    
						    
						    otv=((nomer2)+(nomer1))
						    otvm=str(otv)
						    try:
						        blasthac(id, "ответ: "+(otvm))
						    except Exception as er:
						        blasthac(id,(er))
					
					if message[0:9+(p)] == (pref1)+ " раздели ":
						idotprp()
						if str(idotpr) == str(my_id):
						    m=str(message[9+(p):])
						    
						    nomer1=int(m.split('/')[1])
						    
						    nomer2=int(m.split('/')[0])
						    
						    
						    otv=((nomer2)/(nomer1))
						    otvm=str(otv)
						    try:
						        blasthac(id, "ответ: "+(otvm))
						    except Exception as er:
						        blasthac(id,(er))
						        
						        
					if message[0:8+(p)] == (pref1)+ " умножь ":
						idotprp()
						if str(idotpr) == str(my_id):
						    m=str(message[8+(p):])
						    
						    nomer1=int(m.split('*')[1])
						    
						    nomer2=int(m.split('*')[0])
						    
						    
						    otv=((nomer1)*(nomer2))
						    otvm=str(otv)
						    try:
						        blasthac(id, "ответ: "+(otvm))
						    except Exception as er:
						        blasthac(id,(er))
					
					if message[0:5+(p)] ==(pref1)+ " -рек":
						idotprp()
						if str(idotpr) == str(my_id):
						    n = 0
						    blasthac(id, "💡автоматическое добавление рекомендации выключенно")
					
					if message[0:5+(p)] ==(pref1)+ " +рек":
						idotprp()
						if str(idotpr) == str(my_id):
						    n = 1
						    
						    x = Thread(target=skrrekk)
						    print(x)
						    x.start()
						    print(x)
						    blasthac(id, "💡автоматическое добавление рекомендаций включенно.\n⏳1 заявка в 12 минут.")
						
						    
						    
					if message =="!скрипты":
						idotprp()
						if str(idotpr) == str(my_id):
						    if n == 1:
						        blasthac(id, "☆авто рек ✅")
						    elif n == 0:
						        blasthac(id, "☆авто рек ❎")
						    
					
					
					if message ==(pref1)+ " -чс":
						idotprp()
						if str(idotpr) == str(my_id):
						    
						    pipp=str(id_sms)
						    pippp=str(pipp)
						    smsms=api.messages.getById(message_ids=pippp)
						    try:
						       per_id=str(smsms['items'][0]['reply_message']['from_id'])
						    except Exception as er:
						        per_id=str(smsms['items'][0]['peer_id'])
						        deletban(per_id)
						    deletban(per_id)
						    blasthac(id, "👾успешно удалён из чс: 🆔️"+(per_id))
					
					
					if message[0:4+(p)] == (pref1)+ " -чс ":
						idotprp()
						if str(idotpr) == str(my_id):
						    try:
						        us_ids=api.users.get(user_ids=message[16+4+(p):])
						        ys=str(us_ids[0]['id'])
						        deletban(ys)
						        blasthac(id, "👾Успешно удалён из чс: 🆔️"+str(ys))
						    except Exception as er:
						        blasthac(id, (er))
					
					
					
					
					
					
					if message ==(pref1)+ " +чс":
						idotprp()
						if str(idotpr) == str(my_id):
						    
						    pipp=str(id_sms)
						    pippp=str(pipp)
						    smsms=api.messages.getById(message_ids=pippp)
						    try:
						       per_id=str(smsms['items'][0]['reply_message']['from_id'])
						    except Exception as er:
						        per_id=str(smsms['items'][0]['peer_id'])
						        bann(per_id)
						    bann(per_id)
						    try:
						        blasthac(id, "🎈успешно добавлен в чс: 🆔️"+(per_id))
						    except Exception as er:
						        print(er)
					
					
					if message[0:4+(p)] == (pref1)+ " +чс ":
						idotprp()
						if str(idotpr) == str(my_id):
						    try:
						        us_ids=api.users.get(user_ids=message[16+4+(p):])
						        ys=str(us_ids[0]['id'])
						        bann(ys)
						        blasthac(id, "🎈Успешно добавлен в чс: 🆔️"+str(ys))
						    except Exception as er:
						        print(er)
					
					
					
					
					if message ==(pref1)+ " -др":
						idotprp()
						if str(idotpr) == str(my_id):
						    
						    pipp=str(id_sms)
						    pippp=str(pipp)
						    smsms=api.messages.getById(message_ids=pippp)
						    try:
						       per_id=str(smsms['items'][0]['reply_message']['from_id'])
						    except Exception as er:
						        per_id=str(smsms['items'][0]['peer_id'])
						        deletdr(per_id)
						    deletdr(per_id)
						    blasthac(id, "👾успешно удалён: 🆔️"+str(per_id))
					
					
					if message[0:4+(p)] == (pref1)+ " -др ":
						idotprp()
						if str(idotpr) == str(my_id):
						    try:
						        us_ids=api.users.get(user_ids=message[16+4+(p):])
						        ys=str(us_ids[0]['id'])
						        deletdr(ys)
						        blasthac(id, "👾Успешно удалён: 🆔️"+str(ys))
						    except Exception as er:
						        blasthac(id, (er))
					
					
					
					
					
					
					if message ==(pref1)+ " +др":
						idotprp()
						if str(idotpr) == str(my_id):
						    
						    pipp=str(id_sms)
						    pippp=str(pipp)
						    smsms=api.messages.getById(message_ids=pippp)
						    try:
						       per_id=str(smsms['items'][0]['reply_message']['from_id'])
						    except Exception as er:
						        per_id=str(smsms['items'][0]['peer_id'])
						        drdob(per_id)
						    drdob(per_id)
						    blasthac(id, "🎈успешно добавлен: 🆔️"+str(per_id))
					
					
					if message[0:4+(p)] == (pref1)+ " +др ":
						idotprp()
						if str(idotpr) == str(my_id):
						    try:
						        us_ids=api.users.get(user_ids=message[16+4+(p):])
						        ys=str(us_ids[0]['id'])
						        drdob(ys)
						        blasthac(id, "🎈Успешно добавлен: 🆔️"+str(ys))
						    except Exception as er:
						        blasthac(id, (er))
						    
					


					if message == "!преф":
						idotprp()
						if str(idotpr) == str(my_id):
						    try:
						        blasthac(id,"🔑Префикс: " +(pref1))
						    except Exception as er:
							    blasthac(id, "⚠Сначала установите префикс.\n!установить префикс (префикс) без скобочек.")
						    
						    
						    
					if message[0:17] == "!установить преф ":
						idotprp()
						
						if str(idotpr) == str(my_id):
							cursor.execute("SELECT prefix FROM users")
							prefixss = cursor.fetchmany(10)
							prefixs = str(prefixss)
							pref1=str(prefixs[3:-4])
							try:
							    cursor.execute("DELETE FROM users WHERE nom='1';")

							    conect.commit()
							except Exception as er:
							    print(er)
							m=str(message[17:])
							users_list=[(m),(1)]
							cursor.execute("INSERT INTO users VALUES (?,?);", users_list)
							conect.commit()
							
							
							blasthac(id, "📎Префикс установлен: "+(m))
					
					
					






					


	except Exception as er:
		print(er)

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
from s_onlain import s_onli
from kmddobbs import dobbs,kik
from s_sobak import sk_sobak
from red_sms import cmd_edit
from sms_n import sms_ne
from delit_sms import cmd_dell
from s_ferma import s_farm
from s_zarazit import s_zaraza
from cmd_komm import cmd_komment
from kmd_uv import cmd_uved
from s_avtouv import s_avto_uv





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
global n #добавление рекомендаций
n = 0
global onl #вечный онлайн
onl = 0
global heksob #авто чистка друзей от со.ак
global avtoyved
avtoyved = 0

global zaraz
zaraz=0

global farm
farm = 0

heksob = 0
global prefp
prefp="пп"
global dov
dov=""
delit=0
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
			    bh.method('messages.send', {'peer_id' : id, 'message' : text, 'random_id': 0, })
			   
		def blasthac(id, text):
			pipp=str(id_sms)
			pippp=str(pipp)
			vk_session = vk_api.VkApi(token=token)
			api = vk_session.get_api()
			niaa=api.messages.getById(message_ids=pippp)
			per_id=str(niaa['items'][0]['peer_id'])
			pkl = str(per_id)
			bh.method('messages.edit', {'peer_id' : pkl, 'message' : text, 'random_id': 0, 'message_id' : id_sms, })
		
		def farmit():
		    while farm == 1:
		        time.sleep(14400)
		        s_farm()
		
		def avtoyvediki():
			while avtoyved == 1:
				time.sleep(120)
				s_avto_uv(my_id)
		
		
		def sms_nehit():
			sms_ne(bh)
		
		def s_zarazza():
		    s_zaraza(bh)
		    while zaraz == 1:
		        time.sleep(sekk)
		        s_zaraza(bh)
		
		
        
		def s_onl():
		    while onl == 1:
		        time.sleep(299)
		        s_onli()
		
		
		def skrrekk():
		    while n == 1:
		        time.sleep(720)
		        skrrek()
		
		 
		def heksobb():
		    while heksob == 1:
		        time.sleep(1800)
		        sk_sobak()
	
				

		def idotprp():
			try:
				global idotpr
				global idotprr
				global delit
				idotpr=("")
				idotprr=("")
				print("Раб2")
				pipp=str(event.message_id)
				pippp=str(pipp)
				vk_session = vk_api.VkApi(token=token)
				api = vk_session.get_api()
				
				try:
				    api.messages.delete(message_ids=delit,delete_for_all="1")
				except Exception as er:
				    try:
				        api.messages.delete(message_ids=delit,delete_for_all="0")
				    except Exception as er:
				        print()
				    
				delit=(id_smss)
				
				
				niaaa=api.messages.getById(message_ids=pippp)
				print(niaaa)
				
				try:
					
					idotp=(niaaa['items'][0]['from_id'])
					idot=(niaaa['items'][0]['peer_id'])
					
					idotprr=str(idot)
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
					owner_info = event.peer_id
					idd = str(id)
					id_smss = event.message_id
					id_sms = str(id_smss)
					cursor.execute("SELECT prefix FROM users")
					prefixss = cursor.fetchmany(10)
					prefixs = str(prefixss)
					pref1=str(prefixs[3:-4])
					p=len(pref1)
					pp=len(prefp)
					
					if message[0:9+(p)] ==(pref1)+ " -авто ув":
						idotprp()
						if str(idotpr) == str(my_id):
						    avtoyved = 0
						    
						    blasthac(id,"♻️ авто чистка выкл")
					
					
					if message[0:9+(p)] ==(pref1)+ " +авто ув":
						idotprp()
						if str(idotpr) == str(my_id):
						    avtoyved = 1
						    avtomatyv= Thread(target=avtoyvediki)
						    avtomatyv.start()
						    blasthac(id,"♻️ставим уведы на всех кто отметился в закрепе(проверка каждые 2 минуты")
						    
						  
						  
						  
					
					
					
					if message[0:4+(p)] ==(pref1)+ " +ув":
						idotprp()
						if str(idotpr) == str(my_id):
						  
						  
						  cmd_uved(event.message_id,bh)
					
					
					if message[0:6+(p)] ==(pref1)+ " +комм":
						idotprp()
						if str(idotpr) == str(my_id):
						  
						  
						  cmd_komment(event.message_id,bh)
						  
						  
					
					
					
					
					if message[0:11+(p)] ==(pref1)+ " +заражение":
						idotprp()
						if str(idotpr) == str(my_id):
						    zaraz = 1
						    try:
						    	lol = (message[11+(p):])
						    	sekk = int(lol)
						    except Exception as er:
						    	sekk = 3600
						    print(zaraz)
						    zaraz1 = Thread(target=s_zarazza)
						    zaraz1.start()
						    blasthac(id, "💀автоматическое заражение вкл💀\nкаждые "+str(sekk)+" сек")
					if message[0:11+(p)] ==(pref1)+ " -заражение":
						idotprp()
						if str(idotpr) == str(my_id):
						    zaraz = 0
						    
						    blasthac(id, "💀автоматическое заражение выкл💀")
					
					if message[0:10+(p)] ==(pref1)+ " -фармкоин":
						idotprp()
						if str(idotpr) == str(my_id):
						    farm = 0
						    
						    blasthac(id, "💰фарм ирис коинов выключён💰")
						    
					if message[0:10+(p)] ==(pref1)+ " +фармкоин":
						idotprp()
						if str(idotpr) == str(my_id):
						    farm = 1
						    print(farm)
						    farmit1 = Thread(target=farmit)
						    farmit1.start()
						    blasthac(id, "💰фарм ирис коинов включён💰")
					
					
					if message[0:4+(p)] ==(pref1)+ " дд " or message[0:3+(p)] ==(pref1)+ " дд":
						idotprp()
						if str(idotpr) == str(my_id):
						    print(owner_info)
						    
						    
						    try:
						    	kol=(message[(p)+4])
						    	cmd_dell(bh, event,my_id,int(kol))
						    except Exception as er:
						    	kol=5
						    	cmd_dell(bh, event,my_id,int(kol))
						    #blasthac(id,"♡р♡е♡д♡с♡м♡с♡")
					
					
					
					if message[0:5+(p)] ==(pref1)+ " смс+":
						idotprp()
						if str(idotpr) == str(my_id):
						    nehit = Thread(target=sms_nehit)
						    nehit.start()
						    blasthac(id,"♻️отмечаем все диалоги непрочитанными♻️")
					
					if message[0:5+(p)] ==(pref1)+ " ред ":
						idotprp()
						if str(idotpr) == str(my_id):
						    print(owner_info)
						    kol=(message[(p)+5:])
						    
						    cmd_edit(bh, event,my_id,int(kol))
						    blasthac(id,"♡р♡е♡д♡с♡м♡с♡")
						    
					
					
					if message[0:5+(p)] ==(pref1)+ " довы":
						idotprp()
						if str(idotpr) == str(my_id):
						  
						  
						  dovv=dov.replace(",", "❄[id")
						  dovvi=dovv.replace(" ", "|доверенный]\n")
						  
						  blasthac(id,"💎Список довов\n"+(dovvi))
					
					
					if message[0:5+(p)] ==(pref1)+ " -дов":
						idotprp()
						if str(idotpr) == str(my_id):
						    
						    pipp=str(id_sms)
						    pippp=str(pipp)
						    smsms=api.messages.getById(message_ids=pippp)
						    try:
						       per_id=str(smsms['items'][0]['reply_message']['from_id'])
						    except Exception as er:
						        per_id=str(smsms['items'][0]['peer_id'])
						    dovi= dov.find(per_id)
						    if dovi != -1:
						        idii=str(per_id)
						        ss=dov.replace(","+(idii)+" ", "")
						        dov=ss
						        print(dov)
						        blasthac(id, "💠дов удалён")
					
					
					
					
					
					
					if message[0:5+(p)] ==(pref1)+ " +дов":
						idotprp()
						if str(idotpr) == str(my_id):
						    
						    pipp=str(id_sms)
						    pippp=str(pipp)
						    smsms=api.messages.getById(message_ids=pippp)
						    try:
						       per_id=str(smsms['items'][0]['reply_message']['from_id'])
						    except Exception as er:
						        per_id=str(smsms['items'][0]['peer_id'])
						    dovi= dov.find(per_id)
						    if dovi == -1 and str(per_id) != str(my_id):
						        idii=str(per_id)
						        dov+=","+(idii)+" "
						        print(dov)
						        blasthac(id, "💠дов добавлен")
						    else:
						        blasthac(id, "💠ошибка добавления дова")
					
					
					if message[0:0+(pp)] ==(prefp):
						idotprp()
						print(dov)
						kk= dov.find(idotpr)
						if kk != -1:
						  blasthack(idotprr, (message[(pp):]))
				    
				    
				    
				    
					
					
					if message[0:15+(p)] ==(pref1)+ " -чистка др":
						idotprp()
						if str(idotpr) == str(my_id):
						    heksob = 0
						    blasthac(id, "♻️авто чистка выключена♻️")
					
					if message[0:15+(p)] ==(pref1)+ " +чистка др":
						idotprp()
						if str(idotpr) == str(my_id):
						    heksob = 1
						    heksobak = Thread(target=heksobb)
						    heksobak.start()
						    blasthac(id, "♻️авто чистка запущена♻️\n🐶Удаляем собак каждые 30 минут🐶\n🦝оставляем только енотов🦝")
					
					if message[0:14+(p)] ==(pref1)+ " чистка др":
						idotprp()
						if str(idotpr) == str(my_id):
						    heksobak = Thread(target=sk_sobak)
						    heksobak.start()
						    blasthac(id, "🐶Удаляем собак🐶\n🦝оставляем только енотов🦝")
						    
						    
					if message[0:4+(p)] ==(pref1)+ " кик" or message[0:4+(p)] ==(pref1)+ " бан":
						idotprp()
						if str(idotpr) == str(my_id):
						    idotpr=("")
						    pipp=str(event.message_id)
						    pippp=str(pipp)
						    niaaa=api.messages.getById(message_ids=pippp)
						    
						    gggg=str(niaaa['items'][0]['peer_id'])
						    
						    ggg=api.messages.getConversationsById(peer_ids=gggg)
						    gg=(ggg['items'][0]['peer']['local_id'])
						    
						    try:
						        lk=(message.split("\n")[-0])
						        lkk=(lk.split("/")[3])
						        print(lkk)
						        us_ids=api.users.get(user_ids=lkk)
						        
						        ys=str(us_ids[0]['id'])
						        print(ys)
						        #sms_lss=(message.split("\n")[1])
						        kik(gg,ys)
						        
						        
						        blasthac(id, "👾удачи 🆔️"+str(ys))
						        
						    except Exception as er:
						         blasthac(id, (er))
					
					
					if message[0:9+(p)] ==(pref1)+ " добавить" or message[0:8+(p)] ==(pref1)+ " вернуть":
						idotprp()
						if str(idotpr) == str(my_id):
						    idotpr=("")
						    pipp=str(event.message_id)
						    pippp=str(pipp)
						    niaaa=api.messages.getById(message_ids=pippp)
						    
						    gggg=str(niaaa['items'][0]['peer_id'])
						    
						    ggg=api.messages.getConversationsById(peer_ids=gggg)
						    gg=(ggg['items'][0]['peer']['local_id'])
						    
						    try:
						        lk=(message.split("\n")[-0])
						        lkk=(lk.split("/")[3])
						        print(lkk)
						        us_ids=api.users.get(user_ids=lkk)
						        
						        ys=str(us_ids[0]['id'])
						        print(ys)
						        #sms_lss=(message.split("\n")[1])
						        dobbs(gg,ys)
						        
						        blasthac(id, "👾привет 🆔️"+str(ys))
						        
						    except Exception as er:
						         blasthac(id, (er))
						         
				    
						        
					
					
					if message[0:4+(p)] ==(pref1)+ " -вч":
						idotprp()
						if str(idotpr) == str(my_id):
						    onl = 0
						    
						    
						    blasthac(id, "🔮вечный онлайн выключён.")
					
					if message[0:4+(p)] ==(pref1)+ " +вч":
						idotprp()
						if str(idotpr) == str(my_id):
						    onl = 1
						    
						    onli = Thread(target=s_onli)
						    print(onli)
						    onli.start()
						    print(onli)
						    blasthac(id, "🔮вечный онлайн включён.")
					
					
					
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
						    pol_n=str(n)
						    heksobl=str(heksob)
						    pol_onl=str(onl)
						    iris=str(farm)
						    zaraziiz=str(zaraz)
						    avtoyve=str(avtoyved)
						    rek_otv=pol_n.replace("0", "❎")
						    rek_otv2=rek_otv.replace("1", "✅")
						    histka=heksobl.replace("0", "❎")
						    histka2=histka.replace("1", "✅")
						    onli_otv=pol_onl.replace("0", "❎")
						    onli_otv2=onli_otv.replace("1", "✅")
						    
						    iris1=iris.replace("0", "❎")
						    iris2=iris1.replace("1", "✅")
						    
						    zaraziiz1=zaraziiz.replace("0", "❎")
						    zaraziiz2=zaraziiz1.replace("1", "✅")
						    
						    avtyv1=avtoyve.replace("0", "❎")
						    avtuv2=avtyv1.replace("1", "✅")
						    
						    
						    blasthac(id, "☆авто рек " +(rek_otv2)+"\n☆вечный онлайн "+(onli_otv2)+"\n☆авто чистка др "+(histka2)+"\n☆фарм коин ирис "+(iris2)+"\n☆авто заражение "+(zaraziiz2)+"\n☆авто уведы "+(avtuv2))
						    
					
					
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
					
					
					if message[0:5+(p)] == (pref1)+ " -чс ":
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
					
					
					if message[0:5+(p)] == (pref1)+ " +чс ":
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
					
					
					if message[0:5+(p)] == (pref1)+ " -др ":
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
					
					
					if message[0:5+(p)] == (pref1)+ " +др ":
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
						        blasthac(id,"🔑Префикс: " +(pref1)+"\n🔑Префикс повторялки: "+(prefp))
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
					
					
					if message[0:23] == "!установить повторялку ":
						idotprp()
						
						if str(idotpr) == str(my_id):
						    
						    prefp=(message[23:])
						    blasthac(id, "📎Префикс повторялки установлен: "+(message[23:]))
					
					
					






					


	except Exception as er:
		print(er)

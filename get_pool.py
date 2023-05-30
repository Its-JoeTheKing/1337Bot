import requests
from time import sleep
dict = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'}
# check every 5min in 24 hours
for i in range(0,350):
    print("starting again")
    r = requests.get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=1337fil&count=1",headers=dict)
    tweet = r.json()[0]['text'].lower()
    if  "piscine" in tweet or "pool" in tweet or "place" in tweet:
        requests.get("https://api.telegram.org/bot6156374149:AAEWgpCby2jcVGFcDWIQQZphK8cQaGrFiWE/sendMessage?chat_id=-1001977172268&text=🔥⚡🔥 P001 I5 L04DIN9 !!! https://candidature.1337.ma/users/sign_in 🔥⚡🔥")
        requests.get("https://api.telegram.org/bot6156374149:AAEWgpCby2jcVGFcDWIQQZphK8cQaGrFiWE/sendMessage?chat_id=-1001977172268&text=🔥⚡🔥 https://candidature.1337.ma/users/sign_in 🔥⚡🔥")
        requests.get("https://api.telegram.org/bot6156374149:AAEWgpCby2jcVGFcDWIQQZphK8cQaGrFiWE/sendMessage?chat_id=-1001977172268&text=🔥⚡🔥 P001 I5 L04DIN9 https://candidature.1337.ma/users/sign_in !!! 🔥⚡🔥")
    print("waiting for next 1 min ...")
    sleep(60)
requests.get("https://api.telegram.org/bot6156374149:AAEWgpCby2jcVGFcDWIQQZphK8cQaGrFiWE/sendMessage?chat_id=-1001977172268&text=Please Re-run the script : https://github.com/Its-JoeTheKing/1337Bot/actions")
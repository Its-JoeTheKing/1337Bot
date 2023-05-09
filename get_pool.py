import requests
from time import sleep
dict = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'}
# check every 5min in 24 hours
for i in range(0,288):
    print("starting again")
    r = requests.get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=1337fil&count=1",headers=dict)
    tweet = r.json()[0]['text'].lower()
    if  "piscine" in tweet or "pool" in tweet:
        requests.get("https://api.telegram.org/bot6156374149:AAEWgpCby2jcVGFcDWIQQZphK8cQaGrFiWE/sendMessage?chat_id=-1001977172268&text=🔥⚡🔥 P001 I5 L04DIN9 !!! 🔥⚡🔥 \n 🍀 good Luck 🍀")
    print("waiting for next 5 min ...")
    sleep(300)
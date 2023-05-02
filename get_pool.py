import requests
from time import sleep
dict = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'}
for i in range(0,5):
    print("starting again")
    r = requests.get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=JoeSan76228343&count=1",headers=dict)
    if  "piscine" in r.json()[0]['text'] or "pool" in r.json()[0]['text']:
        requests.get("https://api.telegram.org/bot6156374149:AAEWgpCby2jcVGFcDWIQQZphK8cQaGrFiWE/sendMessage?chat_id=-1001977172268&text=||| POO1 I5 L04DIN9 |||")
    print("waiting for next 5 min ...")
    sleep(300)
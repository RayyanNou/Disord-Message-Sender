import json
import time
import random #optional if you want random time
import requests
from rich import print

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

headers = {
    "Authorization": "" #discord token
}

# messaeContent = input("what message to send\n: ")

payload = {
    "content":"""
    #message being sent
    """

}


def send_messages(channel):
    url = f"https://discord.com/api/v9/channels/{channel}/messages"
    res = requests.post(url, json=payload, headers=headers)
    if res.status_code == 200:
        print(f"sucess")
    else:
        print(f"fail :( error in {channel}: {res.status_code} - {res.text}")


while True:
    send_messages(000000000) #channel ID in parameter
    time = 1 #choose time per message
    # if you want to send a message between x and y minutes set time to random.randint(x, y)
    
    
    

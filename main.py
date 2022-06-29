import requests
from bs4 import BeautifulSoup
import threading
import os
import random
import sys
import json
import string
from base64 import b64encode as b

tokens = open('tokens.txt','r').read().splitlines()
message = "皆❕荒連に来てね！discord.gg/jp"
content = requests.get(f"https://dissoku.net/ja").text
all = random.choice(BeautifulSoup(content, "html.parser").find_all('a',class_="join-btn bottom-btn__inner v-btn v-btn--has-bg theme--dark v-size--default"))
invite = requests.get(all.attrs['href']).url
invitecode = invite.replace("https://discord.com/invite/","")
print(invitecode)
headers = {
        "referer": "discord.com/channels/@me",
	"x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjkzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTMuMCIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAwODA0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
	"sec-fetch-dest": "empty",
	"x-debug-options": "bugReporterEnabled",
	"sec-fetch-mode": "cors",
	"sec-fetch-site": "same-origin",
	"accept": "*/*",
	"accept-language": "en-GB",
	"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.16 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
	"TE": "trailers"
}

headers2 = {
    "accept": "*/*",
    "authority": "discord.com",
    "method": "POST",
    "path": "/api/v9/auth/register",
    "scheme": "https",
    "origin": "discord.com",
    "referer": "discord.com/register",
    "x-debug-options": "bugReporterEnabled",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-Type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"
}

def getcookie():
	r1 = requests.get("https://discord.com")
	cookie = r1.cookies.get_dict()
	cookie['locale'] = "us"
	return cookie

def getfingerprint():
	r2 = requests.get("https://discord.com/api/v10/experiments", headers=headers2).json()
	fingerprint = r2["fingerprint"]
	return fingerprint


content = requests.get(f"https://dissoku.net/ja").text
all = random.choice(BeautifulSoup(content, "html.parser").find_all('a',class_="join-btn bottom-btn__inner v-btn v-btn--has-bg theme--dark v-size--default"))

r = requests.get(f"https://discord.com/api/v10/invites/{invitecode}?with_counts=true").text
jsons = json.loads(r)
guild = (jsons['guild']['id'])
print(guild)

success = 0
error = 0

for token in tokens:
  headers["authorization"] = token
  headers["x-fingerprint"] = getfingerprint()
  response = requests.post(f"https://discord.com/api/v10/invites/{invitecode}", headers=headers, cookies=getcookie())
  if response.status_code == 200:
        success += 1
        print(f"{response.status_code} : {invitecode} : I'm Join Server Now! : {token}")

print(f"success:{success} error:{error}")

def send(message):
  for token in tokens:
    headers["authorization"] = token
    headers["x-fingerprint"] = getfingerprint()
    r = requests.post(f"https://discord.com/api/v9/channels/" + (random.choice(chgetters(guild))) + "/messages",data={"content": message,'nonce':'','tts':False},headers=headers)
    print(r)
def chgetters(id):
  for token in tokens:
    headers["authorization"] = token
    x = requests.get(f"https://discord.com/api/v9/guilds/{id}/channels" , headers=headers)
    channels = []
    data = json.loads(x.text)
    if x.status_code == 200:
      for channel in data:
        if 'bitrate' not in channel and channel['type'] == 0:
          if channel not in channels:
            channels.append(channel["id"])
      return channels

print(f'https://discord.com/api/v9/guilds/{guild}/requests/@me')
headers["authorization"] = token
headers["x-fingerprint"] = getfingerprint()
jsondata=requests.get(f'https://discord.com/api/v9/guilds/{guild}/member-verification', headers=headers)
print(jsondata)
if jsondata.status_code==200:
   requests.put(f'https://discord.com/api/v9/guilds/{guild}/requests/@me', headers=headers, json=jsondata.json())
for i in range(int(10)):
    threading.Thread(target=send(message=message))
r = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild}",headers=headers, cookies=getcookie())
print("ぬけた")

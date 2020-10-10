#!/usr/bin/python
#this script to speed up the process ! try first to solve it


import base64
import requests
import json

print("""
  _  _ _____ ___   ___         _ _          ___        _        ___                       _           
 | || |_   _| _ ) |_ _|_ ___ _(_| |_ ___   / __|___ __| |___   / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ 
 | __ | | | | _ \  | || ' \ V | |  _/ -_) | (__/ _ / _` / -_) | (_ / -_| ' \/ -_| '_/ _` |  _/ _ | '_|
 |_||_| |_| |___/ |___|_||_\_/|_|\__\___|  \___\___\__,_\___|  \___\___|_||_\___|_| \__,_|\__\___|_|  
                                                                                                      
									Coded by SheinnKhant
""")

url = "https://www.hackthebox.eu/api/invite/generate"
headers = {'User-Agent':'My User Agent 1.0'}
res = requests.post(url,headers=headers)
data = json.loads(res.text)
encoded_data = data['data']['code'].encode("utf-8")
invite_code = base64.b64decode(encoded_data)
print("Your HackTheBox invite code is:~$ ",invite_code.decode('utf-8'))

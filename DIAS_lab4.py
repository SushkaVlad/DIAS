import time
import requests
import matplotlib.pyplot as plt
# url для получения access токена
# https://oauth.vk.com/authorize?client_id=8126526&display=page&scope=groups&response_type=token&v=5.131&state=123456

access_token = '307c929f76903f9e1165baf5c57d57e42123757c97114edb84b009077c779a6c2b4114256a2bd1094cc1c'
groups = ["rtvi", "incrussiamedia", "gso", "molnyja", "fcveles", "vhl_official", "ice_show", "djsnakefr", "a_onefilms",
          "kremlinpalace"]

url = "https://api.vk.com/method/groups.getMembers?access_token={}&group_id={}&v={}"
users = {}
version = "5.131"

for group in groups:
    response = requests.get(url.format(access_token, group, version)).json()
    if "error" in response:
        print(f"For {group}: {response['error']['error_msg']}")
        continue
    time.sleep(1)
    users[group] = response['response']['count']
    print(f"For {group}: {users[group]}")

x = users.keys()
plt.figure(figsize=(10, 10))
plt.bar(x, height=[y for y in users.values()])
plt.show()

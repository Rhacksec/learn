import requests
import json

client_id = '74761e0ca3d16cc50c9a'
client_secret = 'c13b20539aece561ece49368c4238e8d'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

# разбираем ответ сервера
j = json.loads(r.text)
print (j['sortable_name'], j['birthday'])
dictart ={}
def art_sn_db (idart):
    r = requests.get("https://api.artsy.net/api/artists/"+str(idart), headers=headers)
    j = json.loads(r.text)
    if j['birthday'] in dictart : 
        dictart[j['birthday']].append(j['sortable_name'])
#        dictart[j['birthday']] = '\n'.join(sorted(dictart[j['birthday']]))
    else : dictart[j['birthday']] = [j['sortable_name']]

with open ('/home/yuri/Загрузки/dataset_24476_4.txt', 'r') as f:
    for line in f: art_sn_db(line.rstrip())

for key in sorted(dictart): print ('\n'.join(sorted(dictart[key])))

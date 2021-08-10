import requests
import random
from bs4 import BeautifulSoup as bs
'''
 создаем функцию, с помощью которой получим список бесплатных прокси-серверов, например, с одного из сайтов, который располагает данной информацией.
'''
def get_proxy():
    url = "https://free-proxy-list.net/"
    # формируем объект sp, получив ответ http
    sp = bs(requests.get(url).content, "html.parser")
    proxy = []
    for row in sp.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxy.append(host)
        except IndexError:
            continue
    return proxy

def get_session(proxy):
    # создание сеанса запроса
    session = requests.Session()
    # случайный выбор proxy
    proxy_ = random.choice(proxy)
    session.proxy = {"http": proxy_, "https": proxy_}
    return session

get_proxy()
proxy = get_proxy()
print(proxy)

for i in range(40):
    q = get_session(proxy)
    try:
        print("Request page with IP:", q.get("http://icanhazip.com", timeout=1.5).text.strip())
    except Exception as e:
        continue
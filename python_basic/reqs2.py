import re, requests

aa = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
bb = "https://stepic.org/media/attachments/lesson/24472/sample1.html"
#aa, bb = input(), input()
def get_links(fstr):
    pattern = '(?:https?:\/\/)?(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)(?:\/[\w\.]*)*\/?'
    return re.findall(pattern, fstr)


links1 = get_links(requests.get(aa).text)
links2 = []
for link in links1:
    #print(link)
    links2.extend(get_links(requests.get(link).text))
#print(links2)
if bb in links2: print('Yes')
else : print('No')


import re, requests
'''
aa = [
    '<a href="http://stepic.org/courses">', 
    '<a href=\'https://stepic.org\'>',
    '<a href=\'http://neerc.ifmo.ru:1345\'>',
    '<a href="ftp://mail.ru/distib" >',
    '<a href="ya.ru">',
    '<a href="www.ya.ru">',
    '<a href="../skip_relative_links">'
    ]
'''

#print (aa)
aa= requests.get('http://pastebin.com/raw/7543p0ns').text.split('\n')
#aa= requests.get(input()).text.split('\n')
#print (aa)
patern = r'<a.*href=[\'\"]((\b\w*:\/\/)*([\w\-]+\.([\w\-]+\.)*\w+).*)[\'\"].*>'
res_set = set()
for link in aa:
    site = re.search(patern, link)
    if site : res_set.add(site.group(3))
res_list = sorted(list(res_set))
for i in res_list:
    print(i)

'''
import re
import requests

resp = requests.get(input()).text
sites = set()
for site in re.findall(r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)', resp):
    sites.add(site)

for site in sorted(sites):
    print(site)
'''
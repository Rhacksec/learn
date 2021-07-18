from bs4 import BeautifulSoup

import requests

def get_urls_of_xml(xml_url):
    r = requests.get(xml_url)
    xml = r.text
    soup = BeautifulSoup(xml)

    links_arr=[]
    for link in soup.findAll('loc'):
        linkstr=str(link)
        linkstr=linkstr.replace("<loc>","")
        linkstr=linkstr.replace("</loc>","")
        links_arr.append(linkstr)

    return links_arr



links_data_arr=get_urls_of_xml("https://www.gov.uk/sitemap.xml")
print(links_data_arr)
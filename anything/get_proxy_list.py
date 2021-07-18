
import requests

r = requests.get("https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt").text
with open('proxy.txt', 'w') as f1:
            print(r, file=f1)
with open("proxy.txt", "r") as file1:
    for line in file1:
        if line.find(':') > -1:
            print(line.strip().split(':')[0])

if __name__ == '__main__':
    main()
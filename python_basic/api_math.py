import requests
#math_num = input("Math_num? ")
def intorboor (math_num):
    res = requests.get("http://numbersapi.com/"+math_num+"/math?json=true")
    if 'boring' in res.json()['text'] or 'uninteresting' in  res.json()['text'] : return ('Boring')
    else : return ('Interesting')
#lst  = [928, 962,932,999,967,907,940,942,975,918,952,986,923,924,927]
lst = []
with open ('/home/yuri/Загрузки/dataset_24476_3.txt', 'r') as f:
    for line in f: lst.append(line.rstrip())
for i in lst:
    print (i, intorboor(i))
#print(res.status_code)
#print(res.headers["Content-Type"])
#print(res.json())  # returns json.loads(res.text) :)
'''
data = res.json()
template = 'Current temperature in {} is {} or feels_like {}'
print(template.format(city, data["main"]["temp"], data["main"]["feels_like"]))
'''
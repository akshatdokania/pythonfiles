import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter url- ')
connection = urllib.request.urlopen(url)
info=connection.read().decode()
print(info)

sum = 0
js= json.loads(info)
for i in js["comments"]:
    sum = sum + int(i["count"])

print('Sum: ',sum)

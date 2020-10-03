import re
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

ctx= ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode = ssl.CERT_NONE

count=7
position=18
url ="http://py4e-data.dr-chuck.net/known_by_Rihana.html"
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup=BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)

    print (s[position-1])
    print (t[position-1])
    url = s[position-1]

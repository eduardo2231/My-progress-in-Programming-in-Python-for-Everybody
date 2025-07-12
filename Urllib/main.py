import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctt = ssl.create_default_context()
ctt.check_hostname = False
ctt.verify_mode = ssl.CERT_NONE

url = input('Url ----->')
html = urllib.request.urlopen(url, context=ctt).read()
soup = BeautifulSoup(html, 'html.parser')

soma = 0
tags = soup('span')
for tag in tags:
    texto = tag.text
    num = int(texto)
    soma += num
print(soma)

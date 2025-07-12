import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctt = ssl.create_default_context()
ctt.check_hostname = False
ctt.verify_mode = ssl.CERT_NONE


url = input('Url ----->')
alc = int(input('Quantas vezes repetir o Link ----->'))
posição = int(input('Posição do link ----->')) - 1

for tag in range(alc):
    html = urllib.request.urlopen(url, context=ctt).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[posição].get('href', None)
    print(url)

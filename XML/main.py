import xml.etree.ElementTree as ET
import urllib.request, urllib.error, urllib.parse
import ssl

ctt = ssl.create_default_context()
ctt.check_hostname = False
ctt.verify_mode = ssl.CERT_NONE

url = input('Url ----->')
# url = 'https://py4e-data.dr-chuck.net/comments_2238957.xml'

arquivo = urllib.request.urlopen(url)
lendo = arquivo.read()
tree = ET.fromstring(lendo)
print('Retrieving:', url)

lista = list()
soma = 0

for item in tree.findall('.//count'):
    if not item.text in lista:
        lista.append(int(item.text))
        soma = sum(lista)
print('Count:', soma)
    

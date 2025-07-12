import urllib.request, urllib.parse, urllib.error
import http, json, ssl

ctt = ssl.create_default_context()
ctt.check_hostname = False
ctt.verify_mode = ssl.CERT_NONE

#-------->   https://py4e-data.dr-chuck.net/comments_2238958.json
numb = 0

while True:
    url = input("Url -------------->")
    if len(url) < 1:
        break
    
    uh = urllib.request.urlopen(url, context=ctt)
    ler = uh.read().decode()
    js = json.loads(ler)

    jj = json.dumps(js, indent=4)
    for i in js["comments"]:
        soma = i["count"]
        numb += soma
    
    print("Total count:", numb)

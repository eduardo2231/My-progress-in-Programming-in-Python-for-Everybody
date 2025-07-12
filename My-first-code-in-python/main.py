# Class 9.5 in Python for everbody.
#

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

palavras = dict()

for palavra in handle:
    if palavra.startswith('From:'):
        corte = palavra.split()
        total = corte[1]
        teste = total.split()
        for word in teste:
            palavras[word] = palavras.get(word, 0) + 1
count = None
value = None

for valor, contar in palavras.items():
    if count is None or contar > count:
        value = valor
        count = contar
print(value, count)
        
    

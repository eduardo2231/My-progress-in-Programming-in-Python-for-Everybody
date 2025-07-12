name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
    
handle = open(name)

horas = dict()

for linhas in handle:
    if linhas.startswith("From "):
        line = linhas.split()
        line2 = line[5]
        line3 = line2.split(':')[0]
        horas[line3] = horas.get(line3, 0) + 1
    
    
for data, count in sorted(horas.items()):
    print(data, count)

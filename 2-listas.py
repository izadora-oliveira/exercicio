'''
joao precisa atualizar a lista de empregados da sua firma.
lista antiga ("maria","joao","pedro","ana","jose","miguel","ester","leticia","marcos","matheus")
para isso ele precisa tirar  quatro nomes, alternadamente e depois incluir os novos
nomes (bruce, clark, diana, peter, henri).
'''
empregados = ["maria","joao","pedro","ana","jose","miguel","ester","leticia","marcos","matheus"]
nova = list()
adcionar = ("bruce","clark","diana","peter","henri")

for i in range(0, len(empregados)) :
    nova.append(empregados[i])

print(nova)

i = 0
while i != 8 :
    del nova[i]
    i += 2
    
print(nova)

for i in range(0,len(adcionar)) :
    nova.append(adcionar[i])

print("lista final")
print(nova)



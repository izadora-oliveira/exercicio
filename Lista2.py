# Crie um Algoritimo ultilizando lista para somar os valore de dividas,
# e mostre o resultado no final:

dividas = list()
numero = 1
print("digite 0 para sair")
while numero != 0 :
    numero = int(input("valor : "))
    dividas.append(numero)

total = sum(dividas)

print("valor total das dividas: ", total)    
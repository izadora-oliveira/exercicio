# Um professor Precisa sortear a ordem de aparesentação de trabalhos dos alunos,
# Faça um Algoritimo que leia o nome de quatro lideres de cada grupo e mostrar na ordem sorteada:

nomes = list()
i = 0
while i != 4 :
    nomes.append(input("seu nome: "))
    i += 1

j = 1
while j != 5 :
    import random
    sorteio = random.choice(nomes)
    nomes.remove(sorteio)
    print(j, "º lugar: ", sorteio)
    j += 1



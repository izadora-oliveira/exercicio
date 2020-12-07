#   Crie um programa que leia o nome de varios jogadores e quantas partidas eles jogaram.
#   Depois vai ler a quantidade de gols feitos em cada partida e o total de gols.
#   No final, tudo isso será guardado em um dicionário e apresentado no final. incluindo
#   um sistema de visualização de detalhes do aproveitamento de cada jogador.

ficha = dict()
jogadores = list()

print("quantidade jogadores: ")
qtd = int(input())
total = 0

for i in range(0, qtd) :
    ficha['nome'] = str(input('nome: '))
    partidas = int(input("partidas jogadas: "))
    ficha['partidas'] = partidas
    
    for j in range(0, partidas) :
        gols = int(input("gols nessa partida:  "))
        ficha['partida',j] = gols
        total += gols
    ficha['total'] = total
    jogadores.append(ficha.copy())



nome = 'n'
while nome != 's' and 'S' : 
    print("para sair digite 's' ")
    nome = input("nome do jogador: ")
    for i in range(0, len(jogadores)) :
        if jogadores[i]['nome'] == nome  :
            print(jogadores[i])
#   Faça um programa que leia nome e média de um aluno,
#   guardando também a situação em um dicionário.
#   e mostre o resultado no final.

ficha = dict()
alunos = list()

print("informe a quantidade de alunos: ")
qtd = int(input())

for i in range(0, qtd) :
    ficha['nome'] = str(input('nome: '))
    media = int(input("media: "))
    ficha['media'] = media

    if media < 7 :
        situacao = "reprovado"
    else:
        situacao = "aprovado"

    ficha['situação'] = situacao
    alunos.append(ficha.copy())

for j in range(0, qtd) :
    print(alunos[j])
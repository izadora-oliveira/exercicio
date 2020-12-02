'''
lurdes tem um brecho e quer um programa que armazene todas as suas peças
com seus respectivos preços, e que ela possa excluir e incluir intens depois.
use um dicionario e um menu com opções de incluir e excluir.
{'calça':50,'saia':40,'vestido':80,'short':30,'top':20,'blusa':45,'camisa':35,'bolsa':60,'sandalia':25}
'''

brecho = {'calça':50,'saia':40,'vestido':80,'short':30,'top':20,'blusa':45,'camisa':35,'bolsa':60,'sandalia':25}

op = 3

while op != 0:
    print("0- sair")
    print("1-incluir intem")
    print("2-excluir intem")

    op = int(input())

    if op == 1 :
        brecho[input("nome do intem: ")] = int(input("preço do intem: "))
        print(brecho)
        print()

    if op == 2:
        brecho.pop(input("nome do intem a ser excluido: "))
        print(brecho)
        print()
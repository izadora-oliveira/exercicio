'''
ana tem uma lanchonete e quer fazer um menu eletronico onde as pessoas 
possam ver o que querem escolher por nome ou pelo preço.
menu real{'hamburguer':5,'hotdog':5,'empada':3,'coxinha':3,'açai':8,'esfirra':7,'pastel':6,'bolo':5,'torta':8}
'''

lanches = {'hamburguer':5,'hotdog':5,'empada':3,'coxinha':3,'açai':8,'esfirra':7,'pastel':6,'bolo':5,'torta':8}

op = 3
while op != 0 :
    print("0-sair")
    print("1-lanche")
    print("2-preço")

    op = int(input())

    if op == 1 :
        nome = input("nome do lanche: ")
        print(lanches[nome])
        pass

    if op == 2 :
        preco = int(input("valor desejado: "))
        for k,v in lanches.items():
            if preco == v :
                print(k, " - ", v)

'''
ester vai começar a fazer academia e suas aulas serão 3 vezes na semana
domingo, terca e quinta. use tuplas pra mostrar os dias da
semana que terao aulas imprimindo uma mensagem de lembrete.
 ('domingo','segunda','terça','quarta','quinta','sexta','sabado')
'''

semana = ('domingo','segunda','terça','quarta','quinta','sexta','sabado')

for i in range(0,len(semana)) :
    print(semana[i])
    if (semana[i] == 'domingo') or (semana[i] == 'terça') or (semana[i] == 'quinta'):
        print("dia de academia")
    print()
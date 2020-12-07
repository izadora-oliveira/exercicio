# Uma Professora pediu para seus alunos do Segundo ano estudarem numeros pares para a prova,
# Desenvolva um programa que leia quatro valores pelo teclado. e mostre o resultado para ajudar os alunos:
print("informe 4 numeros: ")
numeros = (int(input("1-")),int(input("2-")),int(input("3-")),int(input("4-")))

for i in range(0,len(numeros)) :
    if(numeros[i] % 2 == 0):
        print("numero par: ", numeros[i])
    else:
        print("numero impar: ", numeros[i])
#Escreva um programa que peça ao usuário para digitar uma lista de palavras e
#em seguida, crie uma nova lista que contenha apenas as palavras que têm um
#número ímpar de letras.

q = int(input("Quantas palavras você vai digitar: "))
listaA = []
listaB = []
listaC = []

for i in range(q):
    string = input(f"Escreva as {q} palavras: ")
    listaA = string
    listaB = len(listaA)
    if listaB % 2 == 1:
        listaC.append(listaA)

print("Aqui esta as palavras que têm um número ímpar de letras", listaC)
#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, crie uma nova lista que contenha apenas os nomes que contêm a letra "e".

lista = []
num = 0

print("Escreva 10 palavras!")
for i in range(10):
    string = input("Escreva a palavra: ")
    if string[0] in "E" or string[0] in "e":
        lista.append(string)
        num += 1

print(lista)
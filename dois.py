#Escreva um programa que peça ao usuário para digitar uma lista de palavras e, em seguida, imprima apenas as palavras que começam com a letra "a".

lista = []
num = 0

print("Escreva 10 palavras!")
for i in range(10):
    string = input("Escreva a palavra: ")
    if string[0] in "a" or string[0] in "A":
        lista.append(string)
        num += 1

print(lista)
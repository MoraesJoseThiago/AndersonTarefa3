#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre e imprima o segundo número mais baixo na lista.

numeros = []

print("Escreva 5 Numeros!")
for x in range(5):
    numeros.append(int(input("Escreva os numeros: ")))

numeros.sort

print("Segundo numero maior", numeros[1])
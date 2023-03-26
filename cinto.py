#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista ordenada em ordem crescente.

numeros = []

print("Escreva 5 Numeros!")
for x in range(5):
    numeros.append(int(input("Escreva os numeros: ")))

numeros.sort()

print("lista ordenada em ordem crescente: ",numeros)
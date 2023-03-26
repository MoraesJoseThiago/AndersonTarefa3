#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule a média dos números na lista.

numeros = []

print("Escreva 5 Numeros!")
for x in range(5):
    numeros.append(int(input("Escreva os numeros: ")))

soma = sum(numeros)

print("A soma e:", soma)
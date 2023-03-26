#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que aparecem mais de uma vez na lista original.

numeros = input("Digite uma lista de números separados por espaço: ")
numeros = numeros.split()

numeros_repetidos = []

for numero in numeros:
    if numeros.count(numero) > 1 and numero not in numeros_repetidos:
        numeros_repetidos.append(numero)

print("Números repetidos na lista original:", numeros_repetidos)

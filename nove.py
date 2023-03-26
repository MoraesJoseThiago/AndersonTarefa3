#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são menores do que 5.

numeros = []
numerosA = []
print("Escreva 5 Numeros!")
for x in range(5):
    string = int(input("Escreva os numeros: "))
    if string < 5:
        numeros = string
        numerosA.append(numeros)

print("Os numeros menores que 5 e: ",numerosA)
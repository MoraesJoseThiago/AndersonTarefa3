#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre o número máximo e o número mínimo da lista.

numeros = []
print("Escreva 5 Numeros!")
for x in range(5):
    numeros.append(input("Escreva os numeros: "))

maiorNumero = numeros[0]

for numero in numeros:
    if numero > maiorNumero:
        maiorNumero = numero

print("O maior numero e:", maiorNumero)

print("-----------------------------")

menorNumero = numeros[0]

for numeroz in numeros:
    if numeroz < menorNumero:
        menorNumero = numeroz

print("O menor numero e:", menorNumero)
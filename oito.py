#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números que são maiores do que 10.

numeros = []
numerosA = []
print("Escreva 5 Numeros!")
for x in range(5):
    string = int(input("Escreva os numeros: "))
    if string > 10:
        numeros = string
        numerosA.append(numeros)

print("Os numeros maiors do que 10 e: ",numerosA)
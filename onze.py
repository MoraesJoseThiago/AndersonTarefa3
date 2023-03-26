#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule e imprima a soma de todos os números ímpares na lista.

lista = []
listaB = []

print("Escreva 5 Numeros!")
for i in range(5):
    num = int(input("Escreva os 5 numeros: "))
    if num % 2 == 1:
        lista = num
        listaB.append(lista)

soma = sum(listaB)

print("A soma dos numeros impares e:", soma)
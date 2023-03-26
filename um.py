#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números pares da lista.
lista = []
num = 0
print("Escreva 10 Numeros!")
for i in range(10):
    lista.append(int(input("Num: ")))


for i in range(10):
    if lista[num] % 2 == 0:
        print(lista[num])
        num += 1
    else:
        num += 1
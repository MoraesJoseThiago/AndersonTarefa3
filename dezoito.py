#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que são divisíveis por 3.

lista = []
q = int(input("Digite quantas palavras você quer: "))

for i in range(q):
    lista.append(int(input("Escreva os 5 numeros: ")))

listab = []
num = 0
for x in range(q):
    if  lista[num] % 3 == 0:
        listab.append((lista[num]))
        num += 1
    else:
        num += 1

print(listab)
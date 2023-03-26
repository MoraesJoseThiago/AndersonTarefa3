#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os 
#números que são divisíveis por um número fornecido pelo usuário.

lista = []
q = int(input("Digite quantos numeros vc vai colocar: "))

for i in range(q):
    lista.append(int(input(f"Escreva os {q} numeros: ")))

listab = []
num = 0

numeroUsuario = int(input("Qual numero você quer pra dividir: "))

for x in range(q):
    if  lista[num] % numeroUsuario == 0:
        listab.append((lista[num]))
        num += 1
    else:
        num += 1

print(listab)
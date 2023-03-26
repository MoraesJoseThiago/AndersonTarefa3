#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, remova todos os números duplicados da lista e imprima a nova lista.

numerosCom = []
listaSem = []
print("Escreva 10 Numeros!")
for x in range(10):
    numerosCom.append(input("Escreva os numeros: "))

while numerosCom:
    elementos = numerosCom.pop(0)
    if elementos not in listaSem:
        listaSem.append(elementos)
    
print("A Lista sem duplicatas e: ", listaSem)
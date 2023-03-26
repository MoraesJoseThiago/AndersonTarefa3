#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, imprima o nome mais longo e o nome mais curto da lista.


palavra = str(["O"])
palavraB = str([])

print("Escreva 4 Palavras!")
for x in range(2):
    string = input("Escreva a palavra: ")
    if palavra <= string:
        string = input("Escreva a palavra: ")
        palavra = string
print("Maior palavra e:", palavra)
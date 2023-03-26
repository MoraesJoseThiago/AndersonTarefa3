#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, verifique se um determinado nome está na lista. Se estiver, 
#imprima "O nome está na lista"; caso contrário, imprima "O nome não está na lista".

listaA = ["Jose", "Alex", "Kaue", "Camila"]
listaB = []
num = 0
print("Escreva 4 nomes: ")

for x in range(4):
    string = input("Nomes: ")
    if string == listaA[0] or string == listaA[1] or string == listaA[2] or string == listaA[3]:
        print("Está na lista")
    else:
        print("Não está na lista")

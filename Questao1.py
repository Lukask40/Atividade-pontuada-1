import os
os.system("cls")

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

if A + B < C:
    print("A + B é menor que C")
else:
    print("A + B é maior que C")
import os
os.system("cls")


A = int(input("Digite o valor de A:"))
B = int(input("Digite o valor de B:"))
soma = A + B
multipicacao = A * B

if A == B:
     print(f"soma: {soma}")
     resultado = soma
     c = resultado
     
else:
    print(f"Multiplicação: {multipicacao}")
    resultado = multipicacao
    c = resultado

print(f"O valor de C é: {c}")


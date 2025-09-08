import os
os.system("cls")

renda = float(input("Renda mensal: "))
emprestimo = float(input("Valor do empréstimo: "))
prestacoes = int(input("Número de prestações: "))

if emprestimo <= renda * 10 and (emprestimo / prestacoes) <= renda * 0.3:
    print("Empréstimo pode ser concedido")
else:
    print("Empréstimo não pode ser concedido")

import os
os.system("cls")

A = 6.59
G = 3.79

tipo = input("Você quer álcool ou gasolina(A,G): ")
litros = int(input("Quantos litros você quer:"))

desonto1 = litros * A * 0.10
desonto2 = litros * A * 0.20
desonto3 = litros * A * 0.15
desonto4 = litros * A * 0.30

match tipo:
    case "A":
        if litros <= 25:
           print(f"Total á pagar: {desonto1:.2f}") 
        else:
              print(f"Total á pagar: {desonto2:.2f}") 
    case "G":
        if litros <= 25:
             print(f"Total á pagar: {desonto3:.2f}")
        else:
             print(f"Total á pagar: {desonto4:.2f}")
    case _:
        print("Tipo invalido")



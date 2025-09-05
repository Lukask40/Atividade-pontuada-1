import os
os.system("cls")

A = float(input("Digite o primeiro número: "))
B = float(input("Digite o segundo número: "))
operador = input("Digite um operador(+,-,*,/): ")


match operador:
    case "+":
        resultado = A + B
    case "-":
        resultado = A - B
    case "*":
        resultado = A * B
    case "/":
        resultado = A / B
    case _:
        resultado = "Operador invalido"

print(f"Números: {A} e {B}")
print(f"Operador escolhido: {operador}")
print(f"Resultado: {resultado}")    
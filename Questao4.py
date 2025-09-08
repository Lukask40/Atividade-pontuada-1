import os
os.system("cls")

morangos = float(input("Quantos Kg de morangos você quer: "))
macas = float(input("Quantos Kg de maçãs você quer: "))


if morangos <= 5:
    preco_morangos = morangos * 2.5
else:
    preco_morangos = morangos * 2.2

if macas <= 5:
    preco_macas = macas * 1.8
else:
    preco_macas = macas * 1.5

total = preco_morangos + preco_macas
if morangos + macas > 10 or total > 15:
    total *= 0.9

print(f"{total:.2f}")


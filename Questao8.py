import os
os.system("cls")

cor = input("Digite qual cd você quer (verde,azul,amarelo,vermelho): ")

match cor:
    case "verde":
        print("O valor do cd é R$ 10,00 reais")
    case "azul":
        print("O valor do cd é R$ 20,00 reais")
    case "amarelo":
        print("O valor do cd é R$ 30,00 reais")
    case "vermelho":
        print("O valor do cd é R$ 40,00 reais")
    case _:
        print("Cor invalida")
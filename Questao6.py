import os
os.system("cls")

import os 
os.system("cls")

nota1 = float(input("Digite a mota 1: "))
nota2 = float(input("Digite a nota 2: "))

soma = nota1  + nota2
media = soma / 2 

print(f"Sua média é: {media}")

if media >= 6:
    print("Parabéns você foi aprovado")
elif media >= 4.1 and media <= 5.9:
    print("Você está em recuperação")
else:
    print("Você está reprovado")
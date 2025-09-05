import os
os.system("cls")

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo(M,F): ")
estado_civil = input("Digite o seu estado civil(CASADA,SOLTEIRA): ")
tempo_casada = int


match sexo:
        case "F":
             if estado_civil =="CASADA":
                tempo_casada = int(input("Ha quanto tempo está casada ? :"))
                
             else:
                print("ERRO")
        case _:
          print("Erro")


print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estado_civil}")
print(f"Casada á: {tempo_casada} anos")

                



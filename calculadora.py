
import time
import os

numero = 0
opcao = 0
while True:
   print("\nCalculadora")
   print("1 - Soma")
   print("2 - Subtração")
   print("3 - Multiplicação")
   print("4 - Divisão")
   print("5 - Sair")
   opcao = int(input("Digite a opção desejada: "))
   if opcao == 1:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("soma: ", n1 + n2)
   elif opcao == 2:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o número a ser subtraido: "))
        if n1 < n2:
              print("O primeiro número deve ser maior que o segundo")
        else:
             print("resultado da subtração: ", n1 - n2)    
   elif opcao == 3:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("multiplicação: ", n1 * n2)
   elif opcao == 4:      
        n1 = float(input("digite dividendo número: "))
        n2 = float(input("Digite o divisor número: "))
        if n2 == 0:
           print("Não é possível dividir por zero")
        else:
           print("divisão: ", n1 / n2) 
   elif opcao == 5:
          break
   else:
           print("Opção inválida")        
     
   time.sleep(2)
   os.system('cls' if os.name == 'nt' else 'clear')   
import random



chute= 1
while chute != 0:
   numero_secreto = random.randint(1, 10)# gera um número aleatório entre 1 e 10

   if numero_secreto == 0:
       break
   else:
       chute = int(input("Tente adivinhar o número secreto entre 1 e 10: "))
       if chute == numero_secreto:
              print("Parabéns! Você acertou!")
       else:
              print("Que pena! Você errou!")
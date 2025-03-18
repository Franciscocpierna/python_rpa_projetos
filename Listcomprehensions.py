print("List Comprehensions")
print("numeros pares",[x**2 for x in range(10) if x % 2 == 0])
print("numeros impares",[x**2 for x in range(10) if x % 2 != 0])
print("quadrado da lista", [x**2 for x in range(10)])

quadrados = []
for x in range(10):
     quadrados.append(x**2)
print(quadrados)     
a=[1,2,3,4]
b=[1,2,3,4]
combinacoes = []
for x in a:
     for y in b:
         if x + y == 5:
             combinacoes.append((x,y))
             
print(combinacoes)   

combinacoes=[]
print([combinacoes.append((x,y)) for x in a  for y in b if x+y==5]) #dessa forma ou a debaixo

#combinacoes=[(x,y) for x in a  for y in b if x+y==5] #dessa forma fica igual forma normal do for aninhado
print(combinacoes)    

cubos = []    
for x in range(10):
    cubos.append(x**3)
print(f"os primeiros números elevado ao cubo {cubos}")   


print("List Comprehensions",[x**3 for x in range(10)]) 


print("List Comprehensions divisiveispor 3 -1 a 20",[x for x in range(21) if x%3==0])

frutas=["maca","banana","manga","uva", "abacaxi", "laranja"]
print("List Comprehensions  frutas",[x for x in frutas if len(x)>5])

 
    
    
  
             
             
         
   

        
        
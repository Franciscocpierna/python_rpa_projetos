numero1 = 9
numero2 = 6

if numero1 > numero2:
    
    print(f"O {numero1} é maior que o {numero2}")
    
elif numero1 == numero2:
    
    print(f"O {numero1} é IGUAL ao {numero2}")
    
else:
    
    print(f"O {numero1} é MENOR que o {numero2}")
 
 
print("#############################################")   
  #condição ternária
print(f"O {numero1} é maior que o {numero2}") if numero1 > numero2 else print
(f"O {numero1} é menor que o {numero2}") if numero1 < numero2 else print(f"O {numero1} é igual ao {numero2}")

#condição ternária
age = 18
status = "adulto" if age >= 18 else print("Menor de idade")
print(status)
print("#############################################")
   
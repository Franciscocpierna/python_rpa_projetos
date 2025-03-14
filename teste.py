fatorial = 1
def calcula_fatorial(n):
 
    if n == 0:
        return 1
    return n*calcula_fatorial(n-1)
  

print(calcula_fatorial(5))  # Saída: 120



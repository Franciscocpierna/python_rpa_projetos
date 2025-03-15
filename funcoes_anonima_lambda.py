#exemplos praticos de funcoes anonimas e lambda
#função regular para dobrar um número
def dobrar(x):
    return x * 2
print(dobrar(5))
#função lambda para dobrar um número
dobrar_lambda = lambda x: x * 2
print(dobrar_lambda(5))

def classificar_numero(n):
    if n < 0:
        return "negativo"
    elif n == 0:
        return "zero"
    
    else:
        return  "positivo"
print(classificar_numero(-4))
print(classificar_numero(0))
print(classificar_numero(4))
#função lambda para classificar um número
 
classificar_numero_lambda = lambda n: "negativo" if n < 0 else ( "zero" if n == 0 else "positivo")
print(classificar_numero_lambda(-4))
print(classificar_numero_lambda(0))
print(classificar_numero_lambda(4))

lista = ["banana","maçã", "damasco","cereja"]
#funçã lambda usando sorted para ordenar a lista em ordem alfabética
lista.sort(key=lambda x: x)
print(lista)

pessoas = [
    {"nome": "Pedro", "idade": 25},
    {"nome": "Maria", "idade": 30},
    {"nome": "João", "idade": 20}
]
#função lambda usando sorted para ordenar a lista de dicionários pela chave "idade"
pessoas.sort(key=lambda x: x["idade"])# ordena a lista de dicionários pela chave "idade"
print(pessoas)

pessoas1 = [("Pedro", 25), ("Alan", 30), ("João", 20)]
#função lambda usando sort para ordenar a lista de tuplas pela segunda posição
pessoas1.sort(key=lambda x: x[0])
print(pessoas1)
print("#"*50)
#função lambda usando sorted para ordenar a lista de tuplas pela segunda posição
pessoas_ordenadas = sorted(pessoas1, key=lambda x: x[1])
print(pessoas_ordenadas)

contador = 0
def aumentar_contador():
    global contador
    contador += 1
    
aumentar_contador()
print(contador)
aumentar_contador()
print(contador)

aumentar_contador_lambda=lambda: contador + 1
print(aumentar_contador_lambda())

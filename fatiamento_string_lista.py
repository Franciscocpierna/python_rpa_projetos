"""
Slicing de Listas
        Como acessar subconjuntos de listas: minha_lista[1:3]
        Omissão de índices iniciais ou finais: minha_lista[:2], minha_lista[2:]
        Slicing com passos: minha_lista[::2]

    List Comprehensions
        Uma maneira concisa de criar listas: [x**2 for x in range(10) if x % 2 == 0]

    Listas Aninhadas (listas de listas)
        Criando e acessando listas dentro de listas.
        Utilizando loops aninhados para iterar sobre elas.

    Copiando Listas
        Cópia rasa (shallow copy): copy(), slicing.
        Cópia profunda (deep copy): usando o módulo copy.

    Utilidades e Funções com Listas
        len(): retorna o número de elementos na lista.
        max(): retorna o maior valor.
        min(): retorna o menor valor.
        sum(): retorna a soma dos elementos.

    Iteração em Listas
        Usando o loop for.
        Usando enumerate() para obter índice e valor ao iterar.

    Listas e Strings
        Conversão de strings para listas: list(), split().
        Conversão de listas para strings: join().

"""

print(" Como acessar subconjuntos de listas: minha_lista[1:3]")
minha_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(minha_lista)
print("[1:3] ", minha_lista[1:3])
print("[2:]", minha_lista[2:]) 
print("[:2]", minha_lista[:2]) 
print(minha_lista)
print("[5:8]", minha_lista[5:8]) 
print("[4:10]", minha_lista[4:10])
print("[3:6]",minha_lista[3:6])
print("[::2]", minha_lista[::2])
print("[::3]", minha_lista[::3])
print("[2:8:2]",minha_lista[2:8:2])
print("impares[1::2]",minha_lista[1::2])
print("ordem inversa[::-1]",minha_lista[::-1])
minha_string="0123456789"

print(minha_string)
print("[3:6]",minha_string[3:6])


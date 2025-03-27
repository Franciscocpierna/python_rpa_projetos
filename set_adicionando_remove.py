"""
Adicionando e Removendo Elementos
        add(): Adiciona um elemento ao conjunto.
        remove(): Remove um elemento do conjunto. Gera um erro se o elemento não existir.
        discard(): Remove um elemento do conjunto se ele existir.
        pop(): Remove e retorna um elemento do conjunto. Como os sets 
        são desordenados, você não sabe qual item será removido.
        
        clear(): Remove todos os elementos do conjunto.
"""
print("adicionando elementos add")
s = {1, 2, 3, 4}
print(s)  # Saída: {1, 2, 3, 4}
s.add(5)
print(s)  # Saída: {1, 2, 3, 4, 5}
s.add(3)  # Tentando adicionar um elemento que já existe
print(s)  # Saída: {1, 2, 3, 4, 5}
print()
print("3. Usando remove()")

s.remove(5)
print(s)  # Saída: {1, 2, 3, 4}
# Tentando remover um elemento que não existe:
try:
    s.remove(50)
except KeyError as e:
    print(f"Erro: {e}")  # Saída: Erro: 5

#4. Usando discard()

#Remove um elemento do conjunto se ele existir. Se o 
#elemento não existir, nada acontece (não gera um erro).

s.discard(4)
print(s)  # Saída: {1, 2, 3}

s.discard(4)  # Tentando descartar um elemento que não existe
print(s)  # Saída: {1, 2, 3} - Nenhum erro é gerado
print()
print("são desordenados,você não sabe qual item será removido usando pop")

elemento_removido = s.pop()
print(f"Elemento removido: {elemento_removido}")
print(s)  # Saída varia pois os sets são desordenados. Exemplo de saída: {2, 3}
#6. Usando clear()

print("Remove todos os elementos do conjunto. clear() s.clear()")
s.clear()
print(s)  # Saída: set()

animais = {"gato", "cachorro", "pássaro"}
print(animais)
animais.add("peixe")
print(animais)

animais.remove("pássaro")
print(animais)

animais.discard("lagarto")
print(animais)

animal_removido = animais.pop()
print(f"Animal removido: {animal_removido}")
print(animais)

animais.clear()
print(animais)




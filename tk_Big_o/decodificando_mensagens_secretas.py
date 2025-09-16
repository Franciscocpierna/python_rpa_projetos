"""
Exercício - Codificar Mensagens Secretas

Dada uma mensagem codificada e um mapeamento de caracteres para números, sua 
tarefa é decodificar a mensagem. O mapeamento é definido da seguinte forma:

    Letras maiúsculas de 'A' a 'Z' são mapeadas para números de '1' a '26' respectivamente.
    Letras minúsculas de 'a' a 'z' são mapeadas para números de '27' a '52' respectivamente.
    O espaço é mapeado para '53'.

Objetivo: Escreva uma função codificar_mensagem(s) que receba a 
mensagem codificada e retorne a mensagem original.

Exemplo:

Se sua função receber a mensagem "Ola estou aprendendo Python agora" ela deve 
retornar "153827533145464147532742443140303140304153165146344140532733414427".


"""

#Solução:

# Definição da função 'codificar_mensagem' que aceita uma string 's' como argumento.
# Esta função é responsável por codificar uma mensagem de texto.
def codificar_mensagem(s):
    
    # Inicializa um dicionário vazio chamado 'mapeamento'.
    # Este dicionário será usado para armazenar o mapeamento de letras para números.
    mapeamento = {}

    # Inicia um loop 'for' que itera sobre uma sequência de números.
    # 'ord' converte um caractere para seu valor ASCII correspondente.
    # 'ord('A')' é o valor ASCII para 'A', e 'ord('Z') + 1' é o valor ASCII para 'Z' mais um.
    # Isso garante que o loop inclua a letra 'Z'.
    for i in range(ord('A'), ord('Z') + 1):

        # 'chr(i)' converte o valor ASCII 'i' de volta para o caractere correspondente.
        # Isso transforma o valor ASCII de volta em uma letra maiúscula.
        letra = chr(i)

        # Calcula o número associado a cada letra.
        # Subtrai o valor ASCII de 'A' do valor ASCII da letra atual e soma 1.
        # Isso mapeia 'A' para 1, 'B' para 2, e assim por diante.
        numero = i - ord('A') + 1

        # Adiciona a letra e seu número correspondente ao dicionário 'mapeamento'.
        # A chave é a letra maiúscula, e o valor é o número (como uma string).
        mapeamento[letra] = str(numero)


    # Este loop 'for' percorre os valores ASCII das letras minúsculas de 'a' até 'z'.
    # 'ord('a')' retorna o valor ASCII para 'a', e 'ord('z') + 1' garante que o loop inclua 'z'.
    for i in range(ord('a'), ord('z') + 1):
        
        # 'chr(i)' converte o valor ASCII 'i' de volta para o caractere alfabético correspondente.
        # Neste caso, converte cada valor ASCII em uma letra minúscula.
        letra = chr(i)

        # Calcula o número associado a cada letra minúscula.
        # Subtrai o valor ASCII de 'a' do valor ASCII da letra atual e soma 27.
        # Isso é feito para começar a numeração das letras minúsculas em 27,
        # onde 'a' = 27, 'b' = 28, e assim por diante, até 'z' = 52.
        numero = i - ord('a') + 27

        # Adiciona a letra minúscula e seu número correspondente ao dicionário 'mapeamento'.
        # A chave é a letra minúscula, e o valor é o número associado (como uma string).
        mapeamento[letra] = str(numero)

    # Adiciona um mapeamento para o espaço em branco no dicionário 'mapeamento'.
    # A chave é o espaço (' '), e o valor é '53'.
    # Isso é feito para codificar espaços em branco na mensagem.
    mapeamento[' '] = '53'
    
    # Inicializa uma lista vazia chamada 'mensagem_codificada_lista'.
    # Esta lista será usada para armazenar os valores numéricos correspondentes
    # a cada caractere da mensagem original durante a codificação.
    mensagem_codificada_lista = []


    # Inicia um loop 'for' que percorre cada caractere na string 's'.
    # 's' é a mensagem original que será codificada.
    for caractere in s:
        
        # Usa o dicionário 'mapeamento' para encontrar o valor codificado correspondente
        # ao caractere atual. O dicionário 'mapeamento' contém pares de chave-valor,
        # onde as chaves são caracteres (letras maiúsculas, minúsculas e espaço) e
        # os valores são os números codificados associados a esses caracteres.
        valor_codificado = mapeamento[caractere]

        # Adiciona o valor codificado do caractere atual à lista 'mensagem_codificada_lista'.
        # Esta lista está sendo usada para coletar os valores codificados de todos os caracteres
        # da mensagem original 's'.
        mensagem_codificada_lista.append(valor_codificado)

    # Utiliza o método 'join' para converter a lista 'mensagem_codificada_lista' em uma string.
    # Este método concatena todos os elementos da lista em uma única string, resultando na
    # mensagem codificada completa. Cada elemento da lista é um número em forma de string
    # representando um caractere da mensagem original.
    mensagem_codificada = ''.join(mensagem_codificada_lista)

    # Retorna a mensagem codificada. Esta string é a versão codificada da mensagem original 's',
    # onde cada caractere foi substituído pelo seu valor numérico correspondente conforme
    # definido no dicionário 'mapeamento'.
    return mensagem_codificada



# Define a variável 'mensagem' com o valor da string "Ola estou aprendendo Python agora".
# Esta é a mensagem original que será codificada. A string pode ser qualquer texto
# que você deseja codificar usando o mapeamento definido na função 'codificar_mensagem'.
mensagem = "Ola estou aprendendo Python agora"

# "Ola estou aprendendo Python agora"

# Chama a função 'codificar_mensagem', passando a variável 'mensagem' como argumento.
# Esta função é responsável por converter cada caractere da mensagem original em um valor
# numérico codificado, baseado no mapeamento predefinido que associa letras e espaços a números.
# O resultado dessa função, que é a mensagem codificada, é armazenado na variável 'mensagem_codificada'.
mensagem_codificada = codificar_mensagem(mensagem)

# Imprime a mensagem codificada no console. 
# O comando 'print' é usado para exibir a string "Mensagem Codificada:" seguida do valor
# da variável 'mensagem_codificada'. Esta variável contém a versão codificada da mensagem
# original, onde cada caractere foi substituído pelo seu valor correspondente conforme
# o mapeamento definido na função 'codificar_mensagem'.
print("Mensagem Codificada:", mensagem_codificada)

        
        
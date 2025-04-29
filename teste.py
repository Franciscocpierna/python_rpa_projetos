
'''def calcula_fatorial(n):
 
    if n == 0:
        return 1
    return n*calcula_fatorial(n-1)
  

print(calcula_fatorial(5))  # Saída: 120
palavras = ['Olá,', 'como', 'vai', 'você?']
print(palavras)
frase = ' '.join(palavras)
print(frase)
espaco=[" "," "," "]
nova = '|'.join(espaco)
print(nova)
# Define a função chamada 'eh_primo', que recebe um parâmetro 'numero'.
# Esta função verifica se um número é primo.
def eh_primo(numero):
    
    # Primeiro, verifica se o número é menor que 2.
    # Por definição, números menores que 2 não são primos.
    if numero < 2:
        return False
    
    # Inicia um laço que vai de 2 até o número-1.
    # O laço testa se o número pode ser dividido de forma 
            # igual por algum número nesse intervalo.
    for i in range(2, numero):
        print("i", i)  # Imprime o valor de 'i' a cada iteração.
        # Se o número for divisível por algum 'i', ele não é primo.
        if numero % i == 0:
            return False
    
    # Se o laço terminar sem encontrar nenhum 
            # divisor, o número é primo.
    return True

# Chama a função 'eh_primo' com o número 7.
# Armazena o resultado retornado pela função 
        # na variável 'resultado'.
resultado = eh_primo(2)

# Imprime o resultado da função.
# A f-string é usada para incluir o resultado da 
        # verificação na mensagem exibida.
print(f"É primo? {resultado}")
'''
'''
dicionario_palavras = ["casa", "carro", "jogo", "animal", "caminho", "livro", "escola", "planta"]
import random
palavra_escolhida = random.choice(dicionario_palavras)
print(palavra_escolhida)

palavra = palavra_escolhida[0]
print(palavra)
print("dicionario_palavras[0][0]",dicionario_palavras[0][0])
'''
1350//10000 # 0.1350
print("a divisão = ",1350//100000) # 0
print("a divisão = ",1350/100000) 
milhares = 1350//10000
if milhares:
    print("milhares = ", milhares)
else:
    print("milhares = 0")
    
milhares = 1350//1000    
print("a divisão = ",1350/1000)
if milhares:
    print("milhares = ", milhares)
else:
    print("milhares = 0")
    
    
'''
# Define o caminho do arquivo Excel que contém os dados. Este arquivo deve
# estar acessível no mesmo diretório do script ou o caminho deve ser
# ajustado adequadamente.
caminho_planilha = "CEP.xls"
# Cria um arquivo Excel no formato 2003
#workbook = xlwt.Workbook()
#sheet = workbook.add_sheet("CEP")
#columns=['CEP', 'Logradouro', 'Bairro', 'Localidade', 'UF']        
# Escreve os cabeçalhos (nomes das colunas)
sheet = xlwt.open_workbook("CEP.xls")

sheet.write(0, 0, "Cep")  # Linha 0, Coluna 0
sheet.write(0, 1, "Logradouro")  # Linha 0, Coluna 1
sheet.write(0, 2, "Bairro")  # Linha 1, Coluna 0
sheet.write(0, 3, "Localidade")  # Linha 1, Coluna 1
sheet.write(0, 4, "UF")  # Linha 2, Coluna 0

df = pd.read_excel("CEP.xls")

linha = 0 
for cep in df:
    endereco = obter_endereco_por_cep(str(cep).replace('-', ''))
# Verifica se o dicionário contém a chave 'erro'. A presença dessa
    # chave indica que o CEP não foi encontrado.
    if "erro" not in endereco:
        
        linha = linha +1       
        # Escreve os valores do endereço
        sheet.write(linha, 0, endereco.get("cep", ''))  # Linha 1, Coluna `col`
        sheet.write(linha, 1, endereco.get('logradouro', ''))  # Linha 1, Coluna `col`
        sheet.write(linha, 2, endereco.get('bairro', ''))  # Linha 1, Coluna `col`
        sheet.write(linha, 3, endereco.get('localidade', ''))  # Linha 1, Coluna `col`
        sheet.write(linha, 4, endereco.get('uf', ''))  # Linha 1, Coluna `col`
  
       
      
        
        # Salva o arquivo Excel
        sheet.save("CEP")
        
        # Imprime uma mensagem de sucesso
        print(f"Dados salvos com sucesso no arquivo CEP.xls")
        
    else:
        # Se a chave 'erro' estiver presente, imprime uma mensagem de erro.
        print("Não foi possível salvar os dados: CEP não encontrado.")
    

print("Endereços salvos na aba 'Dados' da planilha 'CEP.xls'.")
#Abro o arquivo
#os.startfile("CEP.")

'''    
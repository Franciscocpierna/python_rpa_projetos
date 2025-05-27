#Encontro em qual página está o texto e trato um pouco os dados

#Separo a parte de um texto de uma página
from PyPDF2 import PdfReader
from pathlib import Path

# Define o caminho do arquivo PDF.
caminhoArquivo = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Mercado_Livre.pdf"

# Abre o arquivo PDF usando a classe 'PdfReader'.
PDF_MercadoLivre = PdfReader(caminhoArquivo)

# Texto a ser procurado no PDF.
texto = """Entendendo sobre a criação do 
Preço
"""

# Inicializa o contador para o número da página.
numeroPagina = 1

# Itera sobre cada página no arquivo PDF.
for pagina in PDF_MercadoLivre.pages:
    
    # Extrai o texto da página atual usando o método 'extract_text'.
    textoDaPagina = pagina.extract_text()
    
    # Verifica se o texto procurado está na página atual.
    if texto in textoDaPagina:
        
        # Se o texto especificado na variável 'texto' for encontrado no 'textoDaPagina' 
        # (o texto extraído da página atual),
        # o programa executa o bloco de código dentro do 'if'.
        # Imprime o número da página onde o texto foi encontrado.
        print("Texto está na página: ", numeroPagina)
        

        # Organiza um pouco mais o texto com substituições para melhorar a formatação.
        # Realiza substituições no texto extraído para melhorar sua legibilidade:
        # 1. Substitui " ." por uma quebra de linha ("\n"), o que ajuda a separar as sentenças.
        # 2. Remove linhas duplas em branco ("\n \n").
        # 3. Substitui múltiplos espaços e quebras de linha por um único espaço.
        textoDaPagina = textoDaPagina.replace(" .", "\n").replace("\n \n", "").replace(""" 
    """, " ")
        
        # Encontra a posição inicial e final do texto específico dentro do texto da página.
        posicaoInicial = textoDaPagina.find("LEMBRANDO QUE : ")
        
        # 'find' procura a string "LEMBRANDO QUE : " no 'textoDaPagina' e retorna a posição onde começa.
        # Se não for encontrada, retorna -1.
        # Procura a string "links abaixo." após a posição inicial e retorna a posição onde termina.
        # O '+ len("links abaixo.")' garante que o texto "links abaixo." seja incluído no texto final extraído.
        posicaoFinal = textoDaPagina.find("links abaixo.", posicaoInicial + 1) + len("links abaixo.")
        
        
        print("Posição Inicial:", posicaoInicial)
        print("Posição Final:", posicaoFinal)
        
        # Verifica se as posições foram encontradas antes de extrair o texto.
        # Esta condição verifica se tanto a 'posicaoInicial' quanto a 'posicaoFinal' são diferentes de -1.
        # Em Python, o método 'find' retorna -1 se a substring não for encontrada no texto.
        # Portanto, se ambas as posições não são -1, significa que as strings de início e 
        # fim desejadas foram encontradas no texto.
        if posicaoInicial != -1 and posicaoFinal != -1:
            
            
            # Se ambas as strings foram encontradas (ou seja, as posições iniciais e finais não são -1),
            # o programa extrai o texto entre essas posições.
            textoSeparado = textoDaPagina[posicaoInicial:posicaoFinal]
            
            # 'textoDaPagina[posicaoInicial:posicaoFinal]' extrai uma substring do 'textoDaPagina'.
            # A extração começa na 'posicaoInicial' (inclusive) e vai até a 'posicaoFinal' (não inclusiva).
            # Isso significa que o texto extraído começa no ponto onde a primeira string específica ("LEMBRANDO QUE : ") foi encontrada
            # e termina onde a segunda string específica ("links abaixo.") termina.

            # Imprime o texto extraído.
            print(textoSeparado)
            
            
        else:
            
            # Se uma ou ambas as strings não forem encontradas, imprime uma mensagem indicando isso.
            print("Texto não encontrado na página.")

    # Incrementa o contador do número da página.
    # Adiciona 1 ao 'numeroPagina' para passar para a próxima página no próximo loop.
    numeroPagina += 1
    
print("Pronto!")
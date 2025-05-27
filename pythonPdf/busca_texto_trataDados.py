#Encontro em qual página está o texto e trato um pouco os dados

# Importa a classe PdfReader do módulo PyPDF2 e a classe Path do módulo pathlib.
from PyPDF2 import PdfReader
from pathlib import Path

# Define o caminho do arquivo PDF que será lido.
caminhoArquivo = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Mercado_Livre.pdf"

# Utiliza a classe 'PdfReader' para abrir o arquivo PDF especificado.
# 'PdfReader' é usada para ler e extrair informações de arquivos PDF.
PDF_MercadoLivre = PdfReader(caminhoArquivo)

# Define o texto específico que está sendo procurado no arquivo PDF.
texto = """Entendendo sobre a criação do 
Preço
"""

# Inicializa a variável 'numeroPagina' para rastrear o número da página durante a iteração.
numeroPagina = 1

# Itera sobre cada página do arquivo PDF aberto.
for pagina in PDF_MercadoLivre.pages:
    
    # Utiliza o método 'extract_text()' para extrair o texto contido na página atual.
    # O texto extraído é armazenado na variável 'textoDaPagina'.
    textoDaPagina = pagina.extract_text()
    
    # Verifica se o texto definido anteriormente está presente no texto extraído da página.
    if texto in textoDaPagina:
        
        # Se o texto for encontrado, imprime o número da página onde foi encontrado.
        print("Texto está na página: ", numeroPagina)
        
        # Realiza algumas substituições no texto extraído para melhorar a sua formatação.
        # Estas substituições lidam com espaços e quebras de linha inadequadas.
        textoDaPagina = textoDaPagina.replace(" .", "\n")
        textoDaPagina = textoDaPagina.replace("\n \n", "")
        textoDaPagina = textoDaPagina.replace(""" 
""", " ")
        textoDaPagina = textoDaPagina.replace("•Para", "\n•Para")
        
        # Imprime o texto da página com a formatação ajustada.
        print(textoDaPagina)
        
    # Incrementa o número da página para continuar a busca na próxima página.
    numeroPagina += 1
    
# Ao finalizar a iteração por todas as páginas, imprime uma mensagem indicando a conclusão do processo.
print("Pronto!")

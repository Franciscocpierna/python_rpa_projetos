# Buscar texto

# Importa a classe PdfReader do módulo PyPDF2 e a classe Path do módulo pathlib.
from PyPDF2 import PdfReader
from pathlib import Path

# Define o caminho do arquivo PDF que será lido.
caminhoArquivo = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Mercado_Livre.pdf"

# Cria um objeto PDF_MercadoLivre usando a classe PdfReader.
# PdfReader é usada para abrir e ler o conteúdo de arquivos PDF.
# O arquivo PDF especificado em 'caminhoArquivo' é aberto para leitura.
PDF_MercadoLivre = PdfReader(caminhoArquivo)

# Define o texto que está sendo procurado no arquivo PDF.
texto = """Entendendo sobre a criação do 
Preço
"""

# Inicializa a variável 'numeroPagina' para acompanhar o número da página atual no loop.
numeroPagina = 1

# Itera sobre cada página do arquivo PDF.
# 'PDF_MercadoLivre.pages' retorna um iterável das páginas do arquivo PDF.
for pagina in PDF_MercadoLivre.pages:
    
    # Extrai o texto da página atual usando o método 'extract_text'.
    # 'extract_text()' retorna todo o texto encontrado na página como uma string.
    textoDaPagina = pagina.extract_text()
    
    # Verifica se o texto definido na variável 'texto' está presente no texto extraído da página.
    if texto in textoDaPagina:
        
        # Se o texto for encontrado, imprime o número da página.
        print("Texto está na página: ", numeroPagina)
    
    # Incrementa 'numeroPagina' para passar para a próxima página no próximo loop.
    numeroPagina += 1
    
# Após iterar por todas as páginas, imprime uma mensagem finalizando a busca.
print("Pronto!")
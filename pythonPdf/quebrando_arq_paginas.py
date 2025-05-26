#Cria um novo arquivo para cada página

# Importa as classes PdfReader e PdfWriter do módulo PyPDF2 e a classe Path do módulo pathlib.
# PdfReader é usada para ler arquivos PDF.
# PdfWriter é usada para criar e modificar arquivos PDF.
# Path é usado para trabalhar com caminhos de arquivos de forma orientada a objetos.
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

# Define o caminho para o arquivo PDF original.
caminhoArquivo = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Mercado_Livre.pdf"

# Cria um objeto 'PDF_MercadoLivre' usando 'PdfReader' para ler o arquivo PDF.
PDF_MercadoLivre = PdfReader(caminhoArquivo)

# Inicializa um contador para o número da página.
numeroPagina = 1

# Itera sobre cada página do arquivo PDF original.
for pagina in PDF_MercadoLivre.pages:
   
    # Cria um objeto 'novoPDF' usando 'PdfWriter' para cada nova página.
    novoPDF = PdfWriter()

    # Adiciona a página atual ao novo objeto PDF.
    novoPDF.add_page(pagina)

    # Define o caminho da pasta onde os novos arquivos PDF serão salvos.
    caminhoPasta = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\arquivos_quebrados\\"

    # Esta linha cria uma string 'caminhoPasta' que representa o caminho da pasta onde os novos arquivos PDF serão armazenados.
    # A string inclui o nome da pasta "PDFs Mercado Livre" seguido de uma barra invertida (\\) que é usada em caminhos de arquivo no Windows.

    # 'Path(caminhoPasta)' cria um objeto Path a partir do caminho fornecido na variável 'caminhoPasta'.
    # O método '.mkdir(parents=True, exist_ok=True)' tenta criar um diretório no caminho especificado.
    # 'parents=True' autoriza a criação de diretórios pais se eles não existirem. Isso é útil se o caminho completo não existir e precisar ser criado.
    # 'exist_ok=True' permite que o método não lance uma exceção caso o diretório já exista. Isso evita um erro se tentarmos criar um diretório que já está presente.
    Path(caminhoPasta).mkdir(parents=True, exist_ok=True)

    # Cria o caminho completo do novo arquivo PDF para a página atual.
    # Esta linha cria um objeto Path 'caminhoArquivoNovo' para o novo arquivo PDF.
    # O caminho completo do arquivo é formado pela concatenação do caminho da pasta 'caminhoPasta', um nome base para o arquivo ('Arquivo_Mercado_Livre'), o número da página atual (convertido em string) e a extensão '.pdf'.
    # Por exemplo, se 'numeroPagina' for 1, o caminho completo será "PDFs Mercado Livre\\Arquivo_Mercado_Livre1.pdf".
    caminhoArquivoNovo = Path(caminhoPasta + 'Arquivo_Mercado_Livre' + str(numeroPagina) + '.pdf')

    # Abre um novo arquivo para gravação no modo binário ('wb').
    # 'with' é uma estrutura de gerenciamento de contexto que garante que o arquivo seja fechado adequadamente após o uso.
    # 'caminhoArquivoNovo.open(mode='wb')' abre o arquivo no modo de escrita binária ('wb'). 
    # 'wb' significa 'write binary' e é necessário para escrever em arquivos PDF, que são tratados como binários.
    with caminhoArquivoNovo.open(mode='wb') as arquivoConcluido:

        # Escreve o conteúdo do 'novoPDF' no arquivo.
        # 'novoPDF.write(arquivoConcluido)' escreve o conteúdo do objeto 'novoPDF' no arquivo. 
        # Isso salva efetivamente a página atual do PDF no arquivo físico.
        novoPDF.write(arquivoConcluido)


    # Incrementa o contador do número da página.
    numeroPagina += 1

# Imprime uma mensagem indicando que o processo foi concluído.
print("Pronto!")
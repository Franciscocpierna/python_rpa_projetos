#Cria um novo arquivo para páginas especificas

# Importa as classes PdfReader e PdfWriter do módulo PyPDF2 e a classe Path do módulo pathlib.
# PdfReader é usada para ler arquivos PDF, substituindo a antiga PdfFileReader.
# PdfWriter é usada para criar e modificar arquivos PDF, substituindo a antiga PdfFileWriter.
# Path é usada para manipular caminhos de arquivos e diretórios.
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

# Define o caminho para o arquivo PDF original.
caminhoArquivo = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Mercado_Livre.pdf"

try:
    
    # Cria um objeto 'PDF_MercadoLivre' usando 'PdfReader' para ler o arquivo PDF.
    PDF_MercadoLivre = PdfReader(caminhoArquivo)

    # Define uma lista de números de páginas que serão incluídas no novo arquivo PDF.
    paginas = [5, 10, 15, 20]

    # Cria um objeto 'novoPDF' usando 'PdfWriter' para o novo arquivo PDF.
    novoPDF = PdfWriter()

    # Itera sobre cada página do arquivo PDF original usando enumerate para 
    # obter o índice da página.
    # 'enumerate' é uma função que permite iterar sobre algo (neste caso, as páginas do PDF) e receber um índice (i) junto com cada elemento (pagina).
    # 'PDF_MercadoLivre.pages' fornece uma sequência das páginas do PDF.
    # 'start=1' indica que a numeração do índice começa em 1, o que é comum para a numeração de páginas em documentos.
    for i, pagina in enumerate(PDF_MercadoLivre.pages, start=1):
        
        
        # Verifica se o número da página atual está na lista 'paginas'.
        # Se o índice da página (i) está na lista 'paginas', o bloco de código dentro do 'if' será executado.
        # 'paginas' é uma lista pré-definida de números de páginas que serão incluídas no novo PDF.
        if i in paginas:
            
            
            # Adiciona a página ao objeto 'novoPDF'.
            # 'add_page(pagina)' é um método de 'PdfWriter' que adiciona a página atual à instância 'novoPDF'.
            # 'novoPDF' atua como um novo documento PDF em construção, que conterá apenas as páginas especificadas.
            novoPDF.add_page(pagina)
            
            # Imprime o número da página que está sendo adicionada.
            # Esta linha imprime uma mensagem no console, indicando qual número de página está sendo processado e adicionado ao novo PDF.
            print(f"Adicionando página {i}")
            
    # Define o caminho da pasta onde o novo arquivo PDF será salvo.
    # A variável 'caminhoPasta' armazena o caminho da pasta destino para o novo arquivo PDF.
    # A barra invertida dupla (\\) é usada como separador de caminhos em sistemas Windows.
    caminhoPasta = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\novo2\\"
    
    # Cria o diretório especificado, se ele ainda não existir.
    # 'Path(caminhoPasta).mkdir(parents=True, exist_ok=True)' cria o diretório especificado em 'caminhoPasta', se ainda não existir.
    # 'parents=True' assegura a criação de diretórios pais, caso necessário.
    # 'exist_ok=True' evita um erro se o diretório já existir, permitindo que o programa continue.
    Path(caminhoPasta).mkdir(parents=True, exist_ok=True)
    
    # Cria o caminho completo do novo arquivo PDF.
    # 'Path' é usado para criar um objeto Path representando o caminho completo para o novo arquivo PDF.
    # A string do caminho é formada pela concatenação do caminho da pasta, o nome do arquivo e a extensão '.pdf'.
    caminhoArquivoNovo = Path(caminhoPasta + 'Arquivo_Mercado_Livre_Selecionado.pdf')
    
    # Abre um novo arquivo para gravação no modo binário ('wb').
    # A instrução 'with' assegura que o arquivo será fechado corretamente após a sua utilização.
    # 'open(mode='wb')' abre o arquivo no modo de escrita binária, necessário para arquivos PDF.
    with caminhoArquivoNovo.open(mode='wb') as arquivoConcluido:
        
        # Escreve o conteúdo do 'novoPDF' no arquivo.
        # 'novoPDF.write(arquivoConcluido)' grava o conteúdo 
        # de 'novoPDF' (as páginas selecionadas) no arquivo especificado.
        # Isso resulta na criação de um arquivo PDF contendo apenas as páginas desejadas.
        novoPDF.write(arquivoConcluido)
        
        
    # Imprime uma mensagem indicando que o processo foi concluído.
    print("Arquivo PDF com páginas selecionadas criado com sucesso!")

except FileNotFoundError:
    
    # Captura outras exceções genéricas e imprime uma mensagem de erro.
    print(f"Ocorreu um erro: {e}")
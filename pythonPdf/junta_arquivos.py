#Junta 2 arquivos

# Importa a classe PdfMerger do módulo PyPDF2 e a classe Path do módulo pathlib.
# PdfMerger é usada para mesclar vários arquivos PDF em um único arquivo, substituindo a antiga PdfFileMerger.
# Path é usada para manipular caminhos de arquivos e diretórios.
from PyPDF2 import PdfMerger
from pathlib import Path

try:
    
    # Cria um objeto 'pdf_Principal' usando 'PdfMerger' para mesclar vários arquivos PDF em um.
    pdf_Principal = PdfMerger()

    # Define os caminhos para os arquivos PDF que serão mesclados.
    pdf1 = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Evolução_Amazon.pdf"
    pdf2 = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Mercado_Livre.pdf"

    # Adiciona os arquivos PDF ao objeto 'pdf_Principal' para mesclagem.
    # 'pdf_Principal' é uma instância da classe PdfMerger, usada para mesclar vários arquivos PDF.
    # O método 'append' é usado para adicionar cada arquivo PDF individualmente à instância 'pdf_Principal'.
    # 'pdf1' e 'pdf2' são strings que contêm os caminhos dos arquivos PDF que serão mesclados.
    # Ao chamar 'append', cada um desses arquivos PDF é adicionado à fila de mesclagem em 'pdf_Principal'.
    pdf_Principal.append(pdf1)
    pdf_Principal.append(pdf2)
    
    # Define o caminho da pasta onde o arquivo PDF mesclado será salvo.
    # 'caminhoPasta' é uma string que especifica o caminho do diretório onde o arquivo PDF resultante será armazenado.
    # O uso de duas barras invertidas (\\) é uma convenção de caminho em sistemas Windows.
    caminhoPasta = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\novo2\\"
    
    # Cria o diretório se ele não existir.
    # 'Path(caminhoPasta)' cria um objeto Path usando o caminho especificado.
    # O método 'mkdir' com 'parents=True' e 'exist_ok=True' tenta criar o diretório.
    # 'parents=True' garante a criação de diretórios pais se não existirem.
    # 'exist_ok=True' faz com que o método não gere um erro se o diretório já existir.
    Path(caminhoPasta).mkdir(parents=True, exist_ok=True)
    
    # Cria o caminho completo do arquivo PDF mesclado.
    # Aqui, um objeto Path 'caminhoArquivoMesclado' é criado, representando o caminho completo do arquivo PDF resultante.
    # O caminho é formado pela concatenação da string 'caminhoPasta' com o nome do arquivo 'PDF_Consolidado.pdf'.
    caminhoArquivoMesclado = Path(caminhoPasta + 'PDF_Consolidado.pdf')
    
    # Abre um novo arquivo para gravação no modo binário ('wb').
    # 'with' é uma estrutura que garante o fechamento correto do arquivo após a sua utilização.
    # 'open(mode='wb')' abre o arquivo no modo de escrita binária, necessário para arquivos PDF.
    with caminhoArquivoMesclado.open(mode='wb') as arquivoConcluido:
        
        # Escreve o conteúdo do PDF mesclado no arquivo.
        # O método 'write' de 'pdf_Principal' grava o conteúdo mesclado dos PDFs no arquivo especificado em 'arquivoConcluido'.
        # Isso resulta na criação do arquivo PDF consolidado no local especificado.
        pdf_Principal.write(arquivoConcluido)
        


    # Imprime uma mensagem indicando que o processo foi concluído.
    print("Arquivo PDF mesclado criado com sucesso!")

except FileNotFoundError:
    
    # Captura a exceção se algum dos arquivos PDF originais não for encontrado e imprime uma mensagem de erro.
    print("Um dos arquivos PDF originais não foi encontrado. Verifique os caminhos dos arquivos.")

except Exception as e:
    
    # Captura outras exceções genéricas e imprime uma mensagem de erro.
    print(f"Ocorreu um erro: {e}")
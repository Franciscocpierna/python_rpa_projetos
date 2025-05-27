#Junta 3 arquivos PDF jeito 2

# Importa a classe PdfMerger do módulo PyPDF2.
# PdfMerger é uma classe usada para mesclar vários arquivos PDF em um único arquivo.
from PyPDF2 import PdfMerger
from pathlib import Path

# Define os caminhos para os arquivos PDF que serão mesclados.
pdf1 = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Evolução_Amazon.pdf"
pdf2 = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\SEBRAE-AMAZON.pdf"
pdf3 = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Mercado_Livre.pdf"

try:
    
    # Cria um objeto 'juntarPDFs' usando 'PdfMerger'.
    # Este objeto será usado para realizar a operação de mesclagem dos arquivos PDF.
    juntarPDFs = PdfMerger()

    # Itera sobre cada arquivo PDF na lista fornecida e adiciona-os para mesclagem.
    for pdf in [pdf1, pdf2, pdf3]:
        
        # O método 'append' é usado para adicionar cada arquivo PDF ao objeto 'juntarPDFs'.
        juntarPDFs.append(pdf)

    # Define o caminho da pasta onde o arquivo PDF mesclado será salvo.
    caminhoPasta = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\novo2\\"
    
    # Cria o diretório se ele não existir.
    # 'Path(caminhoPasta)' cria um objeto Path usando a string fornecida em 'caminhoPasta'.
    # Este objeto Path representa um caminho no sistema de arquivos.
    # '.mkdir(parents=True, exist_ok=True)' é um método do objeto Path que cria um diretório no caminho especificado.
    # 'parents=True' instrui o método para criar diretórios pais se eles não existirem. Isso é útil se partes do caminho especificado ainda não existirem e precisarem ser criadas automaticamente.
    # 'exist_ok=True' faz com que o método não levante uma exceção se o diretório já existir. Em vez disso, ele permite que a operação prossiga sem criar um novo diretório, evitando um erro de diretório já existente.
    Path(caminhoPasta).mkdir(parents=True, exist_ok=True)
    
    # Define o caminho completo do arquivo PDF mesclado.
    # Esta linha cria um objeto Path 'caminhoArquivoMesclado' que representa o caminho completo para o arquivo PDF que será criado.
    # O caminho completo é formado pela concatenação do caminho da pasta 'caminhoPasta' com o nome do arquivo '3_arquivos_Juntos.pdf'.
    # Por exemplo, se 'caminhoPasta' for "PDF 3 Arquivos\\", o caminho completo será "PDF 3 Arquivos\\3_arquivos_Juntos.pdf".
    caminhoArquivoMesclado = Path(caminhoPasta + '3_arquivos_Juntos.pdf')
    
    # Salva o arquivo PDF mesclado no caminho especificado.
    # O método 'write' do objeto 'juntarPDFs' é usado para escrever o conteúdo do PDF mesclado no arquivo.
    # 'caminhoArquivoMesclado' especifica o local e o nome do arquivo onde o PDF mesclado será salvo.
    # Esta operação escreve todos os dados mesclados dos arquivos PDF no arquivo de destino, criando efetivamente um único arquivo PDF consolidado.
    juntarPDFs.write(caminhoArquivoMesclado)
    
    # Imprime uma mensagem indicando que o processo foi concluído.
    print("Arquivo PDF mesclado criado com sucesso!")

except FileNotFoundError:

    # Captura a exceção se algum dos arquivos PDF originais não for encontrado e imprime uma mensagem de erro.
    print("Um dos arquivos PDF originais não foi encontrado. Verifique os caminhos dos arquivos.")

except Exception as e:
    
    # Captura outras exceções genéricas e imprime uma mensagem de erro.
    print(f"Ocorreu um erro: {e}")
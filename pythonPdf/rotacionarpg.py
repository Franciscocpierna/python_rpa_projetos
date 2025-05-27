#Cria um novo arquivo para cada página

#Rotacionar a página

# Importa as classes PdfReader e PdfWriter do módulo PyPDF2 e a classe Path do módulo pathlib.
# PdfReader é usada para ler arquivos PDF, substituindo a antiga PdfFileReader.
# PdfWriter é usada para criar e modificar arquivos PDF, substituindo a antiga PdfFileWriter.
# Path é usado para trabalhar com caminhos de arquivos de forma orientada a objetos.
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

# Define o caminho para o arquivo PDF original.
caminhoArquivo = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Mercado_Livre.pdf"

try:
    
    # Cria um objeto 'PDF_MercadoLivre' usando 'PdfReader' para ler o arquivo PDF.
    PDF_MercadoLivre = PdfReader(caminhoArquivo)

    # Inicializa um contador para o número da página.
    numeroPagina = 1

    # Itera sobre cada página do arquivo PDF original.
    for pagina in PDF_MercadoLivre.pages:
        
        # Rotaciona a página em 180 graus.
        # O método 'rotate' é usado para rotacionar a página. 
        # O ângulo de rotação é especificado em graus.
        pagina.rotate(270)

        # Cria um objeto 'novoPDF' usando 'PdfWriter' para cada nova página rotacionada.
        novoPDF = PdfWriter()

        # Adiciona a página rotacionada ao objeto 'novoPDF'.
        novoPDF.add_page(pagina)

        # Define o caminho da pasta onde os novos arquivos PDF rotacionados serão salvos.
        caminhoPasta = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\novo_pdf\\"
        
        # 'Path(caminhoPasta)' cria um objeto Path usando o caminho especificado.
        # O método '.mkdir(parents=True, exist_ok=True)' é chamado nesse objeto Path.
        # 'parents=True' autoriza a criação automática de diretórios pais se eles não existirem. Isso é útil se o caminho completo ainda não existir no sistema de arquivos.
        # 'exist_ok=True' significa que se o diretório já existir, nenhuma exceção será levantada, evitando erros de diretório já existente.
        Path(caminhoPasta).mkdir(parents=True, exist_ok=True)
        

        # Cria o caminho completo do novo arquivo PDF rotacionado.
        # Esta linha constrói o caminho completo para o novo arquivo PDF.
        # O caminho é formado pela concatenação do 'caminhoPasta', o nome do arquivo 'Arquivo_Mercado_Livre', o número da página (convertido em string) e a extensão '.pdf'.
        # 'Path(...)' é usado para criar um objeto Path que representa este caminho de arquivo completo.
        caminhoArquivoNovo = Path(caminhoPasta + 'Arquivo_Mercado_Livre' + str(numeroPagina) + '.pdf')
        
        # Abre um novo arquivo para gravação no modo binário ('wb').
        # 'with' aqui é usado para abrir o arquivo e garantir que ele seja fechado adequadamente após a escrita, evitando vazamentos de recursos.
        # 'caminhoArquivoNovo.open(mode='wb')' abre o arquivo no modo binário de escrita ('wb'). 'wb' é necessário para arquivos PDF, que são tratados como binários.
        # 'as arquivoConcluido' cria uma variável temporária que representa o arquivo aberto.
        with caminhoArquivoNovo.open(mode='wb') as arquivoConcluido:
            
            # Escreve o conteúdo do 'novoPDF' no arquivo.
            # 'novoPDF.write(arquivoConcluido)' grava o conteúdo do objeto 'novoPDF' (que contém a página rotacionada) no arquivo aberto.
            # Isso resulta na criação de um arquivo PDF contendo a página rotacionada.
            novoPDF.write(arquivoConcluido)
            

        # Incrementa o contador do número da página.
        numeroPagina += 1

    # Imprime uma mensagem indicando que o processo foi concluído.
    print("Arquivo PDF com páginas rotacionadas criado com sucesso!")

except FileNotFoundError:
    
    # Captura a exceção se o arquivo PDF original não for encontrado.
    print("Arquivo PDF original não encontrado. Verifique o caminho do arquivo.")
    
except Exception as e:
    
    # Captura outras exceções genéricas.
    print(f"Ocorreu um erro: {e}")
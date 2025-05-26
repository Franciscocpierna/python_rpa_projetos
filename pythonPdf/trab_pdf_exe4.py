# Importa as classes 'PdfReader' e 'PdfWriter' da biblioteca 'PyPDF2' e o módulo 'os'.
# 'PdfReader' é usado para ler arquivos PDF, 'PdfWriter' para criar e modificar arquivos PDF 
# 'os' para interagir com o sistema operacional.
from PyPDF2 import PdfReader, PdfWriter
import os

try:
    
    # Bloco 'try' para tentar executar o código seguinte e capturar exceções que possam ocorrer.

    # Cria um objeto 'arquivoPDF' usando 'PdfReader' para abrir e ler o arquivo "Mercado_Livre.pdf".
    # Um erro aqui pode gerar uma exceção 'FileNotFoundError' se o arquivo não for encontrado.
    arquivoPDF = PdfReader("C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Mercado_Livre.pdf")

    # Cria um objeto 'novoArquivoPDF' usando 'PdfWriter'.
    # Este objeto será usado para criar um novo arquivo PDF.
    novoArquivoPDF = PdfWriter()

    # Itera sobre cada página do arquivo PDF original.
    for pagina in arquivoPDF.pages:
        
        # Adiciona cada página do arquivo PDF original ao novo arquivo PDF.
        novoArquivoPDF.add_page(pagina)

    # Adiciona metadados personalizados ao novo arquivo PDF.
    # Define informações como autor, criador, produtor, assunto e título.
    novoArquivoPDF.add_metadata(
        {
            "/Author": "Clevison Santos",
            "/Creator": "Python PdfWriter",
            "/Producer": "Curso Python PDF",
            "/Subject": "Ensinando a trabalhar com PDF",
            "/Title": "Curso RPA Python",
        }
    )

    # Define o nome do novo arquivo PDF que será criado.
    novo_arquivo = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Arquivo_Alterado_Mercado_Livre.pdf"

    # Abre um novo arquivo para gravação no modo binário ('wb').
    with open(novo_arquivo, "wb") as dadosArquivo:
        
        # 'with' é uma palavra-chave em Python que é usada para definir um gerenciador de contexto.
        # Um gerenciador de contexto é um objeto Python que define um contexto para a execução de um bloco de código.
        # O uso de 'with' garante que recursos como arquivos sejam adequadamente gerenciados, abrindo-os e fechando-os conforme necessário.

        # 'open(novo_arquivo, "wb")' é chamado dentro do contexto do 'with'.
        # Isso significa que o arquivo especificado por 'novo_arquivo' é aberto no modo 'wb' (escrita binária).
        # O arquivo permanece aberto enquanto o código dentro do bloco 'with' é executado.

        # 'as dadosArquivo' cria uma variável temporária 'dadosArquivo'.
        # Esta variável é associada ao arquivo aberto. Qualquer operação de arquivo será realizada usando essa variável.
        # Em outras palavras, 'dadosArquivo' agora representa o arquivo aberto 'novo_arquivo' no modo 'wb'.

        # Escreve o conteúdo do 'novoArquivoPDF' no arquivo físico.
        # Aqui, o método 'write' do objeto 'novoArquivoPDF' é chamado.
        # Este método leva 'dadosArquivo' (o arquivo aberto) como argumento e escreve nele o conteúdo do PDF.
        # Isso inclui todas as páginas e metadados adicionados ao 'novoArquivoPDF'.
        novoArquivoPDF.write(dadosArquivo)
        
        

    # Após a execução do bloco de código dentro do 'with', o arquivo 'dadosArquivo' é automaticamente fechado.
    # Isso é uma parte crucial do gerenciamento de recursos, pois garante que o arquivo não permaneça aberto ou bloqueado pelo programa.
    # O fechamento automático do arquivo reduz a possibilidade de erros, como vazamentos de recursos ou corrupção de arquivos.


    # Verifica se o novo arquivo PDF foi criado com sucesso.
    if os.path.exists(novo_arquivo):
        
        # Imprime uma mensagem de sucesso se o arquivo for encontrado no sistema de arquivos.
        print(f"Arquivo '{novo_arquivo}' criado com sucesso!")
        
    else:
        
        # Imprime uma mensagem de erro se o arquivo não for encontrado.
        print(f"Erro ao criar o arquivo '{novo_arquivo}'.")

# Captura a exceção 'FileNotFoundError', que ocorre se o arquivo PDF original não for encontrado.
except FileNotFoundError:
    print("Arquivo PDF de origem não encontrado. Verifique o caminho do arquivo.")

# Captura qualquer outra exceção genérica que possa ocorrer.
except Exception as e:
    print(f"Ocorreu um erro: {e}")
# Criando senha para o arquivo PDF

# Importa as classes 'PdfReader' e 'PdfWriter' da biblioteca 'PyPDF2'.
# 'PdfReader' é usada para ler arquivos PDF, enquanto 'PdfWriter' é usada para criar e modificar arquivos PDF.
from PyPDF2 import PdfReader, PdfWriter

try:
    
    # Tenta abrir o arquivo PDF especificado usando 'PdfReader'.
    # 'PdfReader' é usado para ler e acessar o conteúdo do arquivo PDF "Arquivo_Alterado_Mercado_Livre.pdf".
    arquivoPDF = PdfReader("C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Arquivo_Alterado_Mercado_Livre.pdf")

    # Cria um objeto 'novoArquivoPDF' usando 'PdfWriter'.
    # 'PdfWriter' será usado para escrever em um novo arquivo PDF.
    novoArquivoPDF = PdfWriter()

    # Itera sobre cada página do arquivo PDF original.
    for pagina in arquivoPDF.pages:
        
        # Adiciona cada página do arquivo PDF original ao novo arquivo PDF.
        # Isso copia todas as páginas do PDF original para o novo PDF.
        novoArquivoPDF.add_page(pagina)
    
    # Adiciona uma senha ao novo arquivo PDF.
    # 'encrypt' é um método do 'PdfWriter' que adiciona criptografia ao arquivo PDF.
    # Aqui, 'aluno' é a senha definida para o novo arquivo PDF.
    novoArquivoPDF.encrypt("aluno")

    # Define o nome do novo arquivo PDF que será criado com senha.
    novo_arquivo_com_senha = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Senha_Arquivo_Alterado_Mercado_Livre.pdf"

    # Abre um novo arquivo para gravação no modo binário ('wb').
    # 'with' é uma palavra-chave em Python que é usada para definir um gerenciador de contexto.
    with open(novo_arquivo_com_senha, "wb") as dadosArquivo:
        
        # Escreve o conteúdo do 'novoArquivoPDF' no arquivo físico.
        # Isso cria o arquivo PDF no sistema de arquivos com as páginas e a senha adicionadas.
        novoArquivoPDF.write(dadosArquivo)

    # Imprime uma mensagem indicando que o processo foi concluído.
    print("Arquivo PDF protegido por senha criado com sucesso!")

except FileNotFoundError:
    
    # Captura a exceção se o arquivo PDF original não for encontrado e imprime uma mensagem de erro.
    print("Arquivo PDF original não encontrado. Verifique o caminho do arquivo.")
    
except Exception as e:
    
    # Captura outras exceções genéricas e imprime uma mensagem de erro.
    print(f"Ocorreu um erro: {e}")
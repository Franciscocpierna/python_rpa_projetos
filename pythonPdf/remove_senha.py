#Removendo a senha para o arquivo PDF

# Importa as classes 'PdfReader' e 'PdfWriter' da biblioteca 'PyPDF2'.
# 'PdfReader' é usada para ler arquivos PDF, enquanto 'PdfWriter' é usada para criar e modificar arquivos PDF.
from PyPDF2 import PdfReader, PdfWriter

try:
    
    # Abre o arquivo PDF protegido por senha.
    # 'PdfReader' é utilizado para criar um objeto que representa o arquivo PDF "Senha_Arquivo_Alterado_Mercado_Livre.pdf".
    arquivoPDF = PdfReader("C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Senha_Arquivo_Alterado_Mercado_Livre.pdf")

    # Cria um objeto 'novoArquivoPDF' usando 'PdfWriter'.
    # 'PdfWriter' será usado para escrever em um novo arquivo PDF sem senha.
    novoArquivoPDF = PdfWriter()

    # Verifica se o arquivo PDF está criptografado (ou seja, protegido por senha).
    if arquivoPDF.is_encrypted:
        
        # Tenta remover a senha do arquivo PDF.
        # 'decrypt' é um método do 'PdfReader' que descriptografa o arquivo PDF usando a senha fornecida.
        # Se a senha estiver correta, o arquivo será descriptografado; caso contrário, uma exceção será levantada.
        arquivoPDF.decrypt("aluno")

    # Itera sobre cada página do arquivo PDF original.
    for pagina in arquivoPDF.pages:
        
        # Adiciona cada página do arquivo PDF original ao novo arquivo PDF.
        # Isso copia todas as páginas do PDF original para o novo PDF sem senha.
        novoArquivoPDF.add_page(pagina)

    # Define o nome do novo arquivo PDF que será criado sem a senha.
    novo_arquivo_sem_senha = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Desprotegido_Arquivo_Alterado_Mercado_Livre.pdf"

    # Abre um novo arquivo para gravação no modo binário ('wb').
    with open(novo_arquivo_sem_senha, "wb") as dadosArquivo:
        
        # Escreve o conteúdo do 'novoArquivoPDF' no arquivo físico.
        # Isso cria o arquivo PDF no sistema de arquivos com as páginas e sem a senha.
        novoArquivoPDF.write(dadosArquivo)

    # Imprime uma mensagem indicando que o processo foi concluído.
    print("Arquivo PDF desprotegido criado com sucesso!")

except FileNotFoundError:
    
    # Captura a exceção se o arquivo PDF original não for encontrado e imprime uma mensagem de erro.
    print("Arquivo PDF protegido por senha não encontrado. Verifique o caminho do arquivo.")
    
except Exception as e:
    
    # Captura outras exceções genéricas e imprime uma mensagem de erro.
    print(f"Ocorreu um erro: {e}")
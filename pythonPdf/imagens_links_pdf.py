#Pegar todas as imagens de um arquivo PDF e salvar no computador

# Importa as bibliotecas necessárias: pikepdf para manipulação 
# de PDFs e pathlib para manipulação de caminhos de arquivos
from pikepdf import Pdf, PdfImage
from pathlib import Path

# Define o caminho do arquivo PDF que será processado
caminhoArquivo = "C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\Evolução_Amazon.pdf"

# Abre o arquivo PDF especificado para leitura
arquivoPDF = Pdf.open(caminhoArquivo)

# Cria um objeto Path para o diretório onde as imagens serão salvas
pastaImagens = Path("C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\imagens\\Imagens_PDF")

# Cria o diretório especificado se ele ainda não existir
# 'exist_ok=True' impede que um erro seja gerado se o diretório já existir
pastaImagens.mkdir(exist_ok=True)

# Inicializa um contador para nomear as imagens de forma única
contador = 0

# Itera sobre todas as páginas do arquivo PDF
# 'enumerate' fornece um contador 'i' que representa o número da página atual
for i, pagina in enumerate(arquivoPDF.pages):
    
    # Itera sobre todos os itens de imagem encontrados na página atual
    for nome, imagem in pagina.images.items():
        
        # Cria um objeto PdfImage a partir da imagem extraída
        imagemCapturada = PdfImage(imagem)

        # Define o caminho completo do arquivo onde a imagem será salva
        # Usa o contador para garantir um nome de arquivo único para cada imagem
        caminhoImagem = pastaImagens / f"imagem_{contador}.jpg"

        # Extrai a imagem para o arquivo especificado
        # 'fileprefix=str(caminhoImagem)' define o caminho completo do arquivo de destino
        imagemCapturada.extract_to(fileprefix=str(caminhoImagem))

        # Incrementa o contador após salvar cada imagem
        contador += 1

# Imprime uma mensagem após todas as imagens serem salvas com sucesso
print("Imagens salvas com sucesso!")


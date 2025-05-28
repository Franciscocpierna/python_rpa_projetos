# Pega todos os Hyperlinks de um arquivo

from PyPDF2 import PdfReader

# Utiliza a classe 'PdfReader' para abrir e ler o arquivo PDF especificado.
# 'PdfReader' é uma classe do PyPDF2 que facilita a leitura de informações de arquivos PDF.
pdf = PdfReader("C:\\python_projetos\\python_rpa_projetos\\pythonPdf\\imagens\\ProfessoraRosiane.pdf")

# Inicializa uma lista chamada 'urls' que armazenará as URLs encontradas no PDF.
urls = []

# Inicia um loop que percorrerá todas as páginas do PDF.
# 'len(pdf.pages)' retorna o número total de páginas no arquivo PDF.
# 'range(len(pdf.pages))' cria uma sequência de números, cada um representando o índice de uma página no PDF.
for pagina in range(len(pdf.pages)):
    
    # Acessa a página atual do PDF usando seu índice.
    # 'pdf.pages[pagina]' obtém o objeto de página correspondente ao índice 'pagina'.
    paginaSelecionada = pdf.pages[pagina]

    # Tratamento de exceções para lidar com a possibilidade de uma página não conter anotações.
    try:
        
        # Verifica se há anotações na página atual e itera sobre elas.
        # 'paginaSelecionada.get('/Annots', [])' tenta obter a lista de anotações da página.
        # Se não houver anotações, retorna uma lista vazia para evitar erros.
        for url in paginaSelecionada.get('/Annots', []):
            
            # Converte o objeto de anotação (potencialmente uma URL) em uma string.
            # Isso permite verificar se contém uma URL.
            texto = str(url)
            
            # Verifica se a string ".com" está presente no texto da anotação.
            # A presença de ".com" pode indicar uma URL.
            if ".com" in texto:
                
                # Se ".com" for encontrado, tenta extrair a URL propriamente dita da anotação.
                # 'url.get('/A', {}).get('/URI', '')' tenta obter o atributo '/URI' da anotação,
                # que contém a URL. Se '/A' ou '/URI' não existirem, retorna uma string vazia.
                urls.append(url.get('/A', {}).get('/URI', ''))
                
                # Imprime a lista de URLs coletadas até o momento.
                print(urls)
        
    except KeyError:
        
        # Se uma chave necessária (como '/Annots' ou '/A') não for encontrada em uma anotação,
        # a exceção KeyError é capturada e o loop continua para a próxima anotação ou página.
        # Isso previne que o programa pare por causa de uma página sem anotações.
        pass

# Imprime uma mensagem ao finalizar a busca por URLs em todas as páginas do PDF.
print("Pronto!")
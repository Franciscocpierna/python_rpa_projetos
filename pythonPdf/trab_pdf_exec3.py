# Importa a classe 'PdfReader' da biblioteca 'PyPDF2' e o módulo 'datetime'.
# 'PdfReader' é usado para ler arquivos PDF e 'datetime' para manipulação de datas e horas.
from PyPDF2 import PdfReader
import datetime

# Bloco 'try' para tentar executar as operações a seguir e capturar exceções, se houver.
try:
    

    # Cria um objeto 'arquivoPDF' usando 'PdfReader' para abrir e ler o arquivo "Mercado_Livre.pdf".
    # Isso levanta uma exceção 'FileNotFoundError' se o arquivo não for encontrado.
    arquivoPDF = PdfReader("Mercado_Livre.pdf")

    # A variável 'dados' armazena os metadados do arquivo PDF.
    # Os metadados podem incluir informações como autor, criador, produtor, etc.
    dados = arquivoPDF.metadata

    # Calcula o número total de páginas do PDF e armazena na variável 'num_paginas'.
    num_paginas = len(arquivoPDF.pages)

    # Imprime os metadados básicos do PDF. Se um metadado específico não estiver presente, imprime "Não disponível".
    # Esta seção do código é responsável por acessar e exibir os metadados do arquivo PDF.

    # Aqui, o código tenta imprimir o metadado 'autor' do documento.
    # 'dados.author' acessa o valor do campo 'author' nos metadados do PDF.
    # Se 'dados.author' existir (ou seja, se o documento PDF tiver um autor definido nos metadados), ele será impresso.
    # Se 'dados.author' for 'None' (ou seja, se o autor não estiver definido nos metadados), o código imprime "Não disponível".
    print("Autor:", dados.author if dados.author else "Não disponível")
    
    # Este comando imprime o valor do metadado 'creator'.
    # 'dados.creator' acessa o campo 'creator' nos metadados, que geralmente contém informações sobre o software ou a pessoa que criou o documento PDF.
    # Se esse campo estiver presente nos metadados, ele será impresso; caso contrário, será exibido "Não disponível".
    print("Criador:", dados.creator if dados.creator else "Não disponível")
    
    # Aqui, o código tenta imprimir o metadado 'producer'.
    # 'dados.producer' acessa o campo 'producer' nos metadados, que geralmente indica o software usado para converter ou produzir o documento PDF.
    # Novamente, se este campo existir nos metadados, seu valor é impresso; se não, o código exibe "Não disponível".
    print("Produtor:", dados.producer if dados.producer else "Não disponível")
    
    # Este comando imprime o metadado 'subject'.
    # 'dados.subject' refere-se ao campo 'subject' nos metadados do PDF, que deve descrever o assunto ou o conteúdo do documento.
    # Se o documento tiver um assunto definido nos metadados, ele será impresso; se não, o código exibe "Não disponível".
    print("Assunto:", dados.subject if dados.subject else "Não disponível")
    
    # Finalmente, este comando imprime o metadado 'title'.
    # 'dados.title' acessa o campo 'title' nos metadados, que contém o título do documento PDF.
    # Se o documento tiver um título definido nos metadados, ele será impresso; caso contrário, será exibido "Não disponível".
    print("Título:", dados.title if dados.title else "Não disponível")
    

    # Em cada um desses comandos de impressão, uma expressão condicional (if-else) é usada.
    # Esta expressão verifica se o metadado específico existe e tem um valor.
    # Se o valor estiver presente, ele é impresso. Se não, a expressão retorna "Não disponível" e isso é impresso.


    # Imprime o número total de páginas do documento.
    print(f"Número total de páginas: {num_paginas}")

    # Verifica se o documento está criptografado e imprime "Sim" ou "Não".
    print("Documento Criptografado:", "Sim" if arquivoPDF.is_encrypted else "Não")

    # Tenta obter as datas de criação e modificação do documento dos metadados.
    # Se não estiverem disponíveis, define como "Não disponível".
    data_criacao = dados.get("/CreationDate", "Não disponível")
    data_modificacao = dados.get("/ModDate", "Não disponível")

    # Verifica e formata a data de criação, se disponível.
    # A data é extraída dos metadados e convertida para um formato legível.
    if data_criacao != "Não disponível":
        
        # Formata a data de criação do formato PDF para um objeto 'datetime'.
        data_criacao = datetime.datetime.strptime(data_criacao[2:-7], '%Y%m%d%H%M%S')
        print("Data de Criação:", data_criacao)
        
    else:
        print("Data de Criação: Não disponível")

    # Verifica e formata a data de modificação, se disponível.
    if data_modificacao != "Não disponível":
        
        # Formata a data de modificação do formato PDF para um objeto 'datetime'.
        data_modificacao = datetime.datetime.strptime(data_modificacao[2:-7], '%Y%m%d%H%M%S')
        print("Data de Modificação:", data_modificacao)
        
    else:
        
        print("Data de Modificação: Não disponível")

except FileNotFoundError:
    
    # Captura e imprime uma mensagem se o arquivo PDF não for encontrado.
    print("Arquivo PDF não encontrado. Verifique o caminho do arquivo.")
    
except Exception as e:
    
    # Captura e imprime uma mensagem para qualquer outra exceção que possa ocorrer.
    print(f"Ocorreu um erro: {e}")
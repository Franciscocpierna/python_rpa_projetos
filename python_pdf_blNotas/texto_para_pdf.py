#Converter um arquivo de texto para um arquivo pdf

from fpdf import FPDF

#Salva com o auxilio da classe FPDF
pdf = FPDF()

#Adiciono uma nova página em branco ao arquivo PDF
pdf.add_page()

#Definindo estilo e tamanho da fonte / letra / texto
pdf.set_font("Arial", size = 12)

#Abre o arquivo de texto no modo de leitura
arquivo = open('C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\ProfessoraRosiane.txt', 'r')

#w = Largura da célula
w = 0

#h = Altura da célula
h = 0

for linha in arquivo:
    
    #txt - Texto para imprimir. Valor padrão: String
    #border - Indica se as bordas devem ser desenhadas ao redor da célula
    #0 - Não tem borda
    #1 - Frame
    
    #ln - Indica onde a posição inicial deve ir após abrir o arquivo
    #0 - Para direita
    #1 - Para o inicio da próxima
    #2 - Abaixo
    
    
    #align - Permite o alinhamento da célula
    #L - Alinhamento a esquerda
    #C - Centro
    #R - Alinhar a direita
    
    #fill - Indica se o fundo da célula deve ser pintado pintado (true) ou transparente  (false)
    pdf.cell(w, h = 10, txt = linha, border = 1, ln = 1,
            align = 'L', fill = False, link = 'https://www.google.com/')
    
pdf.output("C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\ProfessoraRosiane.pdf")
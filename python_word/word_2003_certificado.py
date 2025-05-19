
import win32com.client

# Caminho do arquivo modelo .doc
caminho_modelo = r"C:\python_projetos\python_rpa_projetos\python_word\Certificado1.doc"
# Caminho do novo certificado .doc
caminho_saida = r"C:\python_projetos\python_rpa_projetos\python_word\Amanda Batista Alves.doc"

# Abre o Word
word = win32com.client.Dispatch("Word.Application")
word.Visible = False  # Não mostrar o Word

# Abre o documento modelo
doc = word.Documents.Open(caminho_modelo)
# Apaga todos os parágrafos (linhas) do documento
#doc.Content.Delete()
#doc.PageSetup.TopMargin = 0  # ajuste o valor conforme necessário

# Substitui o marcador @nome pelo nome desejado
'''find = doc.Content.Find essas linhas não fez a troca
find.Text = "@nome"
find.Replacement.Text = "Amanda Batista Alves"
find.MatchCase = False  # Ignora maiúsculas/minúsculas
find.MatchWholeWord = False  # Permite encontrar @nome junto de outros caracteres
'''
for paragrafo in doc.Paragraphs:
    if "@nome" in paragrafo.Range.Text:
        paragrafo.Range.Text = paragrafo.Range.Text.replace("@nome", "Amanda Batista Alves")


# Aqui, como exemplo, altera toda a fonte do documento:
doc.Content.Font.Name = "Calibri"
doc.Content.Font.Size = 24

# Salva como .doc (Word 2003)
doc.SaveAs(caminho_saida, FileFormat=0)
#essas linhas são para exibir o texto de cada linha/parágrafo
# for paragrafo in doc.Paragraphs:
#     texto = paragrafo.Range.Text
#     print(texto)  # Exibe o texto de cada linha/parágrafo

doc.Close()
word.Quit()

print("Certificado gerado em formato Word 2003 (.doc) com sucesso!")





'''

import win32com.client

# Caminho do arquivo .docx
caminho_docx = r"C:\python_projetos\python_rpa_projetos\python_word\Amanda Batista Alves.docx"
# Caminho do novo arquivo .doc
caminho_doc = r"C:\python_projetos\python_rpa_projetos\python_word\Amanda Batista Alves.doc"

# Abre o Word
word = win32com.client.Dispatch("Word.Application")
doc = word.Documents.Open(caminho_docx)

# Salva como .doc (formato 0)
doc.SaveAs(caminho_doc, FileFormat=0)
doc.Close()
word.Quit()

print("Arquivo convertido para .doc com sucesso!")

'''

'''

import win32com.client

#Abrindo o arquivo do Word
arquivoWord = Document("C:\\python_projetos\\python_rpa_projetos\\python_word\\word_certificado.py\\Certificado1.doc")

#Configurando os estilos
estilo = arquivoWord.styles["Normal"]

#for = para
for paragrafo in arquivoWord.paragraphs:
    #if = se
    if "@nome" in paragrafo.text:
        paragrafo.text = "Amanda Batista Alves"
        fonte = estilo.font
        fonte.name = "Calibri (Corpo)"
        fonte.size = Pt(24)
        

#Salva o certificado com o nome do aluno
arquivoWord.save("Amanda Batista Alves.docx")

print("Certificado gerado com sucesso!")


'''
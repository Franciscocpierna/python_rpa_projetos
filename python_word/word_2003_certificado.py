
import win32com.client

# Caminho do arquivo modelo .doc
caminho_modelo = r"C:\\python_projetos\\python_rpa_projetos\\python_word\\Certificado1.doc"
# Caminho do novo certificado .doc
caminho_saida = r"C:\\python_projetos\\python_rpa_projetos\\python_word\\Amanda Batista Alves.doc"

# Abre o Word
word = win32com.client.Dispatch("Word.Application")
word.Visible = False  # Não mostrar o Word

# Abre o documento modelo
doc = word.Documents.Open(caminho_modelo)
# Apaga todos os parágrafos (linhas) do documento
#doc.Content.Delete()
#doc.PageSetup.TopMargin = 0  # ajuste o valor conforme necessário

# Substitui o marcador @nome pelo nome desejado find não funcionou
'''find = doc.Content.Find essas linhas não fez a troca
find.Text = "@nome"
find.Replacement.Text = "Amanda Batista Alves"
find.MatchCase = False  # Ignora maiúsculas/minúsculas
find.MatchWholeWord = False  # Permite encontrar @nome junto de outros caracteres
'''
#find substituido por for
# Aqui, como exemplo, altera o texto do parágrafo que contém "@nome"
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






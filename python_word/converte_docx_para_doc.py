
import win32com.client

# Caminho do arquivo .docx
caminho_docx = r"C:\python_projetos\python_rpa_projetos\python_word\Certificado2.docx"
# Caminho do novo arquivo .doc
caminho_doc = r"C:\python_projetos\python_rpa_projetos\python_word\Certificado2.doc"

# Abre o Word
word = win32com.client.Dispatch("Word.Application")
doc = word.Documents.Open(caminho_docx)

# Salva como .doc (formato 0)
doc.SaveAs(caminho_doc, FileFormat=0)
doc.Close()
word.Quit()

print("Arquivo convertido para .doc com sucesso!")

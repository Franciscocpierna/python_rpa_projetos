#busca cep não funcionou prof passou a solução com api com requests

# Importações necessárias
import requests
from tkinter import *
from tkinter import messagebox
 
# Criar a janela principal
janela = Tk()
janela.geometry("1050x850")
janela.title("Consulta de Endereço por CEP")
 
# Label e campo de entrada do CEP
instrucao = Label(text="CEP: ", font="Arial 40")
instrucao.grid(row=1, column=0, sticky="W")
 
campoDigitavelCEP = Entry(font="Arial 40")
campoDigitavelCEP.grid(row=1, column=1, sticky="W")
 
# Função que consulta a API ViaCEP
def pesquisaCEP():
 
    # Obtem o CEP digitado e remove espaços
    cep = campoDigitavelCEP.get().strip().replace("-", "")
 
    # Verifica se o CEP tem 8 dígitos
    if not cep.isdigit() or len(cep) != 8:
        messagebox.showerror("Erro", "CEP inválido. Digite 8 números.")
        return
 
    # Consulta a API do ViaCEP
    try:
 
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        dados = resposta.json()
 
        # Verifica se ocorreu erro na resposta
        if "erro" in dados:
            messagebox.showerror("Erro", "CEP não encontrado.")
            return
 
        # Atualiza os labels com os dados retornados
        lblRua.config(text=f"Rua: {dados.get('logradouro', '-')}")
        lblBairro.config(text=f"Bairro: {dados.get('bairro', '-')}")
        lblCidade.config(text=f"Cidade: {dados.get('localidade', '-')} - {dados.get('uf', '-')}")
        lblCEP.config(text=f"CEP: {dados.get('cep', '-')}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
 
# Botão de pesquisar
botaoPesquisar = Button(text="Pesquisar", font="Arial 40", command=pesquisaCEP)
botaoPesquisar.grid(row=2, column=0, columnspan=2, sticky="NSEW")
 
# Labels de exibição dos resultados
lblRua = Label(text="\nRua: -", font="Arial 40")
lblRua.grid(row=3, column=0, columnspan=2, sticky="NSEW")
 
lblBairro = Label(text="Bairro: -", font="Arial 40")
lblBairro.grid(row=4, column=0, columnspan=2, sticky="NSEW")
 
lblCidade = Label(text="Cidade: -", font="Arial 40")
lblCidade.grid(row=5, column=0, columnspan=2, sticky="NSEW")
 
lblCEP = Label(text="CEP: -", font="Arial 40")
lblCEP.grid(row=6, column=0, columnspan=2, sticky="NSEW")
 
# Executar o aplicativo
janela.mainloop()


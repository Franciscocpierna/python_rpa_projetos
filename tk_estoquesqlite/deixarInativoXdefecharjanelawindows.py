def grafico_tela():
    root1 = tk.Toplevel()
    root1.title("Gráfico de Inclusões por Mês")
    root1.geometry("800x600")
    root1.grab_set()

    # Função centralizada para fechar com segurança (pelo seu botão/menu Sair)
    def fechar_janela():
        plt.close('all')  # Limpa o matplotlib
        # conn.close()  # Fecha o banco se necessário
        root1.destroy()   # Destrói a janela de vez

    # 1. TRUQUE PARA O "X": Uma função vazia que não faz nada!
    def desativar_x():
        pass  # O usuário clica no X, mas o Python ignora e a janela continua aberta

    # 2. Atrela essa função vazia ao protocolo do "X"
    root1.protocol("WM_DELETE_WINDOW", desativar_x)

    # 3. Cria o seu próprio botão ou menu "Sair" que realmente fecha a janela
    btn_sair = ttk.Button(root1, text="Sair / Fechar", command=fechar_janela)
    btn_sair.pack(pady=10)

    # ... restante do seu código (combobox, frames, gráficos) ...
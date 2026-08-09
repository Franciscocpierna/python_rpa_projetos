import tkinter as tk

# 1. Cria a janela principal da aplicação
root = tk.Tk()
root.title("Validação de Campos Diferentes")
root.geometry("350x250")

# 2. Define a função para validar a Data (formato DD/MM/AAAA)
def validar_data(P):
    if P == "":
        return True
    if len(P) > 10:
        return False
    for i, c in enumerate(P):
        if i == 2 or i == 5:
            if c != '/':
                return False
        else:
            if not c.isdigit():
                return False
    return True

# 3. Define a função para validar apenas Números Inteiros (ex: quantidade, ID)
def validar_apenas_numeros(P):
    if P == "":
        return True
    # Verifica se todos os caracteres digitados são números
    return all(c.isdigit() for c in P)

# 4. Registra cada função separadamente no motor do Tkinter
vcmd_data = root.register(validar_data)
vcmd_numero = root.register(validar_apenas_numeros)

# --- PRIMEIRO CAMPO: Data (Usa o validador de data) ---
tk.Label(root, text="Data de Vencimento:", font=("Arial", 10)).pack(pady=(15, 0))
entry_data = tk.Entry(root, validate="key", validatecommand=(vcmd_data, '%P'), font=("Arial", 12))
entry_data.pack(pady=5)
entry_data.insert(0, "DD/MM/AAAA")

# --- SEGUNDO CAMPO: Número (Usa o validador numérico) ---
tk.Label(root, text="Quantidade de Produtos:", font=("Arial", 10)).pack(pady=(10, 0))
entry_qtd = tk.Entry(root, validate="key", validatecommand=(vcmd_numero, '%P'), font=("Arial", 12))
entry_qtd.pack(pady=5)

# 5. Inicia o loop principal da interface gráfica
root.mainloop()
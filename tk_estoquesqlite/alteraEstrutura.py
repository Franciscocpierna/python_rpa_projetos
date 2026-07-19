import sqlite3
from tkinter import messagebox

# --- Banco de Dados ---
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

def atualizar_estrutura_banco():
    try:
        # Verifica se a coluna já existe para evitar erro de "duplicate column"
        cursor.execute("PRAGMA table_info(produtos)")
        colunas = [info[1] for info in cursor.fetchall()]
        
        if 'data_inclusao' not in colunas:
            if messagebox.askyesno("Confirmar", "A coluna 'data_inclusao' não existe. Deseja adicioná-la?"):
                # 1. Adiciona a coluna permitindo valores nulos (ou com um valor padrão estático)
                cursor.execute("ALTER TABLE produtos ADD COLUMN data_inclusao DATE")
                conn.commit() # Salva a primeira alteração
                # 2. Atualiza as linhas antigas com a data de hoje (ou qualquer data padrão)
                cursor.execute("UPDATE produtos SET data_inclusao = DATE('now')")
                conn.commit()

                messagebox.showinfo("Sucesso", "Estrutura atualizada com sucesso!")
        else:
            print("A coluna já existe.")
            
    except sqlite3.OperationalError as e:
        messagebox.showerror("Erro ao mudar estrutura", f"Erro no banco de dados: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")

# Executa a função
atualizar_estrutura_banco()

conn.close()
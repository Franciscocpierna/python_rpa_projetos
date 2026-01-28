import tkinter as tk
from tkinter import messagebox
import random

class LotofacilApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conferidor Lotofácil - Resultado Detalhado")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f2f5")

        # Estados dos jogos
        self.meu_jogo = set()
        self.resultado_oficial = set()

        # Estilização
        self.font_title = ("Segoe UI", 12, "bold")
        self.font_num = ("Segoe UI", 10, "bold")
        
        self.create_widgets()

    def create_widgets(self):
        # Header
        header = tk.Frame(self.root, bg="#1a2a6c", pady=15)
        header.pack(fill="x")
        tk.Label(header, text="CONFERIDOR DE ACERTOS LOTOFÁCIL", font=("Segoe UI", 18, "bold"), 
                 bg="#1a2a6c", fg="white").pack()

        # Container Principal
        main_container = tk.Frame(self.root, bg="#f0f2f5")
        main_container.pack(expand=True, fill="both", padx=20, pady=10)

        # --- FRAME 1: MEU JOGO (ESQUERDA) ---
        col1 = tk.Frame(main_container, bg="#f0f2f5")
        col1.grid(row=0, column=0, padx=10, sticky="n")

        self.frame_meu_jogo = tk.LabelFrame(col1, text=" 📝 SEU JOGO ", font=self.font_title, bg="white", padx=10, pady=10)
        self.frame_meu_jogo.pack()
        self.botoes_meu_jogo = self.create_grid(self.frame_meu_jogo, self.meu_jogo, "#3498db")

        tk.Button(col1, text="APAGAR MEU JOGO", command=lambda: self.limpar_especifico('meu'),
                  bg="#e67e22", fg="white", font=("Segoe UI", 9, "bold"), relief="flat", pady=5).pack(fill="x", pady=5)

        # --- FRAME 2: RESULTADO (CENTRO) ---
        col2 = tk.Frame(main_container, bg="#f0f2f5")
        col2.grid(row=0, column=1, padx=10, sticky="n")

        self.frame_resultado = tk.LabelFrame(col2, text=" 🎲 RESULTADO OFICIAL ", font=self.font_title, bg="white", padx=10, pady=10)
        self.frame_resultado.pack()
        self.botoes_resultado = self.create_grid(self.frame_resultado, self.resultado_oficial, "#e74c3c")

        tk.Button(col2, text="APAGAR RESULTADO", command=lambda: self.limpar_especifico('res'),
                  bg="#e67e22", fg="white", font=("Segoe UI", 9, "bold"), relief="flat", pady=5).pack(fill="x", pady=5)

        # --- FRAME 3: NÚMEROS ACERTADOS (DIREITA) ---
        col3 = tk.Frame(main_container, bg="#f0f2f5")
        col3.grid(row=0, column=2, padx=10, sticky="n")

        self.frame_acertos = tk.LabelFrame(col3, text=" ✅ NÚMEROS ACERTADOS ", font=self.font_title, 
                                          bg="#ffffff", padx=10, pady=10, fg="#27ae60", width=250, height=330)
        self.frame_acertos.pack_propagate(False) # Mantém o tamanho fixo
        self.frame_acertos.pack()

        self.label_lista_acertos = tk.Label(self.frame_acertos, text="Aguardando\nconferência...", 
                                           font=("Segoe UI", 11), bg="white", fg="#7f8c8d", justify="left")
        self.label_lista_acertos.pack(expand=True)

        self.label_total = tk.Label(col3, text="Total: 0", font=("Segoe UI", 14, "bold"), bg="#f0f2f5")
        self.label_total.pack(pady=10)

        # --- BOTÃO CONFERIR (INFERIOR) ---
        self.btn_comparar = tk.Button(self.root, text="CONFERIR ACERTOS", command=self.conferir,
                                font=("Segoe UI", 16, "bold"), bg="#27ae60", fg="white",
                                relief="flat", padx=50, pady=15, cursor="hand2")
        self.btn_comparar.pack(pady=20)

    def create_grid(self, parent, conjunto, active_color):
        buttons = {}
        for i in range(1, 26):
            row = (i-1) // 5
            col = (i-1) % 5
            btn = tk.Button(parent, text=f"{i:02d}", width=4, height=2,
                           font=self.font_num, relief="flat", bg="#ecf0f1",
                           command=lambda n=i, c=conjunto, cl=active_color: self.toggle_number(n, c, cl))
            btn.grid(row=row, column=col, padx=3, pady=3)
            buttons[i] = btn
        return buttons

    def toggle_number(self, num, conjunto, color):
        if num in conjunto:
            conjunto.remove(num)
            self.update_button_style(num, conjunto, color, deselect=True)
        else:
            if len(conjunto) >= 15:
                return 
            conjunto.add(num)
            self.update_button_style(num, conjunto, color)
        
    def update_button_style(self, num, conjunto, color, deselect=False):
        btns = self.botoes_meu_jogo if conjunto == self.meu_jogo else self.botoes_resultado
        if deselect:
            btns[num].configure(bg="#ecf0f1", fg="black")
        else:
            btns[num].configure(bg=color, fg="white")

    def limpar_especifico(self, tipo):
        if tipo == 'meu':
            self.meu_jogo.clear()
            for btn in self.botoes_meu_jogo.values():
                btn.configure(bg="#ecf0f1", fg="black")
        else:
            self.resultado_oficial.clear()
            for btn in self.botoes_resultado.values():
                btn.configure(bg="#ecf0f1", fg="black")
        
        self.label_lista_acertos.config(text="Aguardando\nconferência...", fg="#7f8c8d")
        self.label_total.config(text="Total: 0")

    def conferir(self):
        if len(self.meu_jogo) < 15 or len(self.resultado_oficial) < 15:
            messagebox.showwarning("Atenção", "Selecione 15 números nos dois quadros.")
            return

        # Calcula a interseção (números que estão nos dois conjuntos)
        acertos = sorted(list(self.meu_jogo.intersection(self.resultado_oficial)))
        total_acertos = len(acertos)

        # Atualiza o Frame de Acertos
        if acertos:
            # Formata os números para mostrar um embaixo do outro ou em lista
            texto_acertos = "\n".join([f"Número: {n:02d}" for n in acertos])
            self.label_lista_acertos.config(text=texto_acertos, fg="#27ae60", font=("Segoe UI", 11, "bold"))
        else:
            self.label_lista_acertos.config(text="Nenhum número\nacertado.", fg="#c0392b")

        self.label_total.config(text=f"Total: {total_acertos}", fg="#27ae60" if total_acertos >= 11 else "black")

        # Pinta os botões no quadro "Seu Jogo" para facilitar a visualização
        for n in range(1, 26):
            if n in self.meu_jogo:
                if n in acertos:
                    self.botoes_meu_jogo[n].configure(bg="#2ecc71") # Verde para acerto
                else:
                    self.botoes_meu_jogo[n].configure(bg="#bdc3c7") # Cinza para erro

if __name__ == "__main__":
    root = tk.Tk()
    app = LotofacilApp(root)
    root.mainloop()
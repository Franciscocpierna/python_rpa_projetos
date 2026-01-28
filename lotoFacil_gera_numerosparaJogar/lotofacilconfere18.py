import tkinter as tk
from tkinter import messagebox

class Lotofacil18App:
    def __init__(self, root):
        self.root = root
        self.root.title("Conferidor Lotofácil - Aposta de 18 Números")
        self.root.geometry("1100x750")
        self.root.configure(bg="#f4f6f9")

        # Estados dos jogos
        self.meu_jogo = set()
        self.resultado_oficial = set()

        # Estilização
        self.font_title = ("Segoe UI", 12, "bold")
        self.font_num = ("Segoe UI", 10, "bold")
        
        self.create_widgets()

    def create_widgets(self):
        # Header
        header = tk.Frame(self.root, bg="#2c3e50", pady=20)
        header.pack(fill="x")
        tk.Label(header, text="CONFERIDOR LOTOFÁCIL (ATÉ 18 NÚMEROS)", font=("Segoe UI", 20, "bold"), 
                 bg="#2c3e50", fg="white").pack()

        # Container Principal
        main_container = tk.Frame(self.root, bg="#f4f6f9")
        main_container.pack(expand=True, fill="both", padx=20, pady=10)

        # --- FRAME 1: SEU JOGO (ATÉ 18 NÚMEROS) ---
        col1 = tk.Frame(main_container, bg="#f4f6f9")
        col1.grid(row=0, column=0, padx=10, sticky="n")

        self.frame_meu_jogo = tk.LabelFrame(col1, text=" 📝 SEU JOGO (Marque 18) ", 
                                           font=self.font_title, bg="white", padx=10, pady=10, fg="#2980b9")
        self.frame_meu_jogo.pack()
        self.botoes_meu_jogo = self.create_grid(self.frame_meu_jogo, self.meu_jogo, "#3498db", 18)

        tk.Button(col1, text="LIMPAR MEU JOGO", command=lambda: self.limpar_especifico('meu'),
                  bg="#e67e22", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", pady=8).pack(fill="x", pady=10)

        # --- FRAME 2: RESULTADO (15 NÚMEROS) ---
        col2 = tk.Frame(main_container, bg="#f4f6f9")
        col2.grid(row=0, column=1, padx=10, sticky="n")

        self.frame_resultado = tk.LabelFrame(col2, text=" 🎲 RESULTADO (Marque 15) ", 
                                            font=self.font_title, bg="white", padx=10, pady=10, fg="#c0392b")
        self.frame_resultado.pack()
        self.botoes_resultado = self.create_grid(self.frame_resultado, self.resultado_oficial, "#e74c3c", 15)

        tk.Button(col2, text="LIMPAR RESULTADO", command=lambda: self.limpar_especifico('res'),
                  bg="#e67e22", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", pady=8).pack(fill="x", pady=10)

        # --- FRAME 3: PAINEL DE ACERTOS ---
        col3 = tk.Frame(main_container, bg="#f4f6f9")
        col3.grid(row=0, column=2, padx=10, sticky="n")

        self.frame_acertos = tk.LabelFrame(col3, text=" ✅ NÚMEROS ACERTADOS ", font=self.font_title, 
                                          bg="#ffffff", padx=15, pady=15, fg="#27ae60", width=280, height=350)
        self.frame_acertos.pack_propagate(False)
        self.frame_acertos.pack()

        # Canvas e Scrollbar para caso a lista de acertos seja longa
        self.canvas_acertos = tk.Canvas(self.frame_acertos, bg="white", highlightthickness=0)
        self.scroll_y = tk.Scrollbar(self.frame_acertos, orient="vertical", command=self.canvas_acertos.yview)
        self.scroll_frame = tk.Frame(self.canvas_acertos, bg="white")

        self.canvas_acertos.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas_acertos.configure(yscrollcommand=self.scroll_y.set)

        self.canvas_acertos.pack(side="left", fill="both", expand=True)
        self.scroll_y.pack(side="right", fill="y")

        self.label_info_acertos = tk.Label(self.scroll_frame, text="Marque os números\ne clique em conferir.", 
                                          font=("Segoe UI", 10), bg="white", fg="#95a5a6", justify="left")
        self.label_info_acertos.pack(pady=10)

        self.label_total = tk.Label(col3, text="Acertos: 0", font=("Segoe UI", 16, "bold"), bg="#f4f6f9", pady=10)
        self.label_total.pack()

        # --- BOTÃO CONFERIR ---
        self.btn_comparar = tk.Button(self.root, text="CONFERIR RESULTADO", command=self.conferir,
                                font=("Segoe UI", 16, "bold"), bg="#27ae60", fg="white",
                                relief="flat", padx=60, pady=15, cursor="hand2")
        self.btn_comparar.pack(pady=20)

        # Status Bar
        self.status_var = tk.StringVar(value="Seu Jogo: 0/18 | Resultado: 0/15")
        tk.Label(self.root, textvariable=self.status_var, bd=1, relief="sunken", anchor="w").pack(fill="x", side="bottom")

    def create_grid(self, parent, conjunto, active_color, limite):
        buttons = {}
        for i in range(1, 26):
            row = (i-1) // 5
            col = (i-1) % 5
            btn = tk.Button(parent, text=f"{i:02d}", width=5, height=2,
                           font=self.font_num, relief="flat", bg="#ecf0f1",
                           command=lambda n=i, c=conjunto, cl=active_color, l=limite: self.toggle_number(n, c, cl, l))
            btn.grid(row=row, column=col, padx=4, pady=4)
            buttons[i] = btn
        return buttons

    def toggle_number(self, num, conjunto, color, limite):
        # Resetar cores de destaque ao clicar
        self.reset_visuals()

        if num in conjunto:
            conjunto.remove(num)
            self.update_button_style(num, conjunto, color, deselect=True)
        else:
            if len(conjunto) >= limite:
                messagebox.showwarning("Limite", f"Neste quadro o limite é de {limite} números.")
                return 
            conjunto.add(num)
            self.update_button_style(num, conjunto, color)
        
        self.status_var.set(f"Seu Jogo: {len(self.meu_jogo)}/18 | Resultado: {len(self.resultado_oficial)}/15")

    def update_button_style(self, num, conjunto, color, deselect=False):
        btns = self.botoes_meu_jogo if conjunto == self.meu_jogo else self.botoes_resultado
        if deselect:
            btns[num].configure(bg="#ecf0f1", fg="black")
        else:
            btns[num].configure(bg=color, fg="white")

    def reset_visuals(self):
        for i in range(1, 26):
            # Reset Meu Jogo
            color_m = "#3498db" if i in self.meu_jogo else "#ecf0f1"
            self.botoes_meu_jogo[i].configure(bg=color_m, fg="white" if i in self.meu_jogo else "black")
            # Reset Resultado
            color_r = "#e74c3c" if i in self.resultado_oficial else "#ecf0f1"
            self.botoes_resultado[i].configure(bg=color_r, fg="white" if i in self.resultado_oficial else "black")

    def limpar_especifico(self, tipo):
        if tipo == 'meu':
            self.meu_jogo.clear()
        else:
            self.resultado_oficial.clear()
        
        self.reset_visuals()
        self.label_info_acertos.config(text="Marque os números\ne clique em conferir.", fg="#95a5a6")
        self.label_total.config(text="Acertos: 0", fg="black")
        self.status_var.set(f"Seu Jogo: {len(self.meu_jogo)}/18 | Resultado: {len(self.resultado_oficial)}/15")

    def conferir(self):
        # Validação: aceita entre 15 e 18 no seu jogo, mas exige exatamente 15 no resultado
        if len(self.meu_jogo) < 15:
            messagebox.showwarning("Aviso", "Marque pelo menos 15 números no seu jogo.")
            return
        if len(self.resultado_oficial) != 15:
            messagebox.showwarning("Aviso", "O resultado oficial deve ter exatamente 15 números.")
            return

        acertos = sorted(list(self.meu_jogo.intersection(self.resultado_oficial)))
        qtd = len(acertos)

        # Atualiza a lista no Frame de Acertos
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        if acertos:
            for n in acertos:
                tk.Label(self.scroll_frame, text=f"⭐ Dezena: {n:02d}", font=("Segoe UI", 11, "bold"), 
                         bg="white", fg="#27ae60").pack(anchor="w", pady=2)
            self.canvas_acertos.configure(scrollregion=self.canvas_acertos.bbox("all"))
        else:
            tk.Label(self.scroll_frame, text="Nenhum acerto.", font=("Segoe UI", 11), bg="white", fg="#c0392b").pack()

        self.label_total.config(text=f"Acertos: {qtd}", fg="#27ae60" if qtd >= 11 else "#e67e22")

        # Destaque nos botões
        for n in range(1, 26):
            if n in self.meu_jogo:
                if n in acertos:
                    self.botoes_meu_jogo[n].configure(bg="#2ecc71") # Verde
                else:
                    self.botoes_meu_jogo[n].configure(bg="#bdc3c7") # Cinza

        # Mensagem final
        if qtd >= 11:
            messagebox.showinfo("Parabéns!", f"Você fez {qtd} pontos!\nConfira os números na lista ao lado.")
        else:
            messagebox.showinfo("Resultado", f"Você fez {qtd} pontos. Não foi dessa vez!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Lotofacil18App(root)
    root.mainloop()
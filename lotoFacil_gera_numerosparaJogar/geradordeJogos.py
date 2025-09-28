import tkinter as tk
from tkinter import messagebox
import random
import math
import itertools
from fpdf import FPDF
import os

# --- 1. CONFIGURAÇÕES GLOBAIS ---
MIN_ESCOLHAS = 15
MAX_ESCOLHAS = 25
NUMEROS_POR_JOGO = 15
ALTURA_CARTAO = 25 
ESPACAMENTO_VERTICAL = 10
ESPAÇAMENTO_HORIZONTAL = 10 
NUMERO_COLUNAS = 3 

class LotoFacilApp:
    def __init__(self, root):
        self.root = root
        root.title("Gerador de Jogos Lotofácil")
        root.geometry("600x650")

        self.numeros_escolhidos = set()
        self.checkbox_vars = {}
        self.botoes_numeros = {}

        self.criar_layout()

    # --- 2. CRIAÇÃO DA INTERFACE GRÁFICA ---

    def criar_layout(self):
        # Frame Principal para os Números
        frame_numeros = tk.LabelFrame(self.root, text="Escolha seus números (1 a 25)", padx=10, pady=10)
        frame_numeros.pack(pady=10, padx=10)

        # Cria os botões/checkboxes de 1 a 25
        for i in range(1, 26):
            var = tk.IntVar()
            chk = tk.Checkbutton(
                frame_numeros, 
                text=str(i).zfill(2), 
                variable=var, 
                width=4, 
                font=('Arial', 10, 'bold'),
                # A cada clique, chama a função que atualiza a contagem
                command=lambda num=i, var=var: self.atualizar_escolhas(num, var)
            )
            
            linha = (i - 1) // 5
            coluna = (i - 1) % 5
            chk.grid(row=linha, column=coluna, padx=3, pady=3, sticky="w")
            
            self.checkbox_vars[i] = var
            self.botoes_numeros[i] = chk

        # Frame para o Fechamento de Probabilidade
        frame_fechamento = tk.LabelFrame(self.root, text="Fechamento de Probabilidade", padx=10, pady=10)
        frame_fechamento.pack(pady=10, padx=10, fill="x")

        tk.Label(frame_fechamento, text="Probabilidade (%) (0 a 100):").pack(side=tk.LEFT, padx=5)
        self.entry_prob = tk.Entry(frame_fechamento, width=10, justify='center')
        self.entry_prob.insert(0, "10") # Valor inicial
        self.entry_prob.pack(side=tk.LEFT, padx=5)
        
        # Botão Gerar Jogos
        btn_gerar = tk.Button(self.root, text="Gerar Jogos e Salvar PDF", command=self.gerar_e_salvar_jogos, bg="green", fg="white", font=('Arial', 12, 'bold'))
        btn_gerar.pack(pady=20, ipadx=20, ipady=5)

        # Rótulo de Status (Este é o elemento que será atualizado)
        self.label_status = tk.Label(self.root, text=f"Escolha {MIN_ESCOLHAS} a {MAX_ESCOLHAS} números. (0/25) - SELECIONADOS: 0", fg="blue")
        self.label_status.pack(pady=10)


    def atualizar_escolhas(self, numero, var):
        """Adiciona/remove números e atualiza o rótulo de contagem."""
        if var.get() == 1:
            if len(self.numeros_escolhidos) < MAX_ESCOLHAS:
                self.numeros_escolhidos.add(numero)
            else:
                var.set(0)
                messagebox.showwarning("Limite Atingido", f"Você pode escolher no máximo {MAX_ESCOLHAS} números.")
        else:
            self.numeros_escolhidos.discard(numero)
        
        # --- AJUSTE FEITO AQUI ---
        contagem = len(self.numeros_escolhidos)
        self.label_status.config(
            text=f"Escolha {MIN_ESCOLHAS} a {MAX_ESCOLHAS} números. ({contagem}/25) - SELECIONADOS: {contagem}"
        )
        # --------------------------


    # --- (As funções de Geração e PDF permanecem inalteradas, focando no ajuste) ---
    def calcular_combinacoes(self, n, k):
        return math.comb(n, k)
    
    def gerar_jogos(self, probabilidade_alvo):
        
        escolhas = sorted(list(self.numeros_escolhidos))
        n = len(escolhas)
        
        if n < MIN_ESCOLHAS:
            messagebox.showerror("Erro de Seleção", f"Você deve escolher no mínimo {MIN_ESCOLHAS} números.")
            return []
        
        combinacoes_possiveis = self.calcular_combinacoes(n, NUMEROS_POR_JOGO)
        jogos_necessarios = math.ceil(combinacoes_possiveis * (probabilidade_alvo / 100))
        jogos_necessarios = min(jogos_necessarios, combinacoes_possiveis)
        
        self.label_status.config(text=f"Gerando {jogos_necessarios} jogos (de {combinacoes_possiveis} possíveis)...")

        jogos_gerados = set()
        
        if probabilidade_alvo == 100:
            jogos_gerados.update(itertools.combinations(escolhas, NUMEROS_POR_JOGO))
        else:
            while len(jogos_gerados) < jogos_necessarios:
                novo_jogo = tuple(sorted(random.sample(escolhas, NUMEROS_POR_JOGO)))
                jogos_gerados.add(novo_jogo)
                
        return sorted([list(jogo) for jogo in jogos_gerados])

    
    def gerar_e_salvar_jogos(self):
        try:
            probabilidade = float(self.entry_prob.get())
            if not (0 <= probabilidade <= 100):
                messagebox.showerror("Erro de Probabilidade", "A porcentagem deve ser entre 0 e 100.")
                return
        except ValueError:
            messagebox.showerror("Erro de Entrada", "A probabilidade deve ser um número válido.")
            return

        jogos = self.gerar_jogos(probabilidade)
        
        if jogos:
            self.gravar_pdf(jogos)
            messagebox.showinfo("Sucesso!", f"Total de {len(jogos)} jogos gerados e salvos em 'jogos_lotofacil.pdf'.")
            self.label_status.config(text=f"Arquivo gerado com {len(jogos)} cartões.")


    def gravar_pdf(self, jogos):
        """Gera um arquivo PDF com todos os jogos, com espaçamento HORIZONTAL de 50mm."""
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=16, style='B')
        
        pdf.cell(0, 10, txt="Gerador de Jogos Lotofácil", ln=True, align='C')
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 5, txt=f"Números Escolhidos ({len(self.numeros_escolhidos)}): {', '.join(map(str, sorted(list(self.numeros_escolhidos))))}", ln=True, align='C')
        pdf.cell(0, 10, txt=f"Fechamento: {self.entry_prob.get()}% - Total de Cartões: {len(jogos)}", ln=True, align='C')

        pdf.ln(5) 
        pdf.set_font("Arial", size=12)
        
        # CÁLCULO DO LAYOUT HORIZONTAL
        largura_util = pdf.w - (pdf.l_margin + pdf.r_margin)
        largura_total_espacos = ESPAÇAMENTO_HORIZONTAL * (NUMERO_COLUNAS - 1)
        largura_cartoes_disponivel = largura_util - largura_total_espacos
        col_width = largura_cartoes_disponivel / NUMERO_COLUNAS
        
        y_start = pdf.get_y()
        col = 0
        
        for i, jogo in enumerate(jogos):
            
            pos_x = pdf.l_margin + (col * col_width) + (col * ESPAÇAMENTO_HORIZONTAL)

            if col == NUMERO_COLUNAS: 
                col = 0
                y_start += (ALTURA_CARTAO + ESPACAMENTO_VERTICAL)
                pos_x = pdf.l_margin
            
            if y_start > pdf.h - 30: 
                 pdf.add_page()
                 y_start = 15 
                 pos_x = pdf.l_margin

            # Desenho do Cartão
            pdf.set_xy(pos_x, y_start)
            pdf.set_fill_color(240, 240, 240)
            pdf.rect(pos_x, y_start, col_width, ALTURA_CARTAO, 'F')
            
            pdf.set_text_color(0, 0, 0)
            pdf.set_font("Arial", size=10, style='B')
            pdf.set_xy(pos_x, y_start + 2)
            pdf.cell(col_width, 5, txt=f"Cartão {i+1}", align='C')
            
            pdf.set_font("Arial", size=10)
            pdf.set_xy(pos_x, y_start + 8)
            pdf.multi_cell(col_width, 4, txt=f"{', '.join(map(str, jogo))}", align='C')
            
            col += 1

        output_file = "jogos_lotofacil.pdf"
        pdf.output(output_file)


# --- INICIALIZAÇÃO ---

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = LotoFacilApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Erro Crítico", f"Ocorreu um erro no programa: {e}")
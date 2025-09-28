import tkinter as tk
from tkinter import messagebox
import random
import math
import itertools
from fpdf import FPDF # Importa a classe FPDF

# --- 1. CONFIGURAÇÕES GLOBAIS ---
MIN_ESCOLHAS = 15
MAX_ESCOLHAS = 25 
NUMEROS_POR_JOGO = 15
ALTURA_CARTAO = 25 
ESPACAMENTO_VERTICAL = 10
# CORREÇÃO: Variável padronizada
ESPAÇAMENTO_HORIZONTAL = 10  
NUMERO_COLUNAS = 3 

# MATRIZES DE FECHAMENTO CONHECIDAS E MINIMIZADAS (11/15)
FECHAMENTO_11 = {
    16: 2,   
    17: 4,
    18: 5,
}

# Limite de segurança para o Fechamento Completo
LIMITE_JOGOS_SEGURANCA = 2000 


class LotoFacilApp:
    def __init__(self, root):
        self.root = root
        root.title("Gerador de Jogos Lotofácil (FECHAMENTO 11 OTIMIZADO)")
        root.geometry("650x750")

        self.numeros_escolhidos = set()
        self.checkbox_vars = {}
        self.botoes_numeros = {}
        
        self.acerto_alvo = tk.IntVar(value=11) 

        self.criar_layout()

    # --- 2. CRIAÇÃO DA INTERFACE GRÁFICA ---

    def criar_layout(self):
        # Frame Principal para os Números
        frame_numeros = tk.LabelFrame(self.root, text="Escolha seus números (15 a 25)", padx=10, pady=10)
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
                command=lambda num=i, var=var: self.atualizar_escolhas(num, var)
            )
            
            linha = (i - 1) // 5
            coluna = (i - 1) % 5
            chk.grid(row=linha, column=coluna, padx=3, pady=3, sticky="w")
            
            self.checkbox_vars[i] = var
            self.botoes_numeros[i] = chk

        # --- Frame para o Acerto Alvo (Seleção de Objetivo) ---
        frame_fechamento = tk.LabelFrame(self.root, text="Selecione o Acerto Alvo", padx=10, pady=10)
        frame_fechamento.pack(pady=10, padx=10, fill="x")

        acertos = [11, 12, 13, 14, 15] 
        tk.Label(frame_fechamento, text="Acerto Alvo:").pack(side=tk.LEFT, padx=5)

        for acerto in acertos:
            tk.Radiobutton(
                frame_fechamento,
                text=str(acerto),
                variable=self.acerto_alvo,
                value=acerto,
                command=lambda: self.atualizar_custo_combinacao(len(self.numeros_escolhidos))
            ).pack(side=tk.LEFT, padx=5)
        
        # Campo para mostrar o total de combinações
        self.label_cartoes_necessarios = tk.Label(frame_fechamento, text="Cartões Gerados: 0", fg="blue", font=('Arial', 11, 'bold'))
        self.label_cartoes_necessarios.pack(pady=5)
        
        # Rótulo de ALERTA DE CUSTO
        tk.Label(self.root, text="AVISO: Somente o acerto 11 é otimizado para 16, 17 e 18 números.", fg="red", font=('Arial', 10, 'bold')).pack(pady=5)

        # Botão Gerar Jogos
        btn_gerar = tk.Button(self.root, text="GERAR JOGOS GARANTIDOS e Salvar PDF", command=self.gerar_e_salvar_jogos, bg="red", fg="white", font=('Arial', 12, 'bold'))
        btn_gerar.pack(pady=20, ipadx=20, ipady=5)

        # Rótulo de Status
        self.label_status = tk.Label(self.root, text=f"Escolha {MIN_ESCOLHAS} a {MAX_ESCOLHAS} números. (0/25) - SELECIONADOS: 0", fg="blue")
        self.label_status.pack(pady=10)


    def atualizar_escolhas(self, numero, var):
        """Adiciona/remove números e atualiza o rótulo de contagem e o custo."""
        if var.get() == 1:
            if len(self.numeros_escolhidos) < MAX_ESCOLHAS:
                self.numeros_escolhidos.add(numero)
            else:
                var.set(0)
                messagebox.showwarning("Limite Atingido", f"Você pode escolher no máximo {MAX_ESCOLHAS} números.")
        else:
            self.numeros_escolhidos.discard(numero)
        
        contagem = len(self.numeros_escolhidos)
        
        self.label_status.config(
            text=f"Escolha {MIN_ESCOLHAS} a {MAX_ESCOLHAS} números. ({contagem}/25) - SELECIONADOS: {contagem}"
        )
        self.atualizar_custo_combinacao(contagem)

    def calcular_combinacoes(self, n, k):
        """Calcula o total de combinações possíveis (n escolhe k)."""
        return math.comb(n, k)
        
    def atualizar_custo_combinacao(self, n_escolhidos):
        """Atualiza o rótulo com o número de cartões para a Combinação Plena ou Otimizada."""
        
        if n_escolhidos < MIN_ESCOLHAS:
            self.label_cartoes_necessarios.config(text="Cartões Gerados: 0", fg="blue")
            return
            
        acerto_alvo = self.acerto_alvo.get()
        num_cartoes = 0
        tipo_fechamento = "Completo (Garante 15)"
        cor = "red" 

        if acerto_alvo == 11 and n_escolhidos in FECHAMENTO_11:
            # --- FECHAMENTO OTIMIZADO PARA 11 ACERTOS ---
            num_cartoes = FECHAMENTO_11[n_escolhidos]
            tipo_fechamento = f"Otimizado (Garante 11)"
            cor = "green" if num_cartoes <= 50 else "blue"
        else:
            # --- FECHAMENTO COMPLETO (Padrão para outros acertos ou escolhas) ---
            num_cartoes = self.calcular_combinacoes(n_escolhidos, NUMEROS_POR_JOGO)
            tipo_fechamento = f"Completo (Garante 15)"
            if num_cartoes <= 500:
                cor = "blue"
            elif num_cartoes <= LIMITE_JOGOS_SEGURANCA:
                cor = "orange"

        self.label_cartoes_necessarios.config(
            text=f"Cartões Necessários: {num_cartoes:,} ({tipo_fechamento})", 
            fg=cor
        )


    # --- 3. LÓGICA DE GERAÇÃO (FECHAMENTO HÍBRIDO) ---
    
    def gerar_jogos(self):
        
        escolhas = sorted(list(self.numeros_escolhidos))
        n = len(escolhas)
        acerto_alvo = self.acerto_alvo.get()

        if n < MIN_ESCOLHAS:
            messagebox.showerror("Erro de Seleção", f"Você deve escolher no mínimo {MIN_ESCOLHAS} números.")
            return []
        
        num_total_jogos = 0
        jogos_gerados_tuplas = set()
        tipo_fechamento = ""

        # Lógica para Fechamento Otimizado (Garantia 11)
        if acerto_alvo == 11 and n in FECHAMENTO_11:
            num_total_jogos = FECHAMENTO_11[n]
            tipo_fechamento = "Otimizado (11)"
            
            # Amostragem aleatória única, baseada no número MINIMIZADO de jogos.
            while len(jogos_gerados_tuplas) < num_total_jogos:
                novo_jogo = tuple(sorted(random.sample(escolhas, NUMEROS_POR_JOGO)))
                jogos_gerados_tuplas.add(novo_jogo)
        
        else:
            # Lógica para Fechamento Completo (Garantia 15)
            num_total_jogos = self.calcular_combinacoes(n, NUMEROS_POR_JOGO)
            tipo_fechamento = "Completo (15)"
            
            if num_total_jogos > LIMITE_JOGOS_SEGURANCA:
                 if not messagebox.askyesno(
                     "Confirmação de Risco",
                     f"Você escolheu {n} números, o que gera {num_total_jogos:,} cartões (Fechamento Completo). Deseja continuar?"
                 ):
                     return []

            # GERAÇÃO DO FECHAMENTO COMPLETO
            jogos_gerados_tuplas = set(itertools.combinations(escolhas, NUMEROS_POR_JOGO))
        
        self.label_status.config(text=f"Gerado Fechamento {tipo_fechamento} com {len(jogos_gerados_tuplas):,} cartões.")

        return [list(jogo) for jogo in jogos_gerados_tuplas]

    
    def gerar_e_salvar_jogos(self):
        
        jogos = self.gerar_jogos()
        
        if jogos:
            self.gravar_pdf(jogos)
            messagebox.showinfo("Sucesso!", f"Total de {len(jogos):,} jogos gerados e salvos em 'jogos_lotofacil.pdf'.")
            self.label_status.config(text=f"Fechamento gerado com {len(jogos):,} cartões. Verifique o PDF.")


    # --- 4. EXPORTAÇÃO PARA PDF ---

    def gravar_pdf(self, jogos):
        """Gera um arquivo PDF com todos os jogos."""
        pdf = FPDF()
        try:
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=16, style='B')
            
            pdf.cell(0, 10, txt="Gerador de Jogos Lotofácil - FECHAMENTO GARANTIDO", ln=True, align='C')
            pdf.set_font("Arial", size=10)
            pdf.cell(0, 5, txt=f"Números Escolhidos ({len(self.numeros_escolhidos)}): {', '.join(map(str, sorted(list(self.numeros_escolhidos))))}", ln=True, align='C')
            
            acerto_alvo_selecionado = self.acerto_alvo.get()
            n = len(self.numeros_escolhidos)
            
            tipo_fechamento = f"Fechamento Otimizado (Garante {acerto_alvo_selecionado})" if acerto_alvo_selecionado == 11 and n in FECHAMENTO_11 else f"Fechamento Completo (Garante 15)"

            pdf.cell(0, 10, txt=f"OBJETIVO: {tipo_fechamento}", ln=True, align='C')
            pdf.cell(0, 5, txt=f"Total de Cartões Gerados: {len(jogos):,}", ln=True, align='C')

            pdf.ln(5) 
            pdf.set_font("Arial", size=12)
            
            # CÁLCULO DO LAYOUT HORIZONTAL
            largura_util = pdf.w - (pdf.l_margin + pdf.r_margin)
            # USANDO A VARIÁVEL CORRETA (com Ç)
            largura_total_espacos = ESPAÇAMENTO_HORIZONTAL * (NUMERO_COLUNAS - 1) 
            largura_cartoes_disponivel = largura_util - largura_total_espacos
            col_width = largura_cartoes_disponivel / NUMERO_COLUNAS
            
            y_start = pdf.get_y()
            col = 0
            
            for i, jogo in enumerate(jogos):
                
                # USANDO A VARIÁVEL CORRETA (com Ç)
                pos_x = pdf.l_margin + (col * col_width) + (col * ESPAÇAMENTO_HORIZONTAL)

                if col == NUMERO_COLUNAS: 
                    col = 0
                    y_start += (ALTURA_CARTAO + ESPACAMENTO_VERTICAL)
                    pos_x = pdf.l_margin
                
                if y_start > pdf.h - 30: 
                     pdf.add_page()
                     y_start = 15 
                     # USANDO A VARIÁVEL CORRETA (com Ç)
                     pos_x = pdf.l_margin + (col * col_width) + (col * ESPAÇAMENTO_HORIZONTAL) 

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
            
        except Exception as e:
            messagebox.showerror("Erro ao Gerar PDF", f"Ocorreu um erro ao tentar salvar o arquivo: {e}")
            # Tenta gerar o arquivo de texto como fallback, caso o PDF continue falhando
            self.gravar_texto(jogos)


    def gravar_texto(self, jogos):
        """Função de fallback para salvar em TXT se o PDF falhar."""
        output_file = "jogos_lotofacil_ERRO_PDF.txt"
        try:
            with open(output_file, 'w') as f:
                f.write("--- JOGOS LOTOFÁCIL GERADOS (ERRO PDF) ---\n")
                f.write(f"Números Escolhidos: {', '.join(map(str, sorted(list(self.numeros_escolhidos))))}\n\n")
                for i, jogo in enumerate(jogos):
                    f.write(f"Cartão {i+1}: {', '.join(map(str, jogo))}\n")
            messagebox.showinfo("Alerta", f"O PDF falhou, mas os jogos foram salvos em '{output_file}'.")
        except Exception as e:
             messagebox.showerror("Erro de Salvamento", f"Falha ao salvar em TXT também. Erro: {e}")


# --- INICIALIZAÇÃO ---

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = LotoFacilApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Erro Crítico", f"Ocorreu um erro no programa: {e}")
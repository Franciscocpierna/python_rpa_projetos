import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import numpy as np
import librosa
import sounddevice as sd
from scipy.io.wavfile import write

class DetectorHarmonicoEstudio:
    def __init__(self, root):
        self.root = root
        self.root.title("Assistente de Estúdio Avançado - Tom & Tons Vizinhos")
        self.root.geometry("680x580")
        self.root.resizable(False, False)
        
        # Mapeamento para exibição em português
        self.notas_pt = {
            'C': 'Dó', 'C#': 'Dó#', 'D': 'Ré', 'D#': 'Ré#', 'E': 'Mí', 'F': 'Fá',
            'F#': 'Fá#', 'G': 'Sol', 'G#': 'Sol#', 'A': 'Lá', 'A#': 'Lá#', 'B': 'Si'
        }
        
        self.campos_harmonicos = self.gerar_banco_campos_harmonicos()
        self.vizinhos_banco = self.gerar_banco_tons_vizinhos()
        self.criar_interface()

    def gerar_banco_campos_harmonicos(self):
        return {
            'Dó Maior': ['Dó', 'Rém', 'Mím', 'Fá', 'Sol', 'Lám'],
            'Dó# Maior': ['Dó#', 'Ré#m', 'Fám', 'Fá#', 'Sol#', 'Lá#m'],
            'Ré Maior': ['Ré', 'Mím', 'Fá#m', 'Sol', 'Lá', 'Sím'],
            'Ré# Maior': ['Ré#', 'Fám', 'Solm', 'Sol#', 'Lá#', 'Dóm'],
            'Mí Maior': ['Mí', 'Fá#m', 'Sol#m', 'Fá', 'Si', 'Dó#m'],
            'Fá Maior': ['Fá', 'Solm', 'Lám', 'Lá#', 'Dó', 'Rém'],
            'Fá# Maior': ['Fá#', 'Sol#m', 'Lá#m', 'Si', 'Dó#', 'Ré#m'],
            'Sol Maior': ['Sol', 'Lám', 'Sím', 'Dó', 'Ré', 'Mím'],
            'Sol# Maior': ['Sol#', 'Lá#m', 'Dóm', 'Dó#', 'Ré#', 'Fám'],
            'Lá Maior': ['Lá', 'Sím', 'Dó#m', 'Ré', 'Mí', 'Fá#m'],
            'Lá# Maior': ['Lá#', 'Dóm', 'Rém', 'Dó#', 'Fá', 'Solm'],
            'Si Maior': ['Si', 'Dó#m', 'Ré#m', 'Mí', 'Fá#', 'Sol#m'],
            
            'Dó Menor': ['Dóm', 'Ré°', 'Ré#', 'Fám', 'Solm', 'Sol#', 'Lá#'],
            'Dó# Menor': ['Dó#m', 'Ré#°', 'Mí', 'Fá#m', 'Sol#m', 'Lá', 'Si'],
            'Ré Menor': ['Rém', 'Mí°', 'Fá', 'Solm', 'Lám', 'Lá#', 'Dó'],
            'Ré# Menor': ['Ré#m', 'Fá°', 'Fá#', 'G#m', 'Lá#m', 'Si', 'Dó#'],
            'Mí Menor': ['Mím', 'Fá#°', 'Sol', 'Lám', 'Sím', 'Dó', 'Ré'],
            'Fá Menor': ['Fám', 'Sol°', 'Sol#', 'Lá#m', 'Dóm', 'Dó#', 'Ré#'],
            'Fá# Menor': ['Fá#m', 'G#°', 'Lá', 'Sím', 'Dó#m', 'Ré', 'Mí'],
            'Sol Menor': ['Solm', 'Lá°', 'Lá#', 'Dóm', 'Rém', 'Dó#', 'Fá'],
            'Sol# Menor': ['Sol#m', 'Lá#°', 'Si', 'Dó#m', 'Ré#m', 'Mí', 'Fá#'],
            'Lá Menor': ['Lám', 'Si°', 'Dó', 'Rém', 'Mím', 'Fá', 'Sol'],
            'Lá# Menor': ['Lá#m', 'Dóm°', 'Dó#', 'Ré#m', 'Fám', 'Fá#', 'G#'],
            'Si Menor': ['Sím', 'Dó#°', 'Ré', 'Mím', 'Fá#m', 'Sol', 'Lá']
        }

    def gerar_banco_tons_vizinhos(self):
        # Mapeamento teórico dos 5 tons vizinhos para cada tonalidade
        return {
            'Sol Menor': {
                'relativo': 'Si# Maior (ou Sib)', 'sub_dom': 'Dó Menor', 'dom': 'Ré Menor',
                'rel_sub_dom': 'Ré# Maior (ou Mib)', 'rel_dom': 'Fá Maior'
            },
            'Fá Menor': {
                'relativo': 'Sol# Maior (ou Lab)', 'sub_dom': 'Lá# Menor (ou Sibm)', 'dom': 'Dó Menor',
                'rel_sub_dom': 'Dó# Maior (ou Reb)', 'rel_dom': 'Ré# Maior (ou Mib)'
            },
            'Ré Menor': {
                'relativo': 'Fá Maior', 'sub_dom': 'Sol Menor', 'dom': 'Lá Menor',
                'rel_sub_dom': 'Lá# Maior (ou Sib)', 'rel_dom': 'Dó Maior'
            },
            'Lá Menor': {
                'relativo': 'Dó Maior', 'sub_dom': 'Ré Menor', 'dom': 'Mí Menor',
                'rel_sub_dom': 'Fá Maior', 'rel_dom': 'Sol Maior'
            },
            'Mí Menor': {
                'relativo': 'Sol Maior', 'sub_dom': 'Lá Menor', 'dom': 'Si Menor',
                'rel_sub_dom': 'Dó Maior', 'rel_dom': 'Ré Maior'
            },
            'Si Menor': {
                'relativo': 'Ré Maior', 'sub_dom': 'Mí Menor', 'dom': 'Fá# Menor',
                'rel_sub_dom': 'Sol Maior', 'rel_dom': 'Lá Maior'
            },
            'Dó Maior': {
                'relativo': 'Lá Menor', 'sub_dom': 'Fá Maior', 'dom': 'Sol Maior',
                'rel_sub_dom': 'Ré Menor', 'rel_dom': 'Mí Menor'
            },
            'Sol Maior': {
                'relativo': 'Mí Menor', 'sub_dom': 'Dó Maior', 'dom': 'Ré Maior',
                'rel_sub_dom': 'Lá Menor', 'rel_dom': 'Si Menor'
            },
            'Ré Maior': {
                'relativo': 'Si Menor', 'sub_dom': 'Sol Maior', 'dom': 'Lá Maior',
                'rel_sub_dom': 'Mí Menor', 'rel_dom': 'Fá# Menor'
            },
            'Lá Maior': {
                'relativo': 'Fá# Menor', 'sub_dom': 'Ré Maior', 'dom': 'Mí Maior',
                'rel_sub_dom': 'Si Menor', 'rel_dom': 'Dó#m'
            },
            'Fá Maior': {
                'relativo': 'Lá Menor', 'sub_dom': 'Lá# Maior (ou Sib)', 'dom': 'Dó Maior',
                'rel_sub_dom': 'Sol Menor', 'rel_dom': 'Ré Menor'
            }
        }

    def criar_interface(self):
        lbl_titulo = tk.Label(self.root, text="Detector de Tom & Modulações (Voz e Cavaquinho)", font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=12)

        frame_botoes = tk.Frame(self.root)
        frame_botoes.pack(pady=5)

        btn_arquivo = tk.Button(frame_botoes, text="Analisar MP3/WAV", command=self.carregar_arquivo, width=24, height=2, bg="#e1e1e1")
        btn_arquivo.grid(row=0, column=0, padx=10)

        btn_gravar = tk.Button(frame_botoes, text="Gravar Microfone (10s)", command=self.gravar_microfone, width=24, height=2, bg="#a8dadc")
        btn_gravar.grid(row=0, column=1, padx=10)

        self.lbl_tom_geral = tk.Label(self.root, text="TOM DETECTADO: ...", font=("Arial", 15, "bold"), fg="#e63946")
        self.lbl_tom_geral.pack(pady=10)

        frame_conteudo = tk.Frame(self.root)
        frame_conteudo.pack(pady=5, padx=20, fill="both", expand=True)

        self.txt_campo_harmonico = scrolledtext.ScrolledText(frame_conteudo, width=65, height=18, font=("Courier New", 10), bg="#f8f9fa")
        self.txt_campo_harmonico.pack(fill="both", expand=True)

        self.lbl_status = tk.Label(self.root, text="Pronto para rodar seu arranjo.", font=("Arial", 9, "italic"), fg="gray")
        self.lbl_status.pack(pady=8)

    def traduzir_texto(self, texto_acorde):
        for en, pt in self.notas_pt.items():
            if texto_acorde.startswith(en):
                return texto_acorde.replace(en, pt, 1)
        return texto_acorde

    def atualizar_painel_completo(self, tom_encontrado):
        self.txt_campo_harmonico.delete('1.0', tk.END)
        tom_chave = tom_encontrado.strip()
        acordes_do_tom = self.campos_harmonicos.get(tom_chave, [])
        
        if acordes_do_tom:
            # 1. Painel Principal
            self.txt_campo_harmonico.insert(tk.END, f" 🎼 ACORDES DO TOM PRINCIPAL: {tom_chave}\n")
            self.txt_campo_harmonico.insert(tk.END, " " + "=" * 55 + "\n")
            graus = ["I (Tônica)", "ii", "iii", "IV", "V", "vi", "vii°"]
            for i, acorde in enumerate(acordes_do_tom):
                if i < len(graus):
                    self.txt_campo_harmonico.insert(tk.END, f"   Grau {graus[i]:<12} ->  {acorde}\n")
            
            self.txt_campo_harmonico.insert(tk.END, "\n " + "-" * 55 + "\n")
            
            # 2. Painel de Tons Vizinhos (Caminhos para mudar de tom no Samba)
            self.txt_campo_harmonico.insert(tk.END, f" 🔄 TONS VIZINHOS RECOMENDADOS (Para a 2ª Parte / Saídas):\n")
            self.txt_campo_harmonico.insert(tk.END, " " + "=" * 55 + "\n")
            
            vizinhos = self.vizinhos_banco.get(tom_chave, None)
            if vizinhos:
                self.txt_campo_harmonico.insert(tk.END, f"   • Vizinho Direto (Relativo)  -> {vizinhos['relativo']}\n")
                self.txt_campo_harmonico.insert(tk.END, f"   • Vizinho Próximo (4º Grau)  -> {vizinhos['sub_dom']}\n")
                self.txt_campo_harmonico.insert(tk.END, f"   • Vizinho Próximo (5º Grau)  -> {vizinhos['dom']}\n")
                self.txt_campo_harmonico.insert(tk.END, f"   • Relativo do 4º Grau        -> {vizinhos['rel_sub_dom']}\n")
                self.txt_campo_harmonico.insert(tk.END, f"   • Relativo do 5º Grau        -> {vizinhos['rel_dom']}\n\n")
                self.txt_campo_harmonico.insert(tk.END, "   💡 Dica: Mudar para o Relativo clareia a melodia,\n   enquanto ir para o 4º ou 5º grau traz mais tensão!")
            else:
                # Fallback gerado dinamicamente caso o tom exato não esteja no banco fixo dos vizinhos
                self.txt_campo_harmonico.insert(tk.END, f"   • Use o Grau vi como Relativo Direto.\n")
                self.txt_campo_harmonico.insert(tk.END, f"   • Use os Graus IV e V para transições harmônicas clássicas.")
        else:
            self.txt_campo_harmonico.insert(tk.END, f"Aviso: Tom detectado, mas fora da tabela estruturada:\n'{tom_chave}'")

    def analisar_audio_completo(self, caminho_audio):
        try:
            self.lbl_tom_geral.config(text="TOM DETECTADO: Analisando...", fg="#1d3557")
            self.root.update()

            y, sr = librosa.load(caminho_audio, sr=None)
            chroma = librosa.feature.chroma_stft(y=y, sr=sr, hop_length=4096)
            
            chroma_medio = np.mean(chroma, axis=1)
            perfil_maior = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
            perfil_menor = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]
            
            nomes_notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
            melhor_score_tom = -1
            tom_predominante = ""

            for i in range(12):
                score_maior = np.corrcoef(chroma_medio, np.roll(perfil_maior, i))[0, 1]
                score_menor = np.corrcoef(chroma_medio, np.roll(perfil_menor, i))[0, 1]
                
                if score_maior > melhor_score_tom:
                    melhor_score_tom = score_maior
                    tom_predominante = f"{nomes_notas[i]} Maior"
                if score_menor > melhor_score_tom:
                    melhor_score_tom = score_menor
                    tom_predominante = f"{nomes_notas[i]} Menor"

            tom_pt = self.traduzir_texto(tom_predominante)
            self.lbl_tom_geral.config(text=f"TOM DETECTADO: {tom_pt}", fg="#e63946")
            
            self.atualizar_painel_completo(tom_pt)
            self.lbl_status.config(text="Análise de estúdio concluída!", fg="green")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro no processamento: {e}")
            self.lbl_status.config(text="Erro ao processar áudio.", fg="red")

    def carregar_arquivo(self):
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecione o áudio do seu samba",
            filetypes=[("Arquivos de Áudio", "*.mp3 *.wav *.ogg")]
        )
        if caminho_arquivo:
            self.lbl_status.config(text="Analisando arquivo...", fg="blue")
            self.analisar_audio_completo(caminho_arquivo)

    def gravar_microfone(self):
        fs = 44100
        segundos = 10
        self.lbl_status.config(text="Gravando... Solta o som!", fg="red")
        self.root.update()
        
        try:
            gravacao = sd.rec(int(segundos * fs), samplerate=fs, channels=1, dtype='float32')
            sd.wait()
            
            arquivo_temp = "temp_estudio_vizinhos.wav"
            write(arquivo_temp, fs, gravacao)
            
            self.lbl_status.config(text="Mapeando estrutura tonal...", fg="blue")
            self.analisar_audio_completo(arquivo_temp)
            
            if os.path.exists(arquivo_temp):
                os.remove(arquivo_temp)
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro no microfone: {e}")
            self.lbl_status.config(text="Falha na gravação.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = DetectorHarmonicoEstudio(root)
    root.mainloop()
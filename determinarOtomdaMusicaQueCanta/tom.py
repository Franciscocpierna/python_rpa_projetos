import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import numpy as np
import librosa
import sounddevice as sd
from scipy.io.wavfile import write

class DetectorSuperCompletoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Detector de Harmonia e Campo Harmônico")
        self.root.geometry("750x550")
        self.root.resizable(False, False)
        
        # Mapeamento para exibição em português
        self.notas_pt = {
            'C': 'Dó', 'C#': 'Dó#', 'D': 'Ré', 'D#': 'Ré#', 'E': 'Mí', 'F': 'Fá',
            'F#': 'Fá#', 'G': 'Sol', 'G#': 'Sol#', 'A': 'Lá', 'A#': 'Lá#', 'B': 'Si'
        }
        
        # Dicionário padronizado dos Campos Harmônicos
        self.campos_harmonicos = self.gerar_banco_campos_harmonicos()

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

    def criar_interface(self):
        lbl_titulo = tk.Label(self.root, text="Análise Harmônica Avançada", font=("Arial", 16, "bold"))
        lbl_titulo.pack(pady=15)

        frame_botoes = tk.Frame(self.root)
        frame_botoes.pack(pady=5)

        btn_arquivo = tk.Button(frame_botoes, text="Analisar MP3/WAV", command=self.carregar_arquivo, width=22, height=2, bg="#e1e1e1")
        btn_arquivo.grid(row=0, column=0, padx=10)

        btn_gravar = tk.Button(frame_botoes, text="Cantar no Microfone (10s)", command=self.gravar_microfone, width=22, height=2, bg="#a8dadc")
        btn_gravar.grid(row=0, column=1, padx=10)

        self.lbl_tom_geral = tk.Label(self.root, text="TOM DETECTADO: ...", font=("Arial", 14, "bold"), fg="#e63946")
        self.lbl_tom_geral.pack(pady=15)

        frame_conteudo = tk.Frame(self.root)
        frame_conteudo.pack(pady=10, padx=20, fill="both", expand=True)

        # Esquerda: O que cantou
        frame_esquerda = tk.Frame(frame_conteudo)
        frame_esquerda.pack(side="left", fill="both", expand=True, padx=10)

        lbl_seq = tk.Label(frame_esquerda, text="Sequência que você Cantou/Tocou:", font=("Arial", 10, "bold"))
        lbl_seq.pack(anchor="w")
        
        self.txt_acordes = scrolledtext.ScrolledText(frame_esquerda, width=38, height=12, font=("Courier New", 10))
        self.txt_acordes.pack(fill="both", expand=True)

        # Direita: Guia do Tom
        frame_direita = tk.Frame(frame_conteudo)
        frame_direita.pack(side="right", fill="both", expand=True, padx=10)

        lbl_sugestao = tk.Label(frame_direita, text="Acordes que combinam com esse Tom:", font=("Arial", 10, "bold"), fg="#1d3557")
        lbl_sugestao.pack(anchor="w")

        self.txt_campo_harmonico = scrolledtext.ScrolledText(frame_direita, width=38, height=12, font=("Courier New", 10), bg="#f8f9fa")
        self.txt_campo_harmonico.pack(fill="both", expand=True)

        self.lbl_status = tk.Label(self.root, text="Pronto.", font=("Arial", 9, "italic"), fg="gray")
        self.lbl_status.pack(pady=5)

    def mapear_para_acorde(self, chroma_vetor):
        nomes_notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        melhor_score = -1
        acorde_detectado = "Indefinido"
        
        for i in range(12):
            perfil_maior = np.zeros(12)
            perfil_maior[[i, (i+4)%12, (i+7)%12]] = 1
            perfil_menor = np.zeros(12)
            perfil_menor[[i, (i+3)%12, (i+7)%12]] = 1
            
            score_maior = np.dot(chroma_vetor, perfil_maior)
            score_menor = np.dot(chroma_vetor, perfil_menor)
            
            if score_maior > melhor_score:
                melhor_score = score_maior
                acorde_detectado = f"{nomes_notas[i]}"
            if score_menor > melhor_score:
                melhor_score = score_menor
                acorde_detectado = f"{nomes_notas[i]}m"
                
        return acorde_detectado

    def traduzir_texto(self, texto_acorde):
        for en, pt in self.notas_pt.items():
            if texto_acorde.startswith(en):
                return texto_acorde.replace(en, pt, 1)
        return texto_acorde

    def atualizar_painel_campo_harmonico(self, tom_encontrado):
        self.txt_campo_harmonico.delete('1.0', tk.END)
        
        # Limpeza para evitar erros de comparação de texto
        tom_chave = tom_encontrado.strip()
        acordes_do_tom = self.campos_harmonicos.get(tom_chave, [])
        
        if acordes_do_tom:
            self.txt_campo_harmonico.insert(tk.END, f"Tom Base: {tom_chave}\n")
            self.txt_campo_harmonico.insert(tk.END, "=" * 35 + "\n\n")
            self.txt_campo_harmonico.insert(tk.END, "Use estes acordes para acompanhar\nou continuar sua composição:\n\n")
            
            graus = ["I (Tônica)", "ii", "iii", "IV", "V", "vi", "vii°"]
            for i, acorde in enumerate(acordes_do_tom):
                if i < len(graus):
                    self.txt_campo_harmonico.insert(tk.END, f" Grau {graus[i]:<10} -> {acorde}\n")
        else:
            self.txt_campo_harmonico.insert(tk.END, f"Aviso:\nNão mapeado no dicionário:\n'{tom_chave}'")

    def analisar_audio_completo(self, caminho_audio):
        try:
            self.txt_acordes.delete('1.0', tk.END)
            self.lbl_tom_geral.config(text="TOM DETECTADO: Analisando...", fg="#1d3557")
            self.root.update()

            y, sr = librosa.load(caminho_audio, sr=None)
            hop_length = 4096
            chroma = librosa.feature.chroma_stft(y=y, sr=sr, hop_length=hop_length)
            tempos = librosa.frames_to_time(range(chroma.shape[1]), sr=sr, hop_length=hop_length)
            
            # Análise Global do Tom
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

            # Atualiza o painel da direita
            self.atualizar_painel_campo_harmonico(tom_pt)

            # Mapeamento cronológico na esquerda
            self.txt_acordes.insert(tk.END, f"{'Tempo':<8} | Acorde\n")
            self.txt_acordes.insert(tk.END, "-" * 25 + "\n")
            
            acorde_anterior = ""
            for col, tempo in enumerate(tempos):
                chroma_vetor = chroma[:, col]
                if np.sum(chroma_vetor) < 0.1:
                    continue
                    
                acorde = self.mapear_para_acorde(chroma_vetor)
                
                if acorde != acorde_anterior and acorde != "Indefinido":
                    minutos = int(tempo // 60)
                    segundos = int(tempo % 60)
                    acorde_pt = self.traduzir_texto(acorde)
                    self.txt_acordes.insert(tk.END, f"{minutos:02d}:{segundos:02d}s   | {acorde_pt}\n")
                    acorde_anterior = acorde
            
            self.lbl_status.config(text="Análise completa!", fg="green")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro no processamento: {e}")
            self.lbl_status.config(text="Erro ao processar.", fg="red")

    def carregar_arquivo(self):
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecione o arquivo de áudio",
            filetypes=[("Arquivos de Áudio", "*.mp3 *.wav *.ogg")]
        )
        if caminho_arquivo:
            self.lbl_status.config(text="Analisando arquivo...", fg="blue")
            self.analisar_audio_completo(caminho_arquivo)

    def gravar_microfone(self):
        fs = 44100
        segundos = 10
        
        self.lbl_status.config(text="Gravando 10 segundos... Cante!", fg="red")
        self.root.update()
        
        try:
            gravacao = sd.rec(int(segundos * fs), samplerate=fs, channels=1, dtype='float32')
            sd.wait()
            
            arquivo_temp = "temp_harmonia_total.wav"
            write(arquivo_temp, fs, gravacao)
            
            self.lbl_status.config(text="Montando mapas harmônicos...", fg="blue")
            self.analisar_audio_completo(arquivo_temp)
            
            if os.path.exists(arquivo_temp):
                os.remove(arquivo_temp)
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro no microfone: {e}")
            self.lbl_status.config(text="Falha na gravação.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = DetectorSuperCompletoApp(root)
    root.mainloop()
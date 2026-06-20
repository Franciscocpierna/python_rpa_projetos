import os
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import librosa
import sounddevice as sd
from scipy.io.wavfile import write

class DetectorDeTomApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Detector de Tom Vocal")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Mapeamento de notas em português
        self.notas_pt = {
            'C': 'Dó', 'C#': 'Dó#', 'D': 'Ré', 'D#': 'Ré#', 'E': 'Mí', 'F': 'Fá',
            'F#': 'Fá#', 'G': 'Sol', 'G#': 'Sol#', 'A': 'Lá', 'A#': 'Lá#', 'B': 'Si'
        }

        self.criar_interface()

    def criar_interface(self):
        # Título
        lbl_titulo = tk.Label(self.root, text="Detector de Tom Predominante", font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=20)

        # Botão para carregar arquivo
        btn_arquivo = tk.Button(self.root, text="Escolher Arquivo MP3/WAV", command=self.carregar_arquivo, width=25, height=2, bg="#e1e1e1")
        btn_arquivo.pack(pady=10)

        # Botão para gravar do microfone
        btn_gravar = tk.Button(self.root, text="Cantar no Microfone (5s)", command=self.gravar_microfone, width=25, height=2, bg="#a8dadc")
        btn_gravar.pack(pady=10)

        # Label de Resultado
        self.lbl_resultado = tk.Label(self.root, text="Resultado: Aguardando áudio...", font=("Arial", 12, "italic"), fg="gray")
        self.lbl_resultado.pack(pady=20)

    def analisar_tom(self, caminho_audio):
        """Processa o áudio e determina a nota musical predominante."""
        try:
            # Carrega o áudio (converte para mono automaticamente)
            y, sr = librosa.load(caminho_audio, sr=None)
            
            # Extrai as notas (Chroma Short-Time Fourier Transform)
            chroma = librosa.feature.chroma_stft(y=y, sr=sr)
            
            # Soma a intensidade de cada uma das 12 notas ao longo do tempo
            soma_notas = np.sum(chroma, axis=1)
            
            # Encontra o índice da nota com maior intensidade
            nota_predominante_idx = np.argmax(soma_notas)
            
            # Lista padrão de notas (C, C#, D...)
            nomes_notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
            nota_encontrada = nomes_notas[nota_predominante_idx]
            
            # Traduz para o português
            nota_pt = self.notas_pt.get(nota_encontrada, nota_encontrada)
            
            self.lbl_resultado.config(text=f"Tom Predominante: {nota_pt}", font=("Arial", 14, "bold"), fg="green")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar o áudio: {e}")

    def carregar_arquivo(self):
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecione o arquivo de áudio",
            filetypes=[("Arquivos de Áudio", "*.mp3 *.wav *.ogg")]
        )
        if caminho_arquivo:
            self.lbl_resultado.config(text="Analisando arquivo...", fg="blue")
            self.root.update()
            self.analisar_tom(caminho_arquivo)

    def gravar_microfone(self):
        fs = 44100  # Taxa de amostragem
        segundos = 5  # Duração da gravação
        
        self.lbl_resultado.config(text="Gravando... Cante agora!", fg="red")
        self.root.update()
        
        try:
            # Grava o áudio do microfone
            gravacao = sd.rec(int(segundos * fs), samplerate=fs, channels=1, dtype='float32')
            sd.wait()  # Espera a gravação terminar
            
            # Salva temporariamente para o librosa ler
            arquivo_temp = "temp_vocal.wav"
            write(arquivo_temp, fs, gravacao)
            
            self.lbl_resultado.config(text="Analisando gravação...", fg="blue")
            self.root.update()
            
            self.analisar_tom(arquivo_temp)
            
            # Limpa o arquivo temporário
            if os.path.exists(arquivo_temp):
                os.remove(arquivo_temp)
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao acessar o microfone: {e}")
            self.lbl_resultado.config(text="Erro na gravação.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = DetectorDeTomApp(root)
    root.mainloop()
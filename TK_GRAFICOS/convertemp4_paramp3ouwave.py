import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os
import ffmpeg

def converter_mp4_para_audio_ffmpeg():
    """
    Permite ao usuário escolher entre MP3 ou WAV, seleciona um arquivo MP4,
    converte para o formato escolhido e salva no mesmo diretório.
    """
    janela_principal = tk.Tk()
    janela_principal.withdraw()

    # Escolha do formato de saída
    formato = simpledialog.askstring(
        "Escolha o formato",
        "Digite o formato de áudio desejado (mp3 ou wav):",
        parent=janela_principal
    )

    if not formato or formato.lower() not in ["mp3", "wav"]:
        messagebox.showinfo("Informação", "Formato inválido ou não selecionado.")
        return

    caminho_mp4 = filedialog.askopenfilename(
        title="Selecione um arquivo MP4 para converter",
        filetypes=[("Arquivos MP4", "*.mp4")]
    )

    if not caminho_mp4:
        messagebox.showinfo("Informação", "Nenhum arquivo foi selecionado.")
        return

    diretorio = os.path.dirname(caminho_mp4)
    nome_arquivo = os.path.basename(caminho_mp4)
    nome_base = os.path.splitext(nome_arquivo)[0]
    caminho_audio = os.path.join(diretorio, f"{nome_base}.{formato.lower()}")

    try:
        if formato.lower() == "mp3":
            ffmpeg.input(caminho_mp4).output(caminho_audio, acodec='libmp3lame').run()
        elif formato.lower() == "wav":
            ffmpeg.input(caminho_mp4).output(caminho_audio, acodec='pcm_s16le').run()

        messagebox.showinfo(
            "Sucesso",
            f"O arquivo MP4 foi convertido para {formato.upper()}.\nArquivo salvo em:\n{caminho_audio}"
        )

    except ffmpeg.Error as e:
        erro = f"Erro de FFmpeg:\n{e.stderr.decode()}"
        messagebox.showerror("Erro na Conversão", erro)
    except Exception as e:
        erro = f"Ocorreu um erro inesperado:\n{str(e)}"
        messagebox.showerror("Erro", erro)

if __name__ == "__main__":
    converter_mp4_para_audio_ffmpeg()
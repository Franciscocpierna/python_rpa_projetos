import tkinter as tk
from tkinter import filedialog, messagebox
import os
import ffmpeg

def converter_mp4_para_mp3_ffmpeg():
    """
    Abre uma caixa de diálogo para selecionar um arquivo MP4,
    converte-o para MP3 e salva o arquivo no mesmo diretório.
    Se um erro ocorrer, exibe uma caixa de diálogo com a mensagem de erro.
    """
    janela_principal = tk.Tk()
    janela_principal.withdraw()

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
    caminho_mp3 = os.path.join(diretorio, nome_base + ".mp3")

    try:
        # Usa o ffmpeg-python para extrair o áudio e salvar como MP3
        ffmpeg.input(caminho_mp4).output(caminho_mp3, acodec='libmp3lame').run()
        
        messagebox.showinfo("Sucesso", f"O arquivo MP4 foi convertido para MP3.\nArquivo salvo em:\n{caminho_mp3}")

    except ffmpeg.Error as e:
        erro = f"Erro de FFmpeg:\n{e.stderr.decode()}"
        messagebox.showerror("Erro na Conversão", erro)
    except Exception as e:
        erro = f"Ocorreu um erro inesperado:\n{str(e)}"
        messagebox.showerror("Erro", erro)

if __name__ == "__main__":
    converter_mp4_para_mp3_ffmpeg()
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os
import ffmpeg

def converter_mp4_wmv_para_audio_ffmpeg():
    """
    Permite ao usuário escolher entre MP3 ou WAV, seleciona um arquivo MP4 ou WMV,
    converte para o formato escolhido e salva no mesmo diretório.
    """
    janela_principal = tk.Tk()
    janela_principal.withdraw()

    # --- 1. Escolha do formato de saída ---
    formato_saida = simpledialog.askstring(
        "Escolha o formato de saída",
        "Digite o formato de áudio desejado (mp3 ou wav):",
        parent=janela_principal
    )

    if not formato_saida or formato_saida.lower() not in ["mp3", "wav"]:
        messagebox.showinfo("Informação", "Formato de saída inválido ou não selecionado.")
        return

    # --- 2. Seleção do arquivo de entrada (MP4 ou WMV) ---
    caminho_video = filedialog.askopenfilename(
        title="Selecione um arquivo de vídeo (MP4 ou WMV) para converter",
        # Inclui ambos os formatos na lista de tipos de arquivo
        filetypes=[
            ("Arquivos de Vídeo Comuns", "*.mp4;*.wmv"),
            ("Arquivos MP4", "*.mp4"),
            ("Arquivos WMV", "*.wmv"),
            ("Todos os arquivos", "*.*")
        ]
    )

    if not caminho_video:
        messagebox.showinfo("Informação", "Nenhum arquivo de vídeo foi selecionado.")
        return

    # --- 3. Preparação dos caminhos ---
    diretorio = os.path.dirname(caminho_video)
    nome_arquivo = os.path.basename(caminho_video)
    nome_base = os.path.splitext(nome_arquivo)[0]
    
    formato_saida_lower = formato_saida.lower()
    caminho_audio = os.path.join(diretorio, f"{nome_base}.{formato_saida_lower}")

    try:
        # --- 4. Configuração e Execução do FFmpeg ---
        stream = ffmpeg.input(caminho_video)
        
        if formato_saida_lower == "mp3":
            # Código para MP3
            stream = stream.output(caminho_audio, acodec='libmp3lame')
        elif formato_saida_lower == "wav":
            # Código para WAV (PCM não-comprimido)
            stream = stream.output(caminho_audio, acodec='pcm_s16le')

        # Executa a conversão
        stream.run(overwrite_output=True) 

        messagebox.showinfo(
            "Sucesso",
            f"O arquivo de vídeo foi convertido para {formato_saida.upper()}.\nArquivo salvo em:\n{caminho_audio}"
        )

    except ffmpeg.Error as e:
        # O erro é capturado e decodificado para ser legível
        erro = f"Erro de FFmpeg:\n{e.stderr.decode()}"
        messagebox.showerror("Erro na Conversão", erro)
    except Exception as e:
        erro = f"Ocorreu um erro inesperado:\n{str(e)}"
        messagebox.showerror("Erro", erro)

if __name__ == "__main__":
    converter_mp4_wmv_para_audio_ffmpeg()
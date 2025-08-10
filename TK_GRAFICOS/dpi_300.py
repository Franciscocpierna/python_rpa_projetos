from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

def converter_para_300dpi_com_dialog():
    """
    Permite ao usuário selecionar uma imagem via file dialog,
    converte-a para 300 DPI e salva o arquivo.
    """
    root = tk.Tk()
    root.withdraw()

    caminho_imagem_original = filedialog.askopenfilename(
        title="Selecione a imagem para converter para 300 DPI",
        filetypes=[("Arquivos de Imagem", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos os arquivos", "*.*")]
    )

    if not caminho_imagem_original:
        print("Nenhuma imagem selecionada. Operação cancelada.")
        return

    try:
        with Image.open(caminho_imagem_original) as img:
            largura_pixels, altura_pixels = img.size

            # Define a nova resolução em DPI para alta resolução (300 DPI)
            nova_dpi = (300, 300)

            img.info['dpi'] = nova_dpi

            diretorio, nome_arquivo = os.path.split(caminho_imagem_original)
            nome_base, extensao = os.path.splitext(nome_arquivo)
            caminho_imagem_saida = os.path.join(diretorio, f"{nome_base}_300dpi{extensao}")

            if img.mode == 'RGBA' and extensao.lower() in ['.jpg', '.jpeg']:
                img = img.convert('RGB')

            img.save(caminho_imagem_saida, dpi=nova_dpi, quality=95)
            print(f"Imagem salva com sucesso em '{caminho_imagem_saida}' com 300 DPI.")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_imagem_original}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# --- Execução do programa ---
if __name__ == "__main__":
    converter_para_300dpi_com_dialog()
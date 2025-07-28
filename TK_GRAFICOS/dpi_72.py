from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os # Para manipular caminhos de arquivo

def redimensionar_para_72dpi_com_dialog():
    """
    Permite ao usuário selecionar uma imagem via file dialog,
    converte-a para 72 DPI e salva o arquivo.
    """
    root = tk.Tk()
    root.withdraw() # Esconde a janela principal do Tkinter

    caminho_imagem_original = filedialog.askopenfilename(
        title="Selecione a imagem para converter para 72 DPI",
        filetypes=[("Arquivos de Imagem", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos os arquivos", "*.*")]
    )

    if not caminho_imagem_original:
        print("Nenhuma imagem selecionada. Operação cancelada.")
        return

    try:
        with Image.open(caminho_imagem_original) as img:
            # Pega as dimensões atuais da imagem em pixels
            largura_pixels, altura_pixels = img.size

            # Define a nova resolução em DPI
            nova_dpi = (72, 72)

            # Define a informação de DPI na imagem.
            # O Pillow irá incorporar essa informação no metadado do arquivo ao salvar.
            img.info['dpi'] = nova_dpi

            # Monta o nome do arquivo de saída
            diretorio, nome_arquivo = os.path.split(caminho_imagem_original)
            nome_base, extensao = os.path.splitext(nome_arquivo)
            caminho_imagem_saida = os.path.join(diretorio, f"{nome_base}_72dpi{extensao}")

            # Converte para RGB se tiver transparência para compatibilidade com JPEG
            if img.mode == 'RGBA' and extensao.lower() in ['.jpg', '.jpeg']:
                img = img.convert('RGB')

            # Salva a imagem com a nova informação de DPI
            # quality é um parâmetro para JPEG e pode ser ajustado (0-100)
            img.save(caminho_imagem_saida, dpi=nova_dpi, quality=95)
            print(f"Imagem salva com sucesso em '{caminho_imagem_saida}' com 72 DPI.")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_imagem_original}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# --- Execução do programa ---
if __name__ == "__main__":
    redimensionar_para_72dpi_com_dialog()
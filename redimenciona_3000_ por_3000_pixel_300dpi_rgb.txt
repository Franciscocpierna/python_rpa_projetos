from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def redimensionar_e_converter_3000x3000():
    """
    Permite ao usuário selecionar uma imagem, redimensiona-a para 3000x3000 pixels,
    converte-a para 300 DPI e salva o arquivo de saída no formato JPEG com modo de cor RGB.
    """
    root = tk.Tk()
    root.withdraw()

    caminho_imagem_original = filedialog.askopenfilename(
        title="Selecione a imagem para redimensionar (3000x3000)",
        filetypes=[("Arquivos de Imagem", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos os arquivos", "*.*")]
    )

    if not caminho_imagem_original:
        messagebox.showinfo("Informação", "Nenhuma imagem foi selecionada. Operação cancelada.")
        return

    try:
        with Image.open(caminho_imagem_original) as img:
            # 1. Redimensiona a imagem para 3000x3000 pixels
            # O parâmetro 'Image.Resampling.LANCZOS' garante um redimensionamento de alta qualidade.
            img_redimensionada = img.resize((3000, 3000), Image.Resampling.LANCZOS)
            
            # 2. Converte a imagem para o modo de cor RGB
            img_rgb = img_redimensionada.convert('RGB')
            
            # 3. Define a resolução de alta qualidade para impressão
            nova_dpi = (300, 300)
            
            # 4. Monta o nome e caminho do arquivo de saída
            diretorio, nome_arquivo = os.path.split(caminho_imagem_original)
            nome_base, _ = os.path.splitext(nome_arquivo)
            caminho_imagem_saida = os.path.join(diretorio, f"{nome_base}_3000x3000_300dpi_RGB.jpg")
            
            # 5. Salva a imagem no formato JPEG com as novas configurações
            # quality=95 é um valor alto para garantir boa qualidade de imagem
            img_rgb.save(caminho_imagem_saida, dpi=nova_dpi, quality=95)
            
            messagebox.showinfo("Sucesso", f"Imagem salva com sucesso em '{caminho_imagem_saida}'\ncom 3000x3000 pixels e 300 DPI.")

    except FileNotFoundError:
        messagebox.showerror("Erro", f"Erro: Arquivo '{caminho_imagem_original}' não encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    redimensionar_e_converter_3000x3000()
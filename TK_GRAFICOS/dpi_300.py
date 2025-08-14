from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

def converter_para_300dpi_rgb():
    """
    Permite ao usuário selecionar uma imagem, converte-a para 300 DPI
    e salva o arquivo de saída no formato JPEG com modo de cor RGB.
    """
    root = tk.Tk()
    root.withdraw()

    caminho_imagem_original = filedialog.askopenfilename(
        title="Selecione a imagem para converter para 300 DPI e RGB",
        filetypes=[("Arquivos de Imagem", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos os arquivos", "*.*")]
    )

    if not caminho_imagem_original:
        print("Nenhuma imagem selecionada. Operação cancelada.")
        return

    try:
        with Image.open(caminho_imagem_original) as img:
            # 1. Converte a imagem para o modo de cor RGB
            img_rgb = img.convert('RGB')

            # 2. Define a resolução de alta qualidade para impressão
            nova_dpi = (300, 300)

            # 3. Monta o nome e caminho do arquivo de saída
            diretorio, nome_arquivo = os.path.split(caminho_imagem_original)
            nome_base, _ = os.path.splitext(nome_arquivo)
            caminho_imagem_saida = os.path.join(diretorio, f"{nome_base}_300_DPI_RGB.jpg")

            # 4. Salva a imagem no formato JPEG com as novas configurações
            # quality=95 é um valor alto para garantir boa qualidade de imagem
            img_rgb.save(caminho_imagem_saida, dpi=nova_dpi, quality=95)

            print(f"Imagem salva com sucesso em '{caminho_imagem_saida}' com 300 DPI e modo de cor RGB.")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_imagem_original}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# --- Execução do programa ---
if __name__ == "__main__":
    converter_para_300dpi_rgb()
        
# O uso do with é obrigatório ou altamente recomendado quando você trabalha com recursos que precisam ser abertos e fechados corretamente, como:

# Arquivos (leitura/escrita): with open('arquivo.txt') as f:
# Imagens (como no seu código, usando Pillow): with Image.open('imagem.png') as img:
# Conexões de banco de dados (algumas bibliotecas suportam contexto)
# Sockets de rede
# Locks/mutexes (controle de concorrência)
# Gerenciadores de contexto personalizados (qualquer classe que implemente __enter__ e __exit__)
# O with garante que o recurso será fechado/liberado corretamente, mesmo se ocorrer erro no bloco. Isso evita vazamentos de memória, arquivos abertos indevidamente ou travamentos.
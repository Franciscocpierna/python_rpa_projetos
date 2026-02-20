from PIL import Image, ImageFilter  # Importa a biblioteca de manipulação de imagem e filtros
import tkinter as tk               # Importa interface gráfica para janelas
from tkinter import filedialog, messagebox
import os                          # Importa funções do sistema operacional (manipulação de pastas)

def redimensionar_e_converter_3000x3000_hd():
    """
    Seleciona uma imagem, redimensiona para 3000x3000px com alta qualidade,
    aplica filtro de nitidez para HD, define 300 DPI e salva em JPEG RGB.
    """
    # 1. Configuração da janela oculta do Tkinter (para não abrir uma janela vazia atrás)
    root = tk.Tk()
    root.withdraw()

    # 2. Abre a caixa de diálogo para o usuário escolher a imagem
    caminho_imagem_original = filedialog.askopenfilename(
        title="Selecione a imagem para Alta Definição (3000x3000px)",
        filetypes=[("Arquivos de Imagem", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos os arquivos", "*.*")]
    )

    # Se o usuário fechar a janela sem escolher nada, interrompe a função
    if not caminho_imagem_original:
        messagebox.showinfo("Informação", "Operação cancelada pelo usuário.")
        return

    try:
        # 3. Abre o arquivo de imagem original
        with Image.open(caminho_imagem_original) as img:
            
            # 4. Redimensionamento de Alta Qualidade
            # O filtro LANCZOS é o melhor algoritmo matemático para manter detalhes ao redimensionar.
            img_redimensionada = img.resize((3000, 3000), Image.Resampling.LANCZOS)
            
            # 5. Garantia de Alta Definição (HD) - Filtro de Nitidez
            # Aplicamos SHARPEN para recuperar o foco nas bordas que se perdem no redimensionamento.
            img_hd = img_redimensionada.filter(ImageFilter.SHARPEN)
            
            # 6. Conversão para o modo de cor RGB
            # Essencial para garantir compatibilidade total com o formato JPEG.
            img_rgb = img_hd.convert('RGB')
            
            # 7. Configuração de DPI (Resolução de impressão)
            # 300 DPI é o padrão profissional para impressões nítidas e alta definição física.
            nova_dpi = (300, 300)
            
            # 8. Geração do caminho e nome do arquivo de saída
            # Pega a pasta original e adiciona um sufixo ao nome para não sobrescrever a original.
            diretorio, nome_arquivo = os.path.split(caminho_imagem_original)
            nome_base, _ = os.path.splitext(nome_arquivo)
            caminho_imagem_saida = os.path.join(diretorio, f"{nome_base}_HD_3000_300dpi.jpg")
            
            # 9. Salvamento com compressão mínima (Qualidade Máxima)
            # quality=95 evita artefatos de compressão, mantendo a alta definição do arquivo.
            img_rgb.save(caminho_imagem_saida, "JPEG", dpi=nova_dpi, quality=95, subsampling=0)
            
            # 10. Alerta de sucesso para o usuário
            messagebox.showinfo("Sucesso", f"Imagem HD salva em:\n{caminho_imagem_saida}")

    except Exception as e:
        # Caso ocorra qualquer erro (arquivo corrompido, permissão negada, etc)
        messagebox.showerror("Erro", f"Ocorreu um problema ao processar a imagem:\n{e}")

if __name__ == "__main__":
    # Inicia a função principal
    redimensionar_e_converter_3000x3000_hd()
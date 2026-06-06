import os
import numpy as np
from gtts import gTTS
from moviepy import ImageClip, AudioFileClip
from PIL import Image

# 1. Configuração dos arquivos
imagem_entrada = "amazon.jpg"
video_saida = "amazonmusic.mp4"
audio_temp = "temp_voice.mp3"

# Verificar se a imagem existe
if not os.path.exists(imagem_entrada):
    print(f"Erro: O arquivo '{imagem_entrada}' não foi encontrado na pasta!")
    exit()

print("1/4 - Gerando o áudio 'Inscreva-se'...")
tts = gTTS(text="escaneie o qrcode, ou procure por Francisco Carlos Pierna no Amazon Music, seguir ou Inscreva-se", lang='pt', slow=False)
tts.save(audio_temp)

try:
    print("2/4 - Carregando os arquivos de mídia...")
    audio_clip = AudioFileClip(audio_temp)
    duracao = audio_clip.duration

    print("3/4 - Forçando compatibilidade da imagem...")
    # Abrimos com o Pillow para limpar qualquer perfil de cor estranho e garantir dimensões pares
    with Image.open(imagem_entrada) as img:
        img_rgb = img.convert("RGB")
        largura, altura = img_rgb.size
        
        # Garante que a largura e altura sejam múltiplos de 2 (obrigatório para o codec libx264)
        nova_largura = largura if largura % 2 == 0 else largura - 1
        nova_altura = altura if altura % 2 == 0 else altura - 1
        
        if (nova_largura != largura) or (nova_altura != altura):
            img_rgb = img_rgb.resize((nova_largura, nova_altura))
            
        # Transforma a imagem em uma Array NumPy que o MoviePy aceita sem reclamar
        img_array = np.array(img_rgb)

    # Criando o clipe com a imagem tratada
    video_clip = ImageClip(img_array).with_duration(duracao)

    # Juntando o áudio ao vídeo
    video_final = video_clip.with_audio(audio_clip)

    print("4/4 - Renderizando o arquivo MP4 final...")
    video_final.write_videofile(
        video_saida, 
        fps=24, 
        codec="libx264", 
        audio_codec="aac"
    )
    
    # Fechando os arquivos para liberar a memória
    video_final.close()
    audio_clip.close()
    print(f"\nSucesso absoluto! Vídeo do Amazon Music salvo como: {video_saida}")

except Exception as e:
    print(f"\nIh, deu erro: {e}")

finally:
    # Remove o áudio temporário
    if os.path.exists(audio_temp):
        os.remove(audio_temp)
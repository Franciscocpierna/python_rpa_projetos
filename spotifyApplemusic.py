import os
from gtts import gTTS
from moviepy import ImageClip, AudioFileClip

# 1. Configuração dos arquivos
imagem_entrada = "spotify.jpg"
video_saida = "spotify_promocional1.mp4"
#imagem_entrada = "applemusic.jpg"
#video_saida = "applemusic.mp4"

audio_temp = "temp_voice.mp3"

# Verificar se a imagem existe antes de começar
if not os.path.exists(imagem_entrada):
    print(f"Erro: O arquivo '{imagem_entrada}' não foi encontrado na pasta!")
    exit()

print("1/4 - Gerando o áudio 'Inscreva-se'...")
tts = gTTS(text="escaneie o qrcode, ou procure por Francisco Carlos Pierna no spotify, seguir ou Inscreva-se", lang='pt', slow=False)
tts.save(audio_temp)

try:
    print("2/4 - Carregando os arquivos de mídia...")
    audio_clip = AudioFileClip(audio_temp)
    duracao = audio_clip.duration

    print("3/4 - Criando a estrutura do vídeo...")
    # Criando o clipe de imagem com a duração do áudio
    video_clip = ImageClip(imagem_entrada).with_duration(duracao)

    # Juntando o áudio ao vídeo
    video_final = video_clip.with_audio(audio_clip)

    print("4/4 - Renderizando o arquivo MP4 final...")
    video_final.write_videofile(
        video_saida, 
        fps=24, 
        codec="libx264", 
        audio_codec="aac"
    )
    
    # Fechando os arquivos para liberar o sistema
    video_final.close()
    audio_clip.close()
    print(f"\nSucesso absoluto! Vídeo salvo como: {video_saida}")

finally:
    # Remove o áudio temporário de qualquer forma
    if os.path.exists(audio_temp):
        os.remove(audio_temp)
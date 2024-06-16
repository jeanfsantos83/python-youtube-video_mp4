from pytube import YouTube

# URL do vídeo do YouTube
url = "https://www.youtube.com/watch?v=B2FXNgkdawE"

# Criar um objeto YouTube
yt = YouTube(url)

# Selecionar o melhor stream de vídeo em MP4
stream = yt.streams.filter(only_audio=False).first()

# Baixar o vídeo
stream.download(output_path="path/to/download/folder")
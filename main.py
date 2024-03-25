from moviepy.editor import VideoFileClip
import os


def create_thumbnails(video_folder, output_folder):
    # Verifica se a pasta de saída existe, senão, cria
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for video_file in os.listdir(video_folder):
        if not video_file.lower().endswith(
            (".mp4", ".mov", ".avi")
        ):  # Adicione mais extensões conforme necessário
            continue  # Ignora arquivos que não são vídeos

        video_path = os.path.join(video_folder, video_file)
        thumbnail_path = os.path.join(
            output_folder, os.path.splitext(video_file)[0] + "_thumbnail.jpg"
        )

        with VideoFileClip(video_path) as video:
            # Obtém um frame no meio do vídeo
            frame_time = video.duration / 2
            # Salva o frame como uma imagem JPEG
            video.save_frame(thumbnail_path, t=frame_time)

        print(f"Miniatura criada para: {video_file}")


# Caminho para a pasta com os vídeos
video_folder = "./video"
# Caminho para a pasta onde as miniaturas serão salvas
output_folder = "./imagens"
create_thumbnails(video_folder, output_folder)

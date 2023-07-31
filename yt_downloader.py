import os
from pytube import YouTube
from get_time import get_current_time


def download_mp3(youtube_url, output_path, file_name):
    try:
        yt = YouTube(youtube_url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        if audio_stream:
            audio_stream.download(output_path=output_path, filename=file_name)
            print(f"{get_current_time()}  Download started...")
            
            # Rename the downloaded file to add .mp3 extension
            saved_file = f"{output_path}/{file_name}"
            new_file_name = f"{output_path}/{file_name}.mp3"
            os.rename(saved_file, new_file_name)
            
            print(f"{get_current_time}  Download completed!")
        else:
            print(f"{get_current_time}  No audio stream available for the given URL.")

    except Exception as e:
        print(f"{get_current_time}  An error occurred: {str(e)}")

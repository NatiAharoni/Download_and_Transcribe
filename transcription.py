import whisper
from get_time import get_current_time

def transcribe_audio(file_path):
    print(f"{get_current_time}Transcription started...")
    model = whisper.load_model("base")
    result_text= model.transcribe(file_path)
    print(f"{get_current_time} transcription completed!")
    with open (f"{file_path}_transription.txt", "w") as f:
        f.write(result_text['text'])
    print(f"{get_current_time}  The audio file was successfully transcribed into a TXT file!")
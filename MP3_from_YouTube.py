import json
import customtkinter
from yt_downloader import download_mp3
from transcription import transcribe_audio    


def read_config_file():
    try:
        with open("config_file.json", "r") as config_file:
            config_data = json.load(config_file)
            return config_data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def download_and_transcribe():
    config_data = read_config_file()
    yt_url = entry.get()
    output_path = config_data.get("file_path", "")
    custom_file_name = 'Test3'
    download_mp3(yt_url, output_path, custom_file_name)
    output_path = output_path + "\\"
    transcribe_audio(output_path + custom_file_name + ".mp3")


if __name__ == "__main__":   
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.geometry("500x300")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text = "Fetch the Text from Youtube")
    label.pack(pady=12, padx=10)

    entry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter the Youtube URL")
    entry.pack(pady=12, padx=10)
    entry_value = entry.get()
    print(entry_value)

    button = customtkinter.CTkButton(master=frame, text="Download and Transcribe", command=download_and_transcribe)
    button.pack(pady=12, padx=10)

    root.mainloop()
    

    



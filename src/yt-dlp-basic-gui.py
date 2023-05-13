import tkinter as tk
from tkinter import filedialog
import yt_dlp as ytdl
import threading

def choose_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_label.config(text=directory)
        message_label.config(text="", fg="red")

def download_thread(ydl_opts, url):
    with ytdl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            message_label.config(text="Descarga completa", fg="green")
        except:
            message_label.config(text="Ha ocurrido un error en la descarga, intentelo nuevamente", fg="red")

def download_as(type):
    url = url_entry.get()
    if(not url or directory_label.cget("text") == "Sin Directorio Seleccionado"):
        message_label.config(text="Sin URL o Directorio seleccionado", fg="red")
        return
    output_path = directory_label.cget("text") + "/%(title)s.%(ext)s"
    message_label.config(text="Descargando...", fg="black")
    
    if(type):
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'outtmpl': output_path,
            'ffmpeg_location': 'ffmpeg_bin/'
        }
    else:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': 'ffmpeg_bin/'
        }

    threading.Thread(target=lambda: download_thread(ydl_opts,url)).start()


root = tk.Tk()
root.title("yt-dlp-gui")

url_label = tk.Label(root, text="URL:")
url_label.grid(row=0, column=0, columnspan=2)

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

directory_label = tk.Label(root, text="Sin Directorio Seleccionado")
directory_label.grid(row=2, column=0, columnspan=2)

directory_button = tk.Button(root, text="Elegir directorio", command=choose_directory)
directory_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

download_label = tk.Label(root, text="Descargar como:")
download_label.grid(row=4, column=0, columnspan=2)

mp3_button = tk.Button(root, text="MP3", command=lambda: download_as(0), width=10)
mp4_button = tk.Button(root, text="MP4", command=lambda: download_as(1), width=10)

mp3_button.grid(row=5, column=0, padx=10, pady=10)
mp4_button.grid(row=5, column=1, padx=10, pady=10)

message_label = tk.Label(root, text="", fg="red") 
message_label.grid(row=6, column=0, columnspan=2)

root.mainloop()


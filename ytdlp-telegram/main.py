import os
import shutil
import requests
from yt_dlp import YoutubeDL
from config import CONFIG


def upload():
    bot_token = CONFIG.BOT_TOKEN
    chat_id = CONFIG.CHAT_ID

    if not bot_token or not chat_id:
        print("[ ERROR CONFIG ]")
        return
    
    API_URL = f"https://api.telegram.org/bot{bot_token}"
    method = "sendAudio"

    file_name = os.listdir("downloads")[0]
    with open(f"downloads/{file_name}", "rb") as f:
        audio = {"audio": f.read()}

    data = {
        "chat_id": chat_id,
        "title": file_name,
        "caption": file_name,
        "parse_mode": "MARKDOWN"
    }

    try:
        r = requests.get(f"{API_URL}/{method}", data, files=audio)
        if r.status_code != 200:
            print(f"Error upload: {r.content}")
        else:
            print("Uploaded Successfully...!")
    except Exception as e:
        print(e)
    
    shutil.rmtree("downloads")


def download(url, upload_file=False):
    try:
        if not os.path.exists("downloads"):
            os.makedirs("downloads", exist_ok=True)
        
        options = {
            "format": "bestaudio[ext=mp3]/bestaudio/best",
            "outtmpl": "downloads/%(title)s.mp3"
        }

        ytdl = YoutubeDL(options)
        ytdl.download([url])

        if upload_file:
            upload()
    except Exception as e:
        print(e)


print(
    "----------------------------------------------\n"
    "       Welcome to Youtube MP3 downloader\n"
    "           Download and upload to telegram\n"
    "               original creator @bishalqx980\n"
    "---------------------------------------------------------"
)

while True:
    url = input("URL: ")
    if url == "q":
        quit()
    download(url, True)

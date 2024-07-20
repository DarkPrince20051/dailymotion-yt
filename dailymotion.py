import os
#sljedeću liniju koda treba instalirati preko cmd ili pypi.org
from yt_dlp import YoutubeDL

def download_video_to_yt_folder(url, download_path):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'format': 'best'
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', None)
            uploader = info_dict.get('uploader', None)
            upload_date = info_dict.get('upload_date', None)
            view_count = info_dict.get('view_count', None)
            
            print("Title:", title)
            print("Channel:", uploader)
            print("Published on:", upload_date)
            print("Views:", view_count)
        
        print("Download complete.")
    except Exception as e:
        print("An error occurred:", str(e))

# Define the base download path to the directory on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "josip polic", "yt")
print(f"Default download path is set to: {desktop_path}")

# Ensure the yt directory exists
if not os.path.exists(desktop_path):
    os.makedirs(desktop_path)

while True:
    url = input("Enter the Dailymotion URL: ")

    # Call the function to download the video
    download_video_to_yt_folder(url, desktop_path)

    choice = input("Želite li ponovno? (da/ne): ").lower()
    if choice != "da":
        break

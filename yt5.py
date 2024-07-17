from pytube import YouTube
import os

def download_video_to_yt_folder(url, download_path):
    try:
        yt = YouTube(url)

        print("Title:", yt.title)
        print("Channel:", yt.author)
        print("Published on:", yt.publish_date)
        print("Views:", yt.views)

        # Get the highest resolution stream
        yd = yt.streams.get_highest_resolution()

        # Download the video to the yt directory
        yd.download(download_path)

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
    url = input("Enter the YouTube URL: ")

    # Call the function to download the video
    download_video_to_yt_folder(url, desktop_path)

    choice = input("Želite li ponovno? (da/ne): ").lower()
    if choice != "da":
        break

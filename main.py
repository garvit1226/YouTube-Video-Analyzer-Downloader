import yt_dlp
import tkinter as tk
from tkinter import filedialog

def get_video_stats(url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        print("\nVIDEO STATS")
        print("-" * 40)

        # Format numbers with commas
        views = info.get('view_count')
        likes = info.get('like_count')
        comments = info.get('comment_count')

        views = f"{views:,}" if views else "N/A"
        likes = f"{likes:,}" if likes else "N/A"
        comments = f"{comments:,}" if comments else "N/A"

        # Format duration (sec → mm:ss)
        duration = info.get('duration')
        if duration:
            mins, secs = divmod(duration, 60)
            formatted_duration = f"{mins}:{secs:02d}"
        else:
            formatted_duration = "N/A"

        # Format date (YYYYMMDD → YYYY.MM.DD)
        upload_date = info.get('upload_date')
        if upload_date:
            formatted_date = f"{upload_date[:4]}.{upload_date[4:6]}.{upload_date[6:]}"
        else:
            formatted_date = "N/A"

        print("Title:", info.get('title'))
        print("Channel:", info.get('uploader'))
        print("Views:", views)
        print("Likes:", likes)
        print("Comments:", comments)
        print("Duration:", formatted_duration)
        print("Upload Date:", formatted_date)

        print("-" * 40)

        return True
    
    except Exception as e:
        print("Error fetching stats:", e)
        return False

def download_video(url, save_path):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'format': 'best[acodec!=none][vcodec!=none]',
        'quiet': True,          # hides most logs
        'no_warnings': True     # removes warnings
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Downloaded successfully!")
    except Exception as e:
        print("Error:", e)




def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

if __name__=="__main__":
    root = tk.Tk()
    root.withdraw()

    print("\n🎬 WELCOME TO YOUTUBE VIDEO ANALYZER 🎬")

    url = input("\nEnter YouTube URL for stats: ")
    print("\nFetching stats....")

    if get_video_stats(url):
        choice = input("\nDo you want to download this video? (yes/no): ").lower()

        if choice == "yes":
            

            print("Please select the folder to save the video : ")

            save_dir = open_file_dialog()

            if save_dir:
                print("Started Downloading.......")
                download_video(url,save_dir)
                print("Check the folder")
            else:
                print("Invalid save location")
    
        else:
            print("Thank You!!")
    




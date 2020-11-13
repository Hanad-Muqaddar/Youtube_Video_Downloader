from pytube import YouTube
import sys
link = input("Enter Link: ")
try: 
    yt = YouTube(link) 
except: 
    print("Connection Error")
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length,"seconds")
print("Ratings: ",yt.rating)
video = yt.streams.get_highest_resolution()
audio = yt.streams.get_audio_only()
print("Downloading ......")
# video.download("C:/Users/syedh/OneDrive/Desktop/Video")
print("Download Complete.")
sys.exit()

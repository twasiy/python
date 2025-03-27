from yt_dlp import YoutubeDL

link = input("Enter video link: ")
ydl_opts = {'format': 'best'}
with YoutubeDL(ydl_opts) as ydl:
    ydl.download(link)

print("Download successfully finished!")

from tkinter.filedialog import *
from moviepy import *  #.video.io.VideoFileClip import VideoFileClip
from tkinter import*

video = askopenfilename()

vid = VideoFileClip(video)
aud = vid.audio
aud.write_audiofile('capcut.mp3')



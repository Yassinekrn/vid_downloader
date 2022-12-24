from tkinter import *
from tkinter import filedialog

from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil  # copy files and folders and move them
# functions


def select_path():
    # allows user to select a path from the file explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget("text")  # gets path as txt
    screen.title("Downloading, Please Wait...")
    # Download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # move to selected dir
    shutil.move(mp4_video, user_path)
    screen.title("Download Complete! Try downloading another file.")


screen = Tk()
title = screen.title("Youtube Video Downloader")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# img logo
logo_img = PhotoImage(
    file='C:/Users/Krichen/Documents/GitHub/vid_downloader/youtube.png')
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 145, image=logo_img)

# link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download Link: ",
                   font=('Arial Rounded MT Bold', 15))

# select path for file saving
path_label = Label(screen, text="Select Path: ",
                   font=('Arial Rounded MT Bold', 15))

select_btn = Button(screen, text="Select", command=select_path)
# Add to window
canvas.create_window(250, 365, window=path_label)
canvas.create_window(250, 400, window=select_btn)


# add widget to window
canvas.create_window(250, 300, window=link_label)
canvas.create_window(250, 335, window=link_field)

# download btns
download_btn = Button(screen, text="Download File", command=download_file)

# add to canvas
canvas.create_window(250, 450, window=download_btn)
screen.mainloop()
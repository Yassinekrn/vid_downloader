from tkinter import *
from tkinter import filedialog
import os
from moviepy import *
from moviepy.editor import VideoFileClip
from moviepy.editor import *

from pytube import YouTube
from pytube import Playlist

import shutil  # copy files and folders and move them
# functions


def non_spc_carc(string):
    res = string
    for i in range(0, len(string)-1):
        if string[i] in ["\\", "/", ":", "*", "?", "<", ">", "|"]:
            res = res[0: i] + res[i+1: len(res)]
    return res


def select_path():
    # allows user to select a path from the file explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # type of download
    format_value = format_var.get()
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget("text")  # gets path as txt
    screen.title("Downloading, Please Wait...")
    # Download video
    if format_value == 1:
        YouTube(
            get_link).streams.get_lowest_resolution().download(filename='tmp_file.mp4')

        # shutil.move(audio_file, user_path)
        video = VideoFileClip('tmp_file.mp4')

        video.audio.write_audiofile(non_spc_carc(
            str(YouTube(get_link).title))+".mp3")
        video.close()
        os.remove('tmp_file.mp4')
        shutil.move(non_spc_carc(
            str(YouTube(get_link).title))+".mp3", user_path)

    elif format_value == 2:
        mp4_video = YouTube(
            get_link).streams.get_highest_resolution().download()
        vid_clip = VideoFileClip(mp4_video)
        vid_clip.close()
        # move to selected dir
        shutil.move(mp4_video, user_path)
    screen.title("Download Complete! Try downloading another file.")


def download_pl():
    # type of download
    format_value = format_var.get()
    # get user playlist link
    pl_link = pl_link_field.get()
    # get user path for downloads
    user_path = path_label.cget("text")  # gets path as txt
    if format_value == 2:
        # loop to download
        p = Playlist(pl_link)
        for video in p.videos:
            screen.title(f'Downloading: {video.title}')
            st = video.streams.get_highest_resolution().download()
            # move to selected dir
            shutil.move(st, user_path)
    elif format_value == 1:
        p = Playlist(pl_link)
        for video in p.videos:
            screen.title(f'Downloading: {video.title}')
            # audio_file = video.streams.get_audio_only().download()
            # shutil.move(audio_file, user_path)
            video.streams.get_lowest_resolution().download(filename='tmp_file.mp4')

            # shutil.move(audio_file, user_path)
            new_video = VideoFileClip("tmp_file.mp4")

            new_video.audio.write_audiofile(
                non_spc_carc(str(video.title))+".mp3")
            new_video.close()
            os.remove("tmp_file.mp4")
            shutil.move(non_spc_carc(str(video.title))+".mp3", user_path)

        screen.title("Download Complete! Try downloading another file.")


screen = Tk()
title = screen.title("Youtube Video Downloader")
canvas = Canvas(screen, width=500, height=600)
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

# playlist link field
pl_link_field = Entry(screen, width=50)
pl_link_label = Label(screen, text="Enter Playlist Link: ",
                      font=('Arial Rounded MT Bold', 15))

# add playlist widget to window
canvas.create_window(250, 500, window=pl_link_label)
canvas.create_window(250, 535, window=pl_link_field)

# select path for file saving
path_label = Label(screen, text="Select Path: ",
                   font=('Arial Rounded MT Bold', 15))

select_btn = Button(screen, text="Select", command=select_path)
# Add to window
canvas.create_window(250, 330, window=path_label)
canvas.create_window(250, 366, window=select_btn)

# Add checkbutton mp3 - mp4
format_var = IntVar()
mp3_radio = Radiobutton(text="MP3", variable=format_var, value=1)
canvas.create_window(175, 290, window=mp3_radio)
mp4_radio = Radiobutton(text="MP4", variable=format_var, value=2)
canvas.create_window(325, 290, window=mp4_radio)


# add widget to window
canvas.create_window(250, 405, window=link_label)
canvas.create_window(250, 435, window=link_field)

# download btns
download_btn = Button(screen, text="Download File", command=download_file)
pl_download_btn = Button(screen, text="Download Playlist", command=download_pl)

# add to canvas
canvas.create_window(250, 465, window=download_btn)
canvas.create_window(250, 565, window=pl_download_btn)
screen.mainloop()

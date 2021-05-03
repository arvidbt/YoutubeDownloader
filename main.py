# /home/arre/Code/python/ytdownload/downloads
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
from colors import *
from pytube import YouTube

#'https://youtu.be/dx9HutGJHAA'

window = Tk()
window.title("YouTube Downloader.")
window.maxsize(2000,1100)
window.config(bg=LIGHT_GRAY)
url = StringVar()
directorypath = StringVar()

def browse():
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    directorypath.set(download_directory)

def download():
    folder = directorypath.get()
    yt = YouTube(yt_url.get())

    videoStream = yt.streams.first()

    videoStream.download(folder)
    messagebox.showinfo("Download Succesful", "Video saved in:\n"+
                         folder)


UI_frame = Frame(window, width=1920, height=1080, bg=LIGHT_GRAY)

directory_path = Button(window, text='Choose download directory', command=browse, bg=RED)
directory_path.pack()

directory_path_entry = Entry(window, textvariable=directorypath)
directory_path_entry.pack()


yt_label = Label(window, text='Paste URL below.')
yt_label.pack()

yt_url =Entry(window, textvariable=url)
yt_url.pack()


yt_label_button = Button(window, text='Enter', command=download, bg=LIGHT_GREEN)
yt_label_button.pack()

#canvas = Canvas(window, width=1900, height=1080, bg=RED)
#canvas.grid(row=1,column=0, padx=10, pady=5)

window.mainloop()
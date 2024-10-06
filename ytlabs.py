import tkinter
import customtkinter
from pytubefix import YouTube
import ssl

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        print("Download Complete!")
    except Exception as e:
        print(f'An error occurred: {e}')


#System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

#App Frame
root = customtkinter.CTk()
root.geometry("720x720")
root.title('Youtube to Mp4 Downloader')

#UI elements
title = customtkinter.CTkLabel(root, text="Insert a YouTube link", fg_color="transparent", pady="20")
title.pack()

#Link input
link = customtkinter.CTkEntry(root, placeholder_text="Input Youtube Link", width=500, height=30, corner_radius=10)
link.pack()

#Download button
download_button = customtkinter.CTkButton(root, text="Download", command=startDownload, width=300)
download_button.pack(pady=30)


root.mainloop()

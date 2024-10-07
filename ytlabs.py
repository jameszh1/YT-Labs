import tkinter
import customtkinter
from pytubefix import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        print("Download Complete!")
    except Exception as e:
        print(f'An error occurred: {e}')


def videoInfo():
    ytLink = link.get()
    ytObject = YouTube(ytLink)
    title = ytObject.title
    views = ytObject.views
    length = ytObject.length
    infoLabel.configure(text=f"Youtube Video Details:\nTitle: {title}\nViews: {views}\nLength: {length}\n")


#System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

#App Frame
root = customtkinter.CTk()
root.geometry("720x720")
root.title('Youtube to Mp4 Downloader')

#UI elements
title = customtkinter.CTkLabel(root, text="Insert a YouTube link", fg_color="transparent", pady="30")
title.pack()

#Link Entry input
link = customtkinter.CTkEntry(root, placeholder_text="Input Youtube Link", width=500, height=30, corner_radius=10)
link.pack()

#Buttons Frame (together)
button_frame = customtkinter.CTkFrame(root)
button_frame.pack(pady=20)
download_button = customtkinter.CTkButton(button_frame, text="Download", command=startDownload, width=300)
fetch_info_button = customtkinter.CTkButton(button_frame, text="Fetch Video Details", command=videoInfo, width=300)
download_button.pack(side="left", padx=5)
fetch_info_button.pack(side="left", padx=5)

#progress bar
progress_var = tkinter.DoubleVar()
progress_bar = customtkinter.CTkProgressBar(root, variable=progress_var, width=300)
progress_bar.pack(pady=20)

#Display information about the YouTube Video
infoFrame = customtkinter.CTkFrame(root, corner_radius=10, fg_color="grey", width=600)
infoFrame.pack_propagate(False)
infoFrame.pack()
infoLabel = customtkinter.CTkLabel(infoFrame, text="Youtube Video Details...", font=("Arial",16, "bold"))
infoLabel.pack(pady=10)

root.mainloop()

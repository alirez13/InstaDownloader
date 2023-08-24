import os
import threading
import instaloader
# from tkinter import *
# from tkinter import filedialog, messagebox
# from tkinter import ttk

from customtkinter import *
from customtkinter import filedialog
from CTkMessagebox import *


root = CTk()
root.title('Instagram Donwloader')
root.geometry('400x200')
root.resizable(0, 0)


def downloadPost():
    link = postlink_Entry.get()

    def download():
        if 'https://www.instagram.com/p/' in link:
            try:
                location = filedialog.askdirectory()
                os.chdir(location)
                URL = link.replace('https://www.instagram.com/p/', '')
                URL = URL.replace('/', '')
                CTkMessagebox(title="Info", message='Downloading')
                # progressbar = CTk.Progressbar(mode="determinate")
                # progressbar.place(x=80, y=40, width=190)
                # progressbar.start()
                l = instaloader.Instaloader()
                post = instaloader.Post.from_shortcode(l.context, URL)

                l.download_post(post, target=link)
                # progressbar.destroy()
                CTkMessagebox(title="Info", message='The download is finished')
            except:
                CTkMessagebox(title="Error", message='There is no mail with this address')
        else:
            profile_name = link
            location = filedialog.askdirectory()
            os.chdir(location)
            CTkMessagebox(title="Info", message='Downloading')
            # progressbar = CTkProgressBar(master=root)
            # progressbar.pack()
            # progressbar.start()
            instaloader.Instaloader().download_profile(profile_name, profile_pic_only=False)
            # progressbar.destroy()
            CTkMessagebox(title="Info", message='The download is finished')

    threading.Thread(target=download).start()


postlink_Entry = CTkEntry(root, placeholder_text='Post Link', font=('Roboto', 16), width=300)
downloadPost_btn = CTkButton(root, text='Download', text_color='white', font=('Roboto', 16), command=downloadPost)
exit_btn = CTkButton(root, text='Exit', text_color='white', font=('Roboto', 16), command=root.destroy)

postlink_Entry.pack(pady=12, padx=10)
downloadPost_btn.pack(pady=6, padx=10)
exit_btn.pack(pady=6, padx=10)

root.mainloop()

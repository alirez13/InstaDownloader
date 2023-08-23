import os
import threading
import instaloader
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk

root = Tk()
root.title('اینستا دانلودر')
root.geometry('400x200')
root.resizable(0, 0)
root.config(bg='#121212')


def downloadPost():
    link = postlink_Entry.get()

    def download():
        if 'https://www.instagram.com/p/' in link:
            try:
                location = filedialog.askdirectory()
                os.chdir(location)
                URL = link.replace('https://www.instagram.com/p/', '')
                URL = URL.replace('/', '')
                messagebox.showinfo('اطلاعات', '  در حال دانلود')

                progressbar = ttk.Progressbar(mode="determinate")
                progressbar.place(x=80, y=40, width=190)
                progressbar.start()
                l = instaloader.Instaloader()
                post = instaloader.Post.from_shortcode(l.context, URL)

                l.download_post(post, target=link)
                progressbar.destroy()
                messagebox.showinfo('اطلاعات', 'دانلود تمام شد')

            except:
                messagebox.showerror('خطا', 'پستی با این آدرس وجود ندارد')

        else:
            profile_name = link
            location = filedialog.askdirectory()
            os.chdir(location)
            messagebox.showinfo('اطلاعات', '  در حال دانلود')
            progressbar = ttk.Progressbar(mode="determinate")
            progressbar.place(x=80, y=40, width=190)
            progressbar.start()
            instaloader.Instaloader().download_profile(profile_name, profile_pic_only=False)
            progressbar.destroy()
            messagebox.showinfo('اطلاعات', 'دانلود تمام شد')

    threading.Thread(target=download).start()


postlink_label = Label(root, text='لینک پست', bg='#121212', fg='white', font=('Arial', 13))
postlink_Entry = Entry(root, width=30)

downloadPost_btn = Button(root, text='دانلود', bg='#121212', fg='white', borderwidth=3, font=('Arial', 11), width=30,
                          command=downloadPost)
exit_btn = Button(root, text='خروج', bg='#121212', fg='white', borderwidth=3, font=('Arial', 11), width=30,
                  command=root.destroy)

postlink_label.grid(row=0, column=0, padx=10, pady=10)
postlink_Entry.grid(row=0, column=1)

downloadPost_btn.place(relx=0.5, rely=0.4, anchor='c')
exit_btn.place(relx=0.5, rely=0.6, anchor='c')

root.mainloop()

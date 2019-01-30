import urllib.request
import tkinter as tk
from tkinter import messagebox

#Callbacks
def download():
    imgInput = urlVar.get().split(" ")
    
    for index, url in enumerate(imgInput):
        link = urllib.request.urlopen(url)
        try:
            name = "image%s.jpg" % (index+1)
            with open(name, "wb") as output:
                output.write(link.read())
        except IOError:
            print("Unable to create %s" % name)
    tk.messagebox.showinfo("Success!", "%a Images Downloaded." % len(imgInput))

win = tk.Tk()
win.title("Bulk Image Downloader")
win.resizable(False, False)

#Labels
urlLabel = tk.Label(win, text="Paste image URL, separated by space")
urlLabel.grid(row=0, column=0)

#Entry
urlVar = tk.StringVar()
urlBox = tk.Entry(win, width=50, textvariable=urlVar)
urlBox.grid(row=1, column=0)

#Button
downloadButton = tk.Button(win, text="Download", command=download)
downloadButton.grid(row=2, column=0)

win.mainloop()

import tkinter as tk
from main import downloadVidio, downloadAudio, downloadPlaylist
# import threading

def submit(audioOnly, playlist):
    url = urlEntry.get()
    audioOnly = bool(audioOnly.get())
    playlist = bool(playlist.get())
    if not playlist:
        result = downloadVidio(url, audioOnly)
    else:
        result = downloadPlaylist(url, audioOnly)
    resultLabel['text'] = f'{result}'

window = tk.Tk()
message = ''
inputFrame = tk.Frame(master=window)
urlLabel = tk.Label(master=inputFrame, text='Enter URL')
urlEntry = tk.Entry(master=inputFrame, width=100)
optionsFrame = tk.Frame(master=window)
audioOnly = tk.IntVar()
playlist = tk.IntVar()
playlistBox = tk.Checkbutton(master=optionsFrame, text='Playlist', variable=playlist)
audioOnlyBox = tk.Checkbutton(master=optionsFrame, text='Audio Only', variable=audioOnly)

urlLabel.grid(row=0, column=0, sticky='w')
urlEntry.grid(row=1, column=0, sticky='w')
audioOnlyBox.grid(row=1, column=0)
playlistBox.grid(row=0, column=0)
submitBtn = tk.Button(master=window, text='Submit', command= lambda: submit(audioOnly, playlist))
resultLabel = tk.Label(master=window, text=message)

inputFrame.grid(row=0, column=0, columnspan=2, padx=10)
optionsFrame.grid(row=1, column=0, padx=10)
submitBtn.grid(row=2, column=0, padx=10)
resultLabel.grid(row=2, column=1, padx=10)

window.mainloop()
# window = tk.Tk()

# def handle_keypress(event):
#     print(event.char)

# window.bind('b', handle_keypress)

# window.mainloop()

# class DownloaderGui:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.loop = self.window.mainloop()

# class ThreadOne(threading.Thread):
#     def __init__(self, threadID):
#         threading.Thread.__init__(self)
#         self.threadID = threadID

#     def run(self):
#         gui = DownloaderGui()

# thread1 = ThreadOne(1)
# thread2 = ThreadOne(2)
# thread1.start()
# thread2.start()
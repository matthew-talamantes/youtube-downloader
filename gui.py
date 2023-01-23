import tkinter as tk
# import threading

def submit():
    url = urlEntry.get()
    resultLabel['text'] = f'You submitted: {url}'

window = tk.Tk()
message = ''
inputFrame = tk.Frame(master=window)
urlLabel = tk.Label(master=inputFrame, text='Enter URL')
urlEntry = tk.Entry(master=inputFrame, width=100)

urlLabel.grid(row=0, column=0, sticky='w')
urlEntry.grid(row=1, column=0, sticky='w')
submitBtn = tk.Button(master=window, text='Submit', command=submit)
resultLabel = tk.Label(master=window, text=message)

inputFrame.grid(row=0, column=0, columnspan=2, padx=10)
submitBtn.grid(row=1, column=0, padx=10)
resultLabel.grid(row=1, column=1, padx=10)

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
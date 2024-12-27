from gtts import gTTS
import os
import tkinter as tk


def getinput():
    inp = inputtext.get(1.0, "end-1c")
    return inp


def texttospeech():
    mytext = getinput()
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("start welcome.mp3")


frame = tk.Tk()
frame.title("Text to Speech Convertor")
frame.geometry('400x200')

label = tk.Label(frame, text="Please enter the text you want to convert to speech: ")
label.pack()

inputtext = tk.Text(frame,
                    height=5,
                    width=20)
inputtext.pack()

playButton = tk.Button(frame,
                       text="Play",
                       command=lambda: [texttospeech(), frame.destroy()])
playButton.pack()

frame.mainloop()

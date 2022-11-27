import pyttsx3
from tkinter import *

root = Tk()

def ozvychka(event):
    ccc = entry.get()
    dd = pyttsx3.init()
    dd.say(ccc)
    dd.runAndWait()

button = Button(root, text='нажми и озвучат твой текст')
button.pack()

entry = Entry(root)
entry.pack()



button.bind('<Button-1>', ozvychka)
root.mainloop()


'''eg = pyttsx3.init()
eg.say('k')
eg.runAndWait()'''

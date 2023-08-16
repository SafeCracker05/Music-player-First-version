import tkinter as tk 
import fnmatch
import os
from pygame import mixer

window = tk.Tk()
window.title("Spotify Music")
window.geometry("600x800")
window.config(bg = 'black')

#rootpath est le lien du fichier contenant toute les music.
rootpath = r"/Users/yaniv/Desktop/Projet spotify Music python/Music"

#pattern est le pattern de fin en commun qu'il y'a entre tout les noms du music.
pattern = "*.mp3"

#initialisation du mixer.
mixer.init()

#initialisation des icon pour gerer la musique.
prev_img = tk.PhotoImage(file = "previous.png")
stop_img = tk.PhotoImage(file = "next_img.png")
pause_img = tk.PhotoImage(file = "pause.png")
play_img = tk.PhotoImage(file = "next_img.png")
next_img = tk.PhotoImage(file = "next.png")

def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(os.path.join(rootpath, listBox.get("anchor")))
    mixer.music.play()
def stop():
    mixer.music.stop()
    listBox.select('active')
def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)
def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def pause_song():
    if pausebutton["text"] == "Pause":
        mixer.music.pause()
        pausebutton["text"] == "Play"
    else:
        mixer.music.unpause()
        pausebutton["text"] == "Pause"


#c'est la list qui affiche et contient toute les liste du fichier musique qu'ont extorque a l'aide de la loop.
listBox = tk.Listbox(window, fg = "cyan", bg = "black", width = 100, font = ('ds-digital', 18))

listBox.pack(padx = 15, pady = 15)

#c'est un label qui est vide de base mais lorsque la musique est lancer le nom du titre s'affiche.
label = tk.Label(window, text = '', bg = 'black', fg = 'yellow', font = ('ds-digital', 18))
label.pack(pady = 15)

#c'estce qui permet de les centrer et les coller a l'horyzontal.
top = tk.Frame(window, bg = "white")
top.pack(padx = 10, pady = 5, anchor = 'center')

#toute les buttons pour gerer la music [play, previous, next, pause, stop]
prevbutton = tk.Button(window, text = "Prev", image = prev_img, bg = 'black', borderwidth = 0, command = play_prev)
prevbutton.pack(pady = 15, in_ = top, side = 'left')

stopbutton = tk.Button(window, text = "Stop", image = stop_img, bg = 'black', borderwidth = 0, command = stop)
stopbutton.pack(pady = 15, in_ = top, side = 'left')

playbutton = tk.Button(window, text = "Play", image = play_img, bg = 'black', borderwidth = 0, command = select)
playbutton.pack(pady = 15, in_ = top, side = 'left')

pausebutton = tk.Button(window, text = "Pause", image = pause_img, bg = 'black', borderwidth = 0, command = pause_song)
pausebutton.pack(pady = 15, in_ = top, side = 'left')

nextButton = tk.Button(window, text = "Next", image = next_img, bg = 'black', borderwidth = 0, command = play_next)
nextButton.pack(pady = 15, in_ = top, side = 'left')


for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)


window.mainloop()

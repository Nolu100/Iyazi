from tkinter import*
from tkinter import Tk
from tkinter import filedialog
import pygame
import os

window = Tk()
window.geometry("500x300")
window.title("Music Player")
window.config(bg="white")
pygame.mixer.init

song_listbox=Listbox(window,bg="purple",fg="white",width="60")
song_listbox.pack(pady=20)


def add_songs():
    song =filedialog.askopenfilename(initialdir="C:/Music/",title="Choose a song", filetypes=(("mp3 files","*.mp3"),))
    song_listbox.insert(END,song)
    song =song.replace("C:/Music/","")
    song =song.replace(".mp3","")

   
def play_song():
    song =song_playlist.get(ACTIVE)
    print =f"C:/Music(song).mp3"
    pygme.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.play(loops=0) 

previous_btn_img = PhotoImage(file=r"C:/images/previous.png")

next_btn_img = PhotoImage(file=r"C:/images/next.png")


play_btn_img = PhotoImage(file=r"C:/images/play.png")

pause_btn_img = PhotoImage(file=r"C:/images/pause.png")

stop_btn_img = PhotoImage(file=r"C:/images/stop.png")

controls_frame=Frame(window)
controls_frame.pack()

#Buttons
previous_btn=Button(controls_frame,image=previous_btn_img,borderwidth=0,padx=10,pady=10 )
previous_btn.grid(column=0,row=0)

next_btn=Button(controls_frame,image=next_btn_img,borderwidth=0 ,padx=10,pady=10)
next_btn.grid(column=1,row=0)

play_btn=Button(controls_frame,image=play_btn_img,borderwidth=0,padx=10,pady=10 )
play_btn.grid(column=2,row=0)

pause_btn=Button(controls_frame,image=pause_btn_img,borderwidth=0,padx=10,pady=10 )
pause_btn.grid(column=3,row=0)

stop_btn=Button(controls_frame,image=stop_btn_img,borderwidth=0,padx=10,pady=10 )
stop_btn.grid(column=4,row=0)
               

my_menu=Menu(window)
window.config(menu=my_menu)

add_songs_menu=Menu(my_menu)
my_menu.add_cascade(label="Add songs", menu=add_songs_menu)
add_songs_menu.add_command(label="add song to playlist",command=add_songs)


window.mainloop()






from tkinter import*
window = Tk()

text1 = Label(window,text="Username")
text1.grid(column=0,row=1)

text2 =Label(window,text="Password")
text2.grid(column=0,row=2)

ent = Entry(window)
ent.grid(column=1,row=1)

ent2 =Entry(window)
ent2.grid(column=1,row=2)

but =Button(window,text="Login",bg="pink",fg="black",padx=10,pady=10)
but.grid(column=1,row=3)

window.mainloop()

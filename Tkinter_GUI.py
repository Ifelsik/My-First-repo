from tkinter import *


def clicked():
	a=int(txt.get())
	a*=2
	lbl.configure(text=a)

w=Tk()
w.geometry('250x250')

txt=Entry(w, width=7)
txt.grid(column=0, row=1)
btn=Button(w, text="btn", command=clicked)
btn.grid(column=0, row=0)
lbl=Label(w, text="")
lbl.grid(column=0, row=2)

w.mainloop()
from tkinter import *
import rocket_computation as RC

def clicked():
	L=float(In_L.get())
	l=float(In_l.get())
	d=float(In_d.get())
	a=float(In_a.get())
	cm=float(In_cm.get())
	St=float(In_St.get())	
	lbl.configure(text=L)
	
w=Tk()
w.geometry('250x250')

In_L=Entry(w, width=7)
In_L.grid(column=0, row=1)
In_l=Entry(w, width=7)
In_l.grid(column=0, row=2)
In_d=Entry(w, width=7)
In_d.grid(column=0, row=3)
In_a=Entry(w, width=7)
In_a.grid(column=0, row=4)
In_cm=Entry(w, width=7)
In_cm.grid(column=0, row=5)
In_St=Entry(w, width=7)
In_St.grid(column=0, row=6)

btn=Button(w, text="compute", command=clicked)
btn.grid(column=0, row=0)

lbl=Label(w, text="None")
lbl.grid(column=0, row=2)

w.mainloop()
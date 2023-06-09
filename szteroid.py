from tkinter import*
foablak = Tk()

menubar = Menu(foablak)
filemenu = Menu(menubar, tearoff=0)
menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="BMI Kalkulátor", menu=menu)
menubar.add_cascade(label="Edzésterv", menu=menu)
menubar.add_cascade(label="Étrend", menu=menu)
menubar.add_cascade(label="Kalória deficit", menu=menu)
menubar.add_cascade(label="Szteroid", menu=menu)

foablak.config(menu=menubar)






foablak.mainloop()
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

txt1 = Label(foablak, text="Fitness")
txt2 = Label(foablak, text="Üdvözöljük az oldalunkon, reméljük a segítségére lehetünk.")


can1=Canvas(foablak, width=500, height=500,)
photo=PhotoImage(file="fooldal.png")
item=can1.create_image(250,250, image=photo)
can1.grid(row=5, column=3, rowspan=5, padx=10, pady=10)
 
txt1.grid(row=0, column=3,)
txt2.grid(row=1, column=3)

foablak.mainloop()
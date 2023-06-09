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
txt3 = Label(foablak, text="Tulajdonosok: Terdik Zalán, Somlyai Tamás, Mihó André")
txt4 = Label(foablak, text="Elérhetőségek:")
txt5 = Label(foablak, text="1. Telefonszám: +36309876543")
txt6 = Label(foablak, text="2. E-mail: Fitness@gmail.com")
txt7 = Label(foablak, text="3. Cím: Kis Feri utca 56 Mucsaröcsöge 9999")



can1=Canvas(foablak, width=500, height=500,)
photo=PhotoImage(file="fooldal.png")
item=can1.create_image(250,250, image=photo)
can1.grid(row=2, column=0, pady=0)
 
txt1.grid(row=0, column=0,)
txt2.grid(row=1, column=0,)
txt3.grid(row=10, column=0, sticky=W)
txt4.grid(row=11, column=0, sticky=W)
txt5.grid(row=12, column=0, sticky=W)
txt6.grid(row=13, column=0, sticky=W)
txt7.grid(row=14, column=0, sticky=W)

foablak.mainloop()
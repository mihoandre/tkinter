from tkinter import*

foablak=Tk()
foablak.title("Foki Zoltán")
foablak.minsize(width=300, height=100)

menusor=Frame(foablak)
menusor.grid(side=TOP, fill=X)

menu1=Menubutton(menusor, text="BMI kalkulátor")
menu1.grid(side=LEFT)
a=Menu(menu1)
menu1.config(menu=a)

menu2=Menubutton(menusor, text="Edzésterv")
menu2.grid(side=LEFT)
b=Menu(menu2)
menu2.config(menu=b)

menu3=Menubutton(menusor, text="Étrend")
menu3.grid(side=LEFT)
c=Menu(menu3)
c.add_command(label="Documents")
c.add_command(label="Messages")
c.add_command(label="Sign Out")
menu3.config(menu=c)

menu4=Menubutton(menusor, text="Kalória deficit")
menu4.grid(side=LEFT)
d=Menu(menu4)
menu4.config(menu=d)

menu5=Menubutton(menusor, text="Szteroid")
menu5.grid(side=LEFT)
e=Menu(menu5)
menu5.config(menu=e)

can1=Canvas(foablak, width=500, height=500, bg="white")
photo=PhotoImage(file="Főoldalkép.png")
item=can1.create_image(250,250, image=photo)
can1.grid(row=1, column=3, rowspan=3, padx=10, pady=5)

foablak.mainloop()
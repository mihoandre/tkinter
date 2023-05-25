from tkinter import*

foablak=Tk()
foablak.title("Foki Zoltán")
foablak.minsize(width=300, height=100)

menusor=Frame(foablak)
menusor.pack(side=TOP, fill=X)

menu1=Menubutton(menusor, text="BMI kalkulátor")
menu1.pack(side=LEFT)
a=Menu(menu1)
menu1.config(menu=a)

menu2=Menubutton(menusor, text="Edzésterv")
menu2.pack(side=LEFT)
b=Menu(menu2)
menu2.config(menu=b)

menu3=Menubutton(menusor, text="Étrend")
menu3.pack(side=LEFT)
c=Menu(menu3)
c.add_command(label="Documents")
c.add_command(label="Messages")
c.add_command(label="Sign Out")
menu3.config(menu=c)

menu4=Menubutton(menusor, text="Kalória deficit")
menu4.pack(side=LEFT)
d=Menu(menu4)
menu4.config(menu=d)

menu5=Menubutton(menusor, text="Szteroid")
menu5.pack(side=LEFT)
e=Menu(menu5)
menu5.config(menu=e)

foablak.mainloop()
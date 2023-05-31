from tkinter import*

foablak=Tk()
foablak.title("Foki Zoltán")
foablak.minsize(width=300, height=100)

menusor=Frame(foablak)
menusor.place(x=5, y=0)

menu1=Menubutton(menusor, text="BMI kalkulátor")
menu1.place(x=5, y=0)
a=Menu(menu1)
menu1.config(menu=a)

menu2=Menubutton(menusor, text="Edzésterv")
menu2.place(x=5, y=0)
b=Menu(menu2)
menu2.config(menu=b)

menu3=Menubutton(menusor, text="Étrend")
menu3.place(x=5, y=0)
c=Menu(menu3)
c.add_command(label="Documents")
c.add_command(label="Messages")
c.add_command(label="Sign Out")
menu3.config(menu=c)

menu4=Menubutton(menusor, text="Kalória deficit")
menu4.place(x=5, y=0)
d=Menu(menu4)
menu4.config(menu=d)

menu5=Menubutton(menusor, text="Szteroid")
menu5.place(x=5, y=0)
e=Menu(menu5)
menu5.config(menu=e)

can1=Canvas(foablak, width=500, height=500, bg="white")
photo=PhotoImage(file="Főoldalkép.png")
item=can1.create_image(250,250, image=photo)
can1.place(height=3, width=4, anchor="center", relx=10, rely=5)

foablak.mainloop()
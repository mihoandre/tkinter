from tkinter import *

foablak =Tk()
foablak.title('Étrend')
foablak.minsize(width =400,height=500)
txt1=Label(foablak,text='Mi a célja az étrendel?')
txt2=Label(foablak,text='Étrend')
var1 =IntVar()
var2 =IntVar()
txt3=Label(foablak,text='Az általunk össze állított étrend tömegnöveléshez (60-70kg-ig).')
jelolo1 =Checkbutton(foablak,text='Tömegnövelés',variable =var1)
jelolo2 =Checkbutton(foablak,text='Diéta',variable =var2)
jelolo3 =Checkbutton(foablak,text='Csirkemell,rizs(2700kalória/nap)',variable =var1)
jelolo4 =Checkbutton(foablak,text='Tejszines csirke, tésztával(2700 kalória/nap)',variable =var1)
jelolo6 =Checkbutton(foablak,text='Rántott sertés comb, salátával+bármilyen körettel(2700 kalória/nap)',variable =var1)
jelolo7 =Checkbutton(foablak,text='pulyka mell+krumpli+zöldség (2700kalória/nap)',variable =var1)
jelolo8 =Checkbutton(foablak,text='Bolognai(2700 kalória/nap)',variable =var1)
jelolo1.grid(row=3,sticky=W)
jelolo2.grid(row=4,sticky=W)
jelolo3.grid(row=6,sticky=W)
jelolo4.grid(row=7,sticky=W)
jelolo6.grid(row=9,sticky=W)
jelolo7.grid(row=10,sticky=W)
jelolo8.grid(row=11,sticky=W)
txt1.grid(row=2,sticky=W)
txt2.grid(row=1,sticky=W)
txt3.grid(row=5,sticky=E)


foablak.mainloop()
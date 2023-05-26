from tkinter import *

foablak =Tk()
foablak.title('Étrend')
foablak.minsize(width =400,height=500)
txt1=Label(foablak,text='Mi a célja az étrendel?')
var1 =IntVar()
var2 =IntVar()
jelolo1 =Checkbutton(foablak,text='Tömegnövelés',variable =var1)
jelolo2 =Checkbutton(foablak,text='Diéta',variable =var2)
jelolo1.grid(row=4)
jelolo2.grid(row=5)
txt1.grid(row =2,sticky =E)



foablak.mainloop()
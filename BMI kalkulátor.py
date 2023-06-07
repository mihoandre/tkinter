''' https://www.tutorialspoint.com/python/tk_radiobutton.htm# '''

from tkinter import*
from math import*

def bmikalk():
    testtomeg=eval(mezo1.get)
    testmagassag=eval(mezo2.get)
    bmikiszamolas=testtomeg//(testmagassag*testmagassag)
    

bmiabl=Tk()

txt1=Label(bmiabl, text="Testtömeg index (BMI) kalkulátor")
txt2=Label(bmiabl, text="Kérem jelölje be a nemét:")
txt3=Label(bmiabl, text="Adja meg a testtömegét (KG):")
txt4=Label(bmiabl, text="Adja meg a testmagasságát (CM):")
txt5=Label(bmiabl, text="Férfi")
txt6=Label(bmiabl, text="Nő")
txt7=Label(bmiabl, text="Az Ön testtömeg indexe:")
txt8=Label(bmiabl, text="Az Ön ideális testtömege:")
txt9=Label(bmiabl, text="Osztályozás (Kg/m2) \n  Súlyos soványság  <16  \n  Mérsékelt soványság     16,0 - 16,99  \n  Enyhe soványság     17,0 - 18,49  \n  Normális testsúly     18,5 - 24,99  \n  Túlsúly     25,0 - 29,99     \n  I. fokú elhízás    30,0 - 34,99  \n  II.fokú elhízás     35,0 - 39,99  \n  III. fokú elhízás     >40")
radiogomb1=Radiobutton(bmiabl, text="Férfi", command=bmikalk)
radiogomb2=Radiobutton(bmiabl, text="Nő", command=bmikalk)
mezo1=Entry(bmiabl)
mezo2=Entry(bmiabl)
mezo3=Entry(bmiabl)
mezo4=Entry(bmiabl)
mezo5=Entry(bmiabl)
gomb1=Button(bmiabl, text="Kiszámít", command=bmikalk)

txt1.grid(row=1, column=2)
txt2.grid(row=2, column=1)
txt3.grid(row=3, column=1)

gomb1.grid(row=4, column=2)

mezo1.grid(row=2, column=2)
mezo2.grid(row=3, column=2)

radiogomb1.grid(row=1, column=3)
radiogomb2.grid(row=2, column=3)

bmiabl.mainloop()
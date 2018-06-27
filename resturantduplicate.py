import tkinter as tk
from  tkinter import *
import random



exquant1 = 0
exquant2 = 0
exquant3 = 0
exquant4 = 0
totq1=0
totq2=0
totq3=0
totq4=0
tot=0
totq=[]
stuff=[]
stuff1=[]
out=[]
dic={}
op =''
dn = ''
sgst=9
cgst=9
billno=0


#=================================================================================================================
def write(dic):

    file=open('rest.txt','w')
    for i in range(0,4):
        if(totq[i]!=0):
            file.write( stuff1[i]+'%d' %dic[stuff[i]])
            file.write("\n")
    file.close()


def read():
    global out
    file = open('rest.txt','r')
    for line in file:
        readd=line[:-1]
        out.append(readd)
        orderout.config(text=out)
    file.close()
    print(out)



def quant1(op):
    global exquant1
    if(op=='+'):
        exquant1 +=1
    else:
        if(exquant1==0):
            exquant1=0
        else:
            exquant1-=1
    burgerq.config(text=exquant1)

def quant2(op):
    global exquant2
    if(op=='+'):
        exquant2 +=1
    else:
        if(exquant2==0):
            exquant2=0
        else:
            exquant2-=1
    momoq.config(text=exquant2)
def quant3(op):
    global exquant3
    if(op=='+'):
        exquant3 +=1
    else:
        if(exquant3==0):
            exquant3=0
        else:
            exquant3-=1
    tikkiq.config(text=exquant3)
def quant4(op):
    global exquant4
    if(op=='+'):
        exquant4 +=1
    else:
        if(exquant4==0):
            exquant4=0
        else:
            exquant4-=1
    paneerrollq.config(text=exquant4)

def done1(dn):
    global totq
    global totq1
    global totq2
    global totq3
    global totq3
    global totq4
    global stuff
    global stuff1
    global exquant1

    totq1=exquant1*20
    totq2=exquant2*30
    totq3=exquant3*15
    totq4=exquant4*30
    totq=[totq1,totq2,totq3,totq4]
    dic={'BURGER':totq1,'MOMOS':totq2,'TIKKI':totq3,'PANEER ROLL':totq4}
    stuff=['BURGER','MOMOS','TIKKI','PANEER ROLL']
    stuff1 = ['BR', 'MM', 'TK', 'PR']
    write(dic)


def totalAmount():
    global totq
    global tot

    for j in range (0,4):
        tot+=totq[j]
    totalout.config(text=tot)
    sgstv = tot * (sgst/100)
    cgstv = sgstv
    tot +=(sgstv*2)
    nettotalout.config(text = tot)
def billNo():
    global billNumscr
    billno = 0
    billno = random.randint(9712980, 9950876)
    billNumscr.config(text= billno)
    sgstvalue.config(text=sgst)
    cgstvalue.config(text=cgst)
    totalAmount()
    read()




mainWindow = tk.Tk()
mainWindow.geometry("1600x700+0+0")
#============================================heading===========================================================
rstinfo = tk.Label(font=( 'aria' ,30, 'bold' ),text="Restaurant Management System",fg="steel blue",bd=10)
rstinfo.grid(row=0,columnspan=4,padx=1,pady=1,ipadx=5,ipady=5)
#=============================================menue============================================================
rstmenu = tk.Label(font=( 'aria' ,30, 'bold' ),text="MENU",fg="steel blue")
rstmenu.grid(row=1,columnspan=4,padx=1,pady=1,ipadx=5,ipady=5,)
#==============================================labels==========================================================
items = tk.Label(font=( 'aria' ,25, 'bold' ),text="ITEMS",fg="black")
items.grid(row=2,column=1,padx=1,pady=1,ipadx=5,ipady=5,)

addq = tk.Label(font=( 'aria' ,25, 'bold' ),text="ADD",fg="black")
addq.grid(row=2,column=2,padx=1,pady=1,ipadx=5,ipady=5,)
subq = tk.Label(font=( 'aria' ,25, 'bold' ),text="SUB",fg="black")
subq.grid(row=2,column=3,padx=1,pady=1,ipadx=5,ipady=5,)


quantity = tk.Label(font=( 'aria' ,20, 'bold' ),text="QUANTITY",fg="BLACK")
quantity.grid(row=2,column=4,padx=1,pady=1,ipadx=5,ipady=5,)

#==============================================eatables==========================================================
photo1 = PhotoImage(file = 'Burger.png' )
burgerimg = tk.Label(mainWindow,image = photo1)
burgerimg.grid(row =3, column = 0, padx = 1, pady = 1, ipadx = 5, ipady = 5 )
burger = tk.Label(mainWindow,text = 'Burger \n Rs 20',font=('Comic Sans MS', 15, 'bold'),height = 2, width = 5)
burger.grid(row=3,column = 1,padx=1,pady=1,ipadx=5,ipady=5)
burgeradd = tk.Button(mainWindow,text = '+',height = 1, width = 2,command = lambda:quant1('+'))
burgeradd.grid(row=3,column = 2,padx=5,pady=5,ipadx=5,ipady=5)
burgersub = tk.Button(mainWindow,text = '-',height = 1, width = 2,command = lambda:quant1('-'))
burgersub.grid(row=3,column = 3,padx=5,pady=5,ipadx=5,ipady=5)
burgerq = tk.Button(mainWindow,text = 0,height = 2, width = 15,relief ='sunken',borderwidth = 5,bg="powder blue" ,justify='right')
burgerq.grid(row=3,column = 4,padx=5,pady=5,ipadx=5,ipady=5)



photo2 = PhotoImage(file = 'momos.png' )
momoimg = tk.Label(mainWindow,image = photo2)
momoimg.grid(row =4, column = 0, padx = 1, pady = 1, ipadx = 5, ipady = 5 )
momo = tk.Label(mainWindow,text = 'Momo \n Rs 30',font=('Comic Sans MS', 15, 'bold'),height = 2, width = 5)
momo.grid(row=4,column = 1,padx=1,pady=1,ipadx=5,ipady=5)
momoadd = tk.Button(mainWindow,text = '+',height = 1, width = 2,command = lambda:quant2('+'))
momoadd.grid(row=4,column = 2,padx=5,pady=5,ipadx=5,ipady=5)
momosub = tk.Button(mainWindow,text = '-',height = 1, width = 2,command = lambda:quant2('-'))
momosub.grid(row=4,column = 3,padx=5,pady=5,ipadx=5,ipady=5)
momoq = tk.Button(mainWindow,text = 0,height = 2, width = 15,relief ='sunken',borderwidth = 5,bg="powder blue" ,justify='right')
momoq.grid(row=4,column = 4,padx=5,pady=5,ipadx=5,ipady=5)


photo3 = PhotoImage(file = 'Tikki.png' )
tikkiimg = tk.Label(mainWindow,image = photo3)
tikkiimg.grid(row =5, column = 0, padx = 1, pady = 1, ipadx = 5, ipady = 5 )
tikki = tk.Label(mainWindow,text = 'Tikki \n Rs 15',font=('Comic Sans MS', 15, 'bold'),height = 2, width = 5)
tikki.grid(row=5,column = 1,padx=1,pady=1,ipadx=5,ipady=5)
tikkiadd = tk.Button(mainWindow,text = '+',height = 1, width = 2,command = lambda:quant3('+'))
tikkiadd.grid(row=5,column = 2,padx=5,pady=5,ipadx=5,ipady=5)
tikkisub = tk.Button(mainWindow,text = '-',height = 1, width = 2,command = lambda:quant3('-'))
tikkisub.grid(row=5,column = 3,padx=5,pady=5,ipadx=5,ipady=5)
tikkiq = tk.Button(mainWindow,text = 0,height = 2, width = 15,relief ='sunken',borderwidth = 5,bg="powder blue" ,justify='right')
tikkiq.grid(row=5,column = 4,padx=5,pady=5,ipadx=5,ipady=5)


photo4 = PhotoImage(file = 'Paneerroll.png' )
paneerrollimg = tk.Label(mainWindow,image = photo4)
paneerrollimg.grid(row =6, column = 0, padx = 1, pady = 1, ipadx = 5, ipady = 5 )
paneerroll = tk.Label(mainWindow,text = 'Paneer Roll \n Rs 30',font=('Comic Sans MS', 15, 'bold'),height = 2, width = 8)
paneerroll.grid(row=6,column = 1,padx=1,pady=1,ipadx=5,ipady=5)
paneerrolladd = tk.Button(mainWindow,text = '+',height = 1, width = 2,command = lambda:quant4('+'))
paneerrolladd.grid(row=6,column = 2,padx=5,pady=5,ipadx=5,ipady=5)
paneerrollsub = tk.Button(mainWindow,text = '-',height = 1, width = 2,command = lambda:quant4('-'))
paneerrollsub.grid(row=6,column = 3,padx=5,pady=5,ipadx=5,ipady=5)
paneerrollq = tk.Button(mainWindow,text = 0,height = 2, width = 15,relief ='sunken',borderwidth = 5,bg="powder blue" ,justify='right')
paneerrollq.grid(row=6,column = 4,padx=5,pady=5,ipadx=5,ipady=5)

#=========================================================================================================================


placeorder = tk.Button(mainWindow, font=('ariel', 10, 'bold'),height = 2, width = 15,text='PLACE ORDER',relief ='raised',bd = 5,bg="powder blue",command = lambda:done1(']') )
placeorder.grid(row=7,column = 4,padx=5,pady=5,ipadx=5,ipady=5)


billNum = tk.Label(mainWindow, font=('aria', 10, 'bold'), text="BILL NO.", fg="black", bd=5)
billNum.grid(row=0, column=6)
billNumscr = tk.Button(mainWindow, height=1, width=15, relief='sunken', borderwidth=5, bg="powder blue")
billNumscr.grid(row=0, column=7, padx=5, pady=5, ipadx=5, ipady=5)

sgstlabel = tk.Label(mainWindow, font=('aria', 10, 'bold'), text="SGST %", fg="black", bd=5)
sgstlabel.grid(row=1, column=6)
sgstvalue = tk.Button(mainWindow, height=1, width=15, relief='sunken', borderwidth=5, bg="powder blue")
sgstvalue.grid(row=1, column=7, padx=5, pady=5, ipadx=5, ipady=5)

cgstlabel = tk.Label(mainWindow, font=('aria', 10, 'bold'), text="CGST %", fg="black", bd=5)
cgstlabel.grid(row=1, column=8)
cgstvalue = tk.Button(mainWindow, height=1, width=15, relief='sunken', borderwidth=5, bg="powder blue")
cgstvalue.grid(row=1, column=9, padx=5, pady=5, ipadx=5, ipady=5)


orderlabel = tk.Label(mainWindow, font=('aria', 10, 'bold'), text="ORDER", fg="black", bd=5)
orderlabel.grid(row=2, column=7)
orderout = tk.Button(mainWindow, height=2, width=30, relief='sunken', borderwidth=5, bg="powder blue")
orderout.grid(row=3, column=7, padx=5, pady=5, ipadx=5, ipady=5)


total = tk.Label(mainWindow, font=('aria', 10, 'bold'), text="TOTAL", fg="black", bd=5)
total.grid(row=4, column=6)
totalout = tk.Button(mainWindow, height=1, width=15, relief='sunken', borderwidth=5, bg="powder blue")
totalout.grid(row=4, column=7, padx=5, pady=5, ipadx=5, ipady=5)

nettotal = tk.Label(mainWindow, font=('aria', 10, 'bold'), text="TOTAL (TAX INC)", fg="black", bd=5)
nettotal.grid(row=5, column=6)
nettotalout = tk.Button(mainWindow, height=1, width=15, relief='sunken', borderwidth=5, bg="powder blue")
nettotalout.grid(row=5, column=7, padx=5, pady=5, ipadx=5, ipady=5)


btnbill = tk.Button(mainWindow , bd=5, fg="black", font=('ariel', 10, 'bold'),height = 2, width=15, text="BILL",bg="powder blue", command=lambda:billNo())
btnbill.grid(row=7, column=3,padx=5,pady=5,ipadx=5,ipady=5)



mainWindow.mainloop()

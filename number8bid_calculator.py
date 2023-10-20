from tkinter import *
from tkinter import colorchooser
window = Tk()
window.geometry("320x280")
window.title("Number 8 bid final payment calculator v1.2 by Joe") # My link: https://github.com/codingmanj

check = StringVar()
check1 = StringVar()

def submit_tellme(event=None):
    result = round((float(amountEntry.get())*1.15*1.15),2)
    finalpaymenttext.config(text=result)
window.bind("<Return>",submit_tellme)

def clearme(event=None):
    amountEntry.delete(0,END)
window.bind("<Up>",clearme)

def clearme_result(event=None):
    finalpaymenttext.config(text="")
window.bind("<Down>",clearme_result)

def backspace():
    amountEntry.delete(len(amountEntry.get())-1,END)

def whatistheamount():
    result = check.get()
    label_amounttopayplatform_text.config(text=result)

def whatistheamountgst():
    result = check1.get()
    label_amounttopaygst_text.config(text=result)

def bgcolor():
    window.config(bg=colorchooser.askcolor()[1])

def label_amounttopayplatform_color():
    label_amounttopayplatform.config(bg=colorchooser.askcolor()[1])

def label_amounttopaygst_color():
    label_amounttopaygst.config(bg=colorchooser.askcolor()[1])

def createwindow():
    newwindows = Tk()
    newwindows.geometry("320x280")
    newwindows.title("Some auction rules")
    rules = Label(newwindows,text="Inspection is highly recommended\nas buyers are responsible for determining for\nthemselves of any item's condition or functionality.").pack()

amountlabel = Label(window,
                    text="Auction\nAmount:",
                    compound='right')

amountEntry = Entry(window,
                    font=('verdana',16),
                    width=5,
                    )

sumbitbutton = Button(window,
                      text='To be paid?',
                      command=submit_tellme)

clearbutton = Button(window,
                      text='Clear amount',
                      command=clearme)

backspacebutton = Button(window,
                      text='Backspace',
                      command=backspace)

clearresultbutton = Button(window,
                      text='Clear result',
                      command=clearme_result)

bgcolorbutton = Button(window,
                       text="Change bg color",
                       command=bgcolor)

newwindowbutton = Button(window,
                       text="Some auction rules",
                       command=createwindow).pack(anchor=E,side=BOTTOM)


label_amounttopayplatform_color_button = Button(window,
                       text="Change number8\ncheckbox bg color",
                       command=label_amounttopayplatform_color)

label_amounttopaygst_color_button= Button(window,
                       text="Change GST\ncheckbox bg color",
                       command=label_amounttopaygst_color)

checkbox_amounttopayplatform = Checkbutton(window,
                                           onvalue="15%",
                                           offvalue="",
                                           variable=check,
                                           command=whatistheamount)

label_amounttopayplatform = Label(window,
                    text="+ Number8 charge %",
                    bg='red')

checkbox_amounttopaygst = Checkbutton(window,
                                           onvalue="15%",
                                           offvalue="",
                                           variable=check1,
                                           command=whatistheamountgst,)

label_amounttopaygst= Label(window,
                    text="+ GST %",
                    bg='yellow')

label_amounttopayplatform_text = Label(window,
                         font=('verdana',8),
                         text="")

label_amounttopaygst_text = Label(window,
                         font=('verdana',8),
                         text="")

finalpaymentlabel = Label(window,
                          text="is actual amount\nto be paid.")

finalpaymenttext = Label(window,
                         font=('verdana',16),
                         text="",
                         )

amountlabel.place(x=2,y=1)
amountEntry.place(x=60,y=5)
sumbitbutton.place(x=140,y=5)
bgcolorbutton.pack(anchor=W,side=BOTTOM)
label_amounttopayplatform_color_button.pack(anchor=W,side=BOTTOM)
label_amounttopaygst_color_button.pack(anchor=W,side=BOTTOM)
clearbutton.place(x=2,y=40)
backspacebutton.place(x=90,y=40)
clearresultbutton.place(x=160,y=40)
#----------------
label_amounttopayplatform_text.place(x=2,y=70)
label_amounttopaygst_text.place(x=2,y=100)
checkbox_amounttopayplatform.place(x=35,y=70)
label_amounttopayplatform.place(x=60,y=70)
checkbox_amounttopaygst.place(x=35,y=100)
label_amounttopaygst.place(x=60,y=100)


#-----------------

finalpaymentlabel.pack(anchor=SE,side=BOTTOM)
finalpaymenttext.pack(anchor=SE,side=RIGHT)
mainloop()
from tkinter import *
import random

root=Tk()
root.geometry('500x500')
root.title("background color changer")

key={'color':['maroon1','lawn green', 'magenta2','purple1','springgreen2','chocolate1','deep pink','cyan','red']}



def color():
    rand_back=random.randint(0,8)
    root.configure(background=key['color'][rand_back])
    


btn=Button(root,text="generate color",command=color)

btn.pack()














root.mainloop()
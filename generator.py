from msilib.schema import CheckBox
import random
from tkinter import *
import string
import tkinter
window = Tk()
window.title('Nagaja s password generator')
window.geometry('500x500')

Label(window,font=('bold',10),text='PASSWORD GENERATOR').pack()


len1=tkinter.IntVar()
len2=tkinter.IntVar()
len3=tkinter.IntVar()

def password_generate(leng):
    valid_char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_'
    password=''.join(random.sample(valid_char,leng))
    l =Label(window, text = password, font=('bold', 20),bg='white')
    l.place(x=180,y=50)

def get_len():
    if len1.get() == 4:
        password_generate(4)
    elif len2.get() == 6:
        password_generate(6)
    elif len3.get() == 8:
        password_generate(8)
    else:
        password_generate(6)

Button(window,text='Generate',font=('Bold',10), bg='purple',command=get_len).place(x=200,y=100)

Checkbutton(bg='green',text='4 character',onvalue=4, offvalue=0,variable=len1).place(x=200,y=150)
Checkbutton(bg='red',text='6 character',onvalue=6, offvalue=0,variable=len2).place(x=200,y=170)
Checkbutton(bg='violet',text='8 character',onvalue=8, offvalue=0,variable=len3).place(x=200,y=190)

window.mainloop()
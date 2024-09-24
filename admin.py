import os
from tkinter import *
from tkinter import messagebox
from tkinter import *
import pymysql
from tkinter import messagebox, filedialog
import cv2
import mysql.connector as mysql

import matplotlib.pyplot as plt

import tk as tk
from PIL import Image, ImageTk
import tkinter as tk
from cvlib.object_detection import draw_bbox

global act1
from main import ViewData
def act():
    x = Admin.get()
    y = password.get()
    if x.__eq__("Admin") and y.__eq__("Admin"):
        s1="login successfully"
        messagebox.showinfo("success",s1)
        winadmin.destroy()
        land = ViewData()
        # exec(open("dataupload.py").read())


    else:
        messagebox.showinfo("login failed")


winadmin = Tk()
winadmin.title("Image Forgery Detection")
winadmin.maxsize(width=800, height=900)
winadmin.minsize(width=800, height=900)
winadmin.configure(bg='#34bfbb')

image1 = Image.open("2.jpg")
img = image1.resize((800, 900))

test = ImageTk.PhotoImage(img)

label1 = tk.Label(winadmin, image=test)
label1.image = test

# Position image
label1.place(x=1, y=1)

# image1 = Image.open("3.png")
test = ImageTk.PhotoImage(img)

label1 = tk.Label(winadmin, image=test)
label1.image = test

# Create Canvas
# canvas1 = Canvas(win, width=400, height=400)

# canvas1.pack(fill="both", expand=True)

# Display image
# canvas1.create_image(0, 0, image=bg, anchor="nw")

Label(winadmin, text='Image Forgery Detection using SIFT Model', bg="#ffb366", font='verdana 15 bold') \
    .place(x=250, y=150)

Admin = Label(winadmin, text="Admin", bg="#34bfbb", width=10, font='Verdana 10 bold')
Admin.place(x=210, y=320)

password = Label(winadmin, text="password", bg="#34bfbb", width=10, font='Verdana 10 bold')
password.place(x=210, y=370)

# Entry Box ------------------------------------------------------------------

Admin = StringVar()
password = StringVar()

Admin = Entry(winadmin, width=30, bg="silver", show='*', textvariable=Admin)
Admin.place(x=400, y=370)

password = Entry(winadmin, width=30, bg="silver", textvariable=password)
password.place(x=400, y=320)

Button(winadmin, text="login", font='Verdana 10 bold', bg="#34bfbb", command=act).place(x=340, y=520)
winadmin.mainloop()



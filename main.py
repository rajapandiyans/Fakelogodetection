
from skimage import filters, feature

import imagehash
from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pymysql
import csv
from csv import writer
import os
from skimage.filters.edges import prewitt_h, prewitt_v
from skimage.io import imread, imshow
from PIL import ImageTk, Image

class ViewData:
    def __init__(self):
        def dataupload():

            global filename1
            f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
            filename1 = filedialog.askopenfilename(filetypes=f_types)
            if(filename1.__len__()<1):

                msg = "Image Not Selected"
                messagebox.showinfo("Success", msg)
            else:
                msg = "Image uploded Sucessfully"
                messagebox.showinfo("Success", msg)

        def viewdata():

            im = cv2.imread(filename1)
            plt.imshow(im)
            plt.show()
            msg = "Feature Extracted Sucessfully"
            messagebox.showinfo("Success", msg)

        def viewdata1():
            image2 = imread(filename1, as_gray=True)
            plt.imshow(image2)
            plt.show()
            msg = "Grayscale Conversion Sucess"
            messagebox.showinfo("Success", msg)

        def viewdata2():
            image2 = imread(filename1, as_gray=True)
            pre_hor = prewitt_h(image2)
            pre_ver = prewitt_v(image2)
            # Sobel Kernel
            ed_sobel = filters.sobel(image2)
            # Datamining algorithm
            can = feature.canny(image2)

            plt.imshow(can, cmap='gray');
            plt.show()
            msg = "Intrest Point Extraction Sucess"
            messagebox.showinfo("Success", msg)

        def viewdata3():

            image2 = cv2.imread(filename1)
            gray1 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

            # keypoints
            sift = cv2.SIFT_create()
            keypoints_1, descriptors_1 = sift.detectAndCompute(image2, None)

            print(descriptors_1)
            img_1 = cv2.drawKeypoints(gray1, keypoints_1, image2)

            plt.imshow(img_1)
            plt.show()
            msg = "Key Point Extracted"
            messagebox.showinfo("Success", msg)

        def act2():
            global vehnorth
            f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
            filename1 = filedialog.askopenfilename(filetypes=f_types)
            pathSpecified = "D:\Fakelogodetect\Train_dataset"
            fnames = os.listdir(pathSpecified)
            # print(listOfFileNames)
            count = 0
            similarity = 80
            threshold = 1 - similarity / 100
            with Image.open(filename1) as img:
                hash1 = imagehash.average_hash(img)
                print(hash1)
            for image in fnames:
                with Image.open(os.path.join("D:\Fakelogodetect\Train_dataset", image)) as img1:
                    hash2 = imagehash.average_hash(img1)
                    print("Similarity Checking", hash2)
                    if hash1 == hash2:
                        count = 1
                        print("{} image found {}% similar to {}".format(image, similarity, filename1))

            if count == 1:
                # print("Logo is Original ")
                s1="Original"
                messagebox.showinfo("success",s1)
            else:
                # print("Logo is Not Origianl ")
                s1 = "Fake"
                messagebox.showinfo(" success",s1)



        win = Tk()

        # app title
        win.title("Image Forgery Detection")

        # window size
        win.maxsize(width=1500, height=800)
        win.minsize(width=1500, height=800)

        win.configure(bg='#59B5B4')
        image1 = Image.open("1.png")
        img = image1.resize((700, 400))
        test = ImageTk.PhotoImage(img)

        label1 = tk.Label(win, image=test)
        label1.image = test

        # Position image
        label1.place(x=230, y=250)

        # image1 = Image.open("3.png")
        test = ImageTk.PhotoImage(img)

        label1 = tk.Label(win, image=test)
        label1.image = test

        heading = Label(win, text="Image Forgery Detection using SIFT Model", font='Verdana 20 bold')
        heading.place(x=230, y=60)

        btnbrowse = Button(win, text="Train Image Upload", font=' Verdana 10 bold', command=lambda: dataupload())
        btnbrowse.place(x=70, y=170)

        btncamera = Button(win, text="Feature Extraction", font='Verdana 10 bold', command=lambda: viewdata())
        btncamera.place(x=260, y=170)

        btnsend = Button(win, text="Grayscale Conversion", font='Verdana 10 bold', command=lambda: viewdata1())
        btnsend.place(x=430, y=170)

        btnsend = Button(win, text="Intrest Point Extraction", font='Verdana 10 bold', command=lambda: viewdata2())
        btnsend.place(x=650, y=170)
        btnsend = Button(win, text="Keypoint Descriptor", font='Verdana 10 bold', command=lambda: viewdata3())
        btnsend.place(x=850, y=170)

        btnsend = Button(win, text="Forgery Detection", font='Verdana 10 bold', command=lambda: act2())
        btnsend.place(x=1050, y=170)


        win.mainloop()


from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x790+0+0")
        self.root.title("face Recognition System")
        
        title_lbl=Label(self.root,text=" HELP DESK ",font=("times new roman",40,"bold"),bg="green",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=55)
        
        img_top=Image.open(r"college_images\hd.jpeg")
        img_top=img_top.resize((1300,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1300,height=720)
        
        dev_label=Label(f_lbl,text="Email:ritikmishra80040@gmail.com",font=("times new roman",25,"bold"),bg="light blue")
        dev_label.place(x=530,y=370)
        
        
        
  
        
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()                     
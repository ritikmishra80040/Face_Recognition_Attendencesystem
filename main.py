from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x790+0+0")
        self.root.title("face Recognition System")
        
        #1st 
        img=Image.open(r"college_images\17.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #2nd
        img1=Image.open(r"college_images\6.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #3rd
        img2=Image.open(r"college_images\3.jpg")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        #big image
        img3=Image.open(r"college_images\a2.jpg")
        img3=img3.resize((1300,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1300,height=710)
        
        title_lbl=Label(bg_img,text="FACE   RECOGNITION   ATTENDANCE   SYSTEM ",font=("times new roman",35,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        #=============== time ====================
        def time(): 
            string = strftime('%H:%M:%S:%p')
            lbl.config(text=string)
            lbl.after(1000,time)
            
        lbl=Label(bg_img,font=('time new roman',28,'bold'),bg="black",fg='red')
        lbl.place(x=460,y=45,width=300,height=60)
        time()      
   
        #student button
        img4=Image.open(r"college_images\11.jpg")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)     
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=150,y=100,width=150,height=150)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details, cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=150,y=210,width=150,height=40)
        
        
        #detect face button
        img5=Image.open(r"college_images\2.jpg")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)     
        
        b1=Button(bg_img,image=self.photoimg5,command=self.face_data,cursor="hand2")
        b1.place(x=400,y=100,width=150,height=150)
        
        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=400,y=210,width=150,height=40)
        
        
        #Attendance button
        img6=Image.open(r"college_images\19.jpg")
        img6=img6.resize((150,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)     
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=650,y=100,width=150,height=150)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=650,y=210,width=150,height=40)
        
        
        #Help button
        img7=Image.open(r"college_images\14.jpg")
        img7=img7.resize((150,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)     
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=900,y=100,width=150,height=150)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=900,y=210,width=150,height=40)
        
        
        #Train face button
        img8=Image.open(r"college_images\4.jpg")
        img8=img8.resize((150,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)     
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=150,y=280,width=150,height=150)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=150,y=390,width=150,height=40)
        
        
        #Photo face button
        img9=Image.open(r"college_images\7.jpg")
        img9=img9.resize((150,150),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)     
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=280,width=150,height=150)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=400,y=390,width=150,height=40)
        
        
       
         #Developer face button
        img10=Image.open(r"college_images\16.jpg")
        img10=img10.resize((150,150),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)     
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.devloper_data)
        b1.place(x=650,y=280,width=150,height=150)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.devloper_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=650,y=390,width=150,height=40)
        
        
         #Exit face button
        img11=Image.open(r"college_images\15.jpg")
        img11=img11.resize((150,150),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)     
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=900,y=280,width=150,height=150)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=900,y=390,width=150,height=40)
    
    def open_img(self):
        os.startfile("data") 
        
       
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition"," Are you sure exit this app",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
                                    
#==============================Function buttons=======================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)    
        
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)    
               
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)    
                     
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def devloper_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)    
                  
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)   
                             
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
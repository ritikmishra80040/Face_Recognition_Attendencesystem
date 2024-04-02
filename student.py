from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x790+0+0")
        self.root.title("face Recognition System")
        
        
        #================= variables=========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        #1st 
        img=Image.open(r"college_images\a5.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #2nd
        img1=Image.open(r"college_images\a4.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #3rd
        img2=Image.open(r"college_images\a2.jpg")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        #big image
        img3=Image.open(r"college_images\a6.jpg")
        img3=img3.resize((1300,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1300,height=710)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="red",fg="blue")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1250,height=600)
        
        # left lable frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=610,height=440)
        
        img_left=Image.open(r"college_images\a2.jpg")
        img_left=img_left.resize((610,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=608,height=130)
        
        
        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=0,y=10,width=608,height=140)
        
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CSE","ECE","IT","ME","MBA","BCA","BBA")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
        # Course
        Course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        Course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        Course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly")
        Course_combo["values"]=("Select Course ","B.Tech","MBA","BA","B.Sc")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        # Year
        Year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly")
        Year_combo["values"]=("Select Year ","2021-22","2022-23","2023-24","2024-25")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        # Semester
        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly")
        Semester_combo["values"]=("Select Semester ","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #class Student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=0,y=120 ,width=608,height=450)
        
        # student id   
        studentId_label=Label(class_student_frame,text="Student Id:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)
        
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        # student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=15)
        div_combo["values"]=("A","B","C","D","E","F")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        
        # roll no
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        # Gender
        Gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=15)
        gender_combo["values"]=("Male ","Female","Custem")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=10,sticky=W)
        
        
        # DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        # Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        # phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        # Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        # Teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        
        #radio Buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="yes")
        radionbtn1.grid(row=6,column=0)
        
        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1)
        
        # buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=215,width=607,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=245,width=607,height=35)
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=30,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Update Photo Sample",width=30,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=1)
        
         # right lable frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=10,width=610,height=440)
        
        img_right=Image.open(r"college_images\b2.jpg")
        img_right=img_right.resize((610,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=0,y=0,width=608,height=130)
        
        # ===searching system====
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=0,y=135,width=600,height=60)
        
        search_label=Label(Search_frame,text="Search By:",width=8,font=("times new roman",15,"bold"),bg="blue",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
         
        search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select ","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,width=10,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        
        search_btn=Button(Search_frame,text="Search",width=9,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn=Button(Search_frame,text="Show All",width=9,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
        
        #====table frame=======
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=0,y=210,width=600,height=200)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL) 
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll_no","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll_no",text="Roll_No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo Sample")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll_no",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    #=================== function decration==================
    def add_data(self):    
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Ritik@9125",database="ritikdb")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                                                 self.var_dep.get(),
                                                                                                                 self.var_course.get(),
                                                                                                                 self.var_year.get(),
                                                                                                                 self.var_semester.get(),
                                                                                                                 self.va_std_id.get(),
                                                                                                                 self.var_std_name.get(),
                                                                                                                 self.var_div.get(),
                                                                                                                 self.var_roll.get(),
                                                                                                                 self.var_gender .get(),
                                                                                                                 self.var_dob.get(),
                                                                                                                 self.var_email.get(),
                                                                                                                 self.var_phone.get(),
                                                                                                                 self.var_address.get(),
                                                                                                                 self.var_teacher.get(),
                                                                                                                 self.var_radio1.get()
                                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)  
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        
        
        
    #============== fetch data ===========
    def fetch_data(self):   
        conn=mysql.connector.connect(host="localhost",username="root",password="Ritik@9125",database="ritikdb")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 
           
   #============== get cursor ===========
    def get_cursor(self,event=""): 
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),         
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[5]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),
        
    #==============update function==========
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)  
                if Update>0:
                    
                    conn=mysql.connector.connect(host="localhost",username="root",password="Ritik@9125",database="ritikdb")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                    
                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                            self.var_gender .get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.va_std_id.get()
                                                                                                                                                                        ))                                                                   
                else:
                    if not Update:
                        return                                                                                                                                                   
                messagebox.showinfo("Success","Student details successfylly update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()                                                                                                                                                      
            except Exception as es:
               messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 
                                                   
   # ==============delete data=========
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id must be requred",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Ritik@9125",database="ritikdb")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 
    # reset data 
    def reset_data(self):
        self.var_dep.set("Select Department")   
        self.var_course.set("Select Course")                   
        self.var_year.set("Select Year")   
        self.var_semester.set("Select Semester")   
        self.va_std_id.set("")   
        self.var_std_name.set("")   
        self.var_div.set("Select Division")   
        self.var_roll.set("")   
        self.var_gender.set("Male")   
        self.var_dob.set("")   
        self.var_email.set("")   
        self.var_phone.set("") 
        self.var_address.set("")   
        self.var_teacher.set("") 
        self.var_radio1.set("") 

        
    #============= Generate data set or Take a samples===========
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Ritik@9125",database="ritikdb")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from Student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                    
                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                            self.var_gender .get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.va_std_id.get()==id+1
                                                                                                                                                                        ))                                                                   
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
               # ===== Load   predifiend data on face frontals from opencv
               
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum Neighbor=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!!!!")
            except Exception as es:
               messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)     
                    
  
  
  
                        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
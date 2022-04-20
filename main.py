from tkinter import*
from tkinter import ttk 
from PIL import Image , ImageTk
import tkinter
from click import command
from cv2 import destroyAllWindows
from helpdesk import Helpdesk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from Attendance import Attendance
from developer import Developer
from helpdesk import Helpdesk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        #first img
        img=Image.open(r"img/sathya2.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second img
        img1=Image.open(r"img/facescan2.png")
        img1=img1.resize((525,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=525,y=0,width=500,height=130)

        #third img
        img2=Image.open(r"img/sathya2.1.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg img
        img3=Image.open(r"img/back.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font =("times new roman",35,"bold"),bg = "white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button img
        img4=Image.open(r"img/student3.jpg")
        img4=img4.resize((170,170),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=170,height=170)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font =("times new roman",15,"bold"),bg = "black",fg="white")
        b1_1.place(x=200,y=270,width=170,height=30)

        #detect face button
        img5=Image.open(r"img/facedet2.jpg")
        img5=img5.resize((170,170),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=170,height=170)

        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font =("times new roman",15,"bold"),bg = "black",fg="white")
        b2_1.place(x=500,y=270,width=170,height=30)

        #attendance button
        img6=Image.open(r"img/attendence.jpg")
        img6=img6.resize((170,170),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=100,width=170,height=170)

        b3_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font =("times new roman",15,"bold"),bg = "black",fg="white")
        b3_1.place(x=800,y=270,width=170,height=30)

        #help desk
        img7=Image.open(r"img/helpdesk.jpg")
        img7=img7.resize((170,170),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command= self.helpdesk_data)
        b4.place(x=1100,y=100,width=170,height=170)

        b4_1=Button(bg_img,text="Help Desk",cursor="hand2",font =("times new roman",15,"bold"),bg = "black",fg="white")
        b4_1.place(x=1100,y=270,width=170,height=30)

        #Train Face
        img8=Image.open(r"img/trainface3.jpg")
        img8=img8.resize((170,170),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=350,width=170,height=170)

        b5_1=Button(bg_img,text="Train Face",cursor="hand2",command=self.train_data,font =("times new roman",15,"bold"),bg = "black",fg="white")
        b5_1.place(x=200,y=520,width=170,height=30)

        #Photos
        img9=Image.open(r"img/students2.webp")
        img9=img9.resize((170,170),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=350,width=170,height=170)

        b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font =("times new roman",15,"bold"),bg = "black",fg="white")
        b6_1.place(x=500,y=520,width=170,height=30)
        
        #Developer
        img10=Image.open(r"img/developer.jpg")
        img10=img10.resize((170,170),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command = self.developer_data)
        b7.place(x=800,y=350,width=170,height=170)

        b7_1=Button(bg_img,text="Developer",cursor="hand2",font =("times new roman",15,"bold"),bg = "black",fg="white")
        b7_1.place(x=800,y=520,width=170,height=30)

        #Quit
        img11=Image.open(r"img/exit2.jpg")
        img11=img11.resize((170,170),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit)
        b8.place(x=1100,y=350,width=170,height=170)

        b8_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font =("times new roman",15,"bold"),bg = "black",fg="white")
        b8_1.place(x=1100,y=520,width=170,height=30)


    def open_img(self):
        os.startfile("data")

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition ","Are you sure exit this project")
        if self.exit>0:
            self.root.destroy()
        else:
            return


#==============================Function Buttons================================
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
    
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def helpdesk_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Helpdesk(self.new_window)









if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
        

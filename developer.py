from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        title_lbl = Label(self.root, text="DEVELOPER", font=(
            "times new roman", 35, "bold"), bg="white", fg="orange")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"img/bg developer.jpg")
        img_top = img_top.resize((1530, 700), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=700)
#frame-------------------------------
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1030, y=0, width=500, height=700)

        img_top1 = Image.open(r"img/developerpic1.jpg")
        img_top1 = img_top1.resize((200, 200), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)


        # Developer
        dev_label = Label(main_frame,text="Hello!      \n I am Tharun.R", font=("times new roman", 25, "bold"), bg="white")
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame, text="Skill-(Python Developer)", font=("times new roman", 20, "bold"), bg="white")
        dev_label.place(x=0, y=90)







if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()

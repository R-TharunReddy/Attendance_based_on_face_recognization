from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Helpdesk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="orange")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"img/helpdesk1.jpg")
        img_top = img_top.resize((1530, 700), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=700)

        dev_label = Label(f_lbl, text="EMAIL: tharunreddyramigani@gmail.com", font=("times new roman", 25, "bold"), bg="white")
        dev_label.place(x=0, y=5)












if __name__ == "__main__":
    root = Tk()
    obj =Helpdesk(root)
    root.mainloop()
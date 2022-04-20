
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from numpy import place
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

def main():

    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"img/loginbg.jpg")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=314, height=450)

        img1 = Image.open(r"img/user2.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # label------------------
        username = lbl = Label(frame, text="Username", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = lbl = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

# iconimg----------------25
        img2 = Image.open(r"img/user55.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"img/padloc.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=395, width=25, height=25)

        # login btn--------------------------------
        loginbtn = Button(frame, text="Login", font=("times new roman", 15, "bold"), command=self.login,
                          bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # register btn-------------------------------
        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=(
            "times new roman", 10, "bold"), bd=3, borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="red")
        registerbtn.place(x=15, y=350, width=160)

        # forget btn-------------------------------
        forgetbtn = Button(frame, text="Forget Password",command=self.forgot_password_window, font=("times new roman", 10, "bold"), bd=3,
                           borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="red")
        forgetbtn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):

        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All field's required")
        elif self.txtuser.get() == "tharun" and self.txtpass.get() == "reddy":
            messagebox.showinfo("Success", "Welcome to Our Community")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="root", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from face_recognizer.register where email=%s and password=%s", (
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
            ))

            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Inavalid Username & password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return


                conn.commit()
                conn.close()
#reseet pas------------------------------------
    def reset_pass(self):
        if self.combo_securiy_Q.get() == "Select":
            messagebox.showerror(
                "Error", "Select sucurity Quetion", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror(
                "Error", "Plase enter the answer", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror(
                "Error", "Please enter the new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="root", database="face_recognizer")
            my_cursor = conn.cursor()
            qury = (
                "select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue =(self.txtuser.get(), self.combo_securiy_Q.get(), self.txt_security.get(),)
            my_cursor.execute(qury, vlaue)
            row = my_cursor.fetchone()
            if row ==None:
                messagebox.showerror(
                    "Error", "Plaese enter correct Answer", parent=self.root2)
            else:
                query = ("update register set password = %s where email=%s")
                value=(self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Info", "Your password has been reset ,plaese login new password",parent=self.root2)
                self.root2.destroy()


#-------------------------forgot pass------------------
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Plaese Enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="root", database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror ("My Error","Plaese enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                l=Label(self.root2,text="Forget Password", font=("times new roman", 20, "bold"),fg="red", bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2, text="Select Security Quetions",   font=(
                    "times new roman", 15, "bold"), bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_securiy_Q = ttk.Combobox(self.root2,  font=(
                    "times new roman", 15, "bold"), state="readonly")
                self.combo_securiy_Q["values"] = (
                    "Select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
                self.combo_securiy_Q.place(x=50, y=110, width=250)
                self.combo_securiy_Q.current(0)

                self.combo_securiy_Q.current(0)
                security_A = Label(self.root2, text="Security Answer",  font=(
                    "times new roman", 15, "bold"), bg="white", fg="black")
                security_A.place(x=50, y=150)
                self.txt_security = ttk.Entry(
                    self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password= Label(self.root2, text="New Password",  font=(
                    "times new roman", 15, "bold"), bg="white", fg="black")
                new_password.place(x=50, y=220)
                self.txt_newpass = ttk.Entry(
                    self.root2, font=("times new roman", 15))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset",command=self.reset_pass ,fon=("times new roman", 15, "bold"), fg="White", bg="green")
                btn.place(x=100, y=290)




class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # -------------variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

# bgimage-----------------------
        self.bg = ImageTk.PhotoImage(file=r"img/bgreg1.png")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

# leftimg_____-------------------------
        self.bg1 = ImageTk.PhotoImage(file=r"img/reg2.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)
# mainframe-------------------------------
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new romwn", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # lbl and entry------------------

        fname = Label(frame, text="First Name", font=(
            "times new romwn", 15, "bold"), bg="white", fg="black")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname, font=("times new romwn", 15,))
        self.fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name",  font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)
# -----------------row2
        contact = Label(frame, text="Contact No",  font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email",  font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)
# -------------------row3
        security_Q = Label(frame, text="Select Security Quetions",   font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_securiy_Q = ttk.Combobox(frame, textvariable=self.var_securityQ,  font=(
            "times new roman", 15, "bold"), state="readonly")
        self.combo_securiy_Q["values"] = (
            "Select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
        self.combo_securiy_Q.place(x=50, y=270, width=250)
        self.combo_securiy_Q.current(0)

        self.combo_securiy_Q.current(0)
        security_A = Label(frame, text="Security Answer",  font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)
        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_SecurityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)
        # ---------------------row4

        pswd = Label(frame, text="Password ",  font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)
        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)
        confirm_pswd = Label(frame, text="Confirm Password",  font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)
        self.txt_confirm_pswd = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # -----------checkbtn-------------------
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=(
            "times new roman", 15, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # --------------btns-------
        img = Image.open(r"./img/registerbtn.jpg")
        img = img.resize((200, 55), Image. ANTIALIAS)
        self.photoimage = ImageTk. PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data,
                    borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg="white")
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(r"./img/login2.png")
        img1 = img1.resize((200, 45), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", font=(
            "times new roman", 15, "bold"), fg="white")
        b1.place(x=330, y=420, width=200)

    def register_data(self):

        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "password & confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Plaese agree our terms ane condition")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="root", database="face_recognizer")

            my_cursor = conn.cursor()
            query = ("SELECT * FROM register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "User already exist,plaese try another email")
            else:
                my_cursor.execute("insert into register values (%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_SecurityA.get(),
                    self.var_pass.get()
                ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully")


if __name__ == "__main__":
    main()

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import datetime
import random
import time
import mysql.connector
import os
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1600x900+0+0")
        self.root.wm_iconbitmap("icon3.ico")


        self.bg=ImageTk.PhotoImage(file=r"Images\login_bg5.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=650,y=170,width=340,height=450)

        img1=Image.open(r"Images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=770,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=105)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.config(show='*')
        self.txtpass.place(x=40,y=250,width=270)
    

        #=======Icon Images=========
        img2=Image.open(r"Images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=690,y=323,width=25,height=25)

        img3=Image.open(r"Images\lock-512.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=690,y=395,width=25,height=25)

        #LoginButton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #forgetpassbtn
        registerbtn=Button(frame,text="Forget Password", command=self.forgot_password_window, font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)   



    # ----------------------- LOGIN FUNCTION ---------------------------------------------------

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get=="":
            messagebox.showerror("Error","all field required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="BlackBerry@0314",database="face_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
            ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return


            conn.commit()
            conn.close()


    # ----------------------- RESET PASSWORD ---------------------------------------------------

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select" or self.txt_security.get()=="" or self.txt_newpass.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="BlackBerry@0314",database="face_recognition")
                cur = conn.cursor()
                query2 = ("select * from register where email=%s and securityQ=%s and securityA=%s")
                value2 = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get(),)
                cur.execute(query2, value2)
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error", "Please Enter Correct Answer", parent=self.root2)
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.txt_newpass.get(), self.txtuser.get())
                    cur.execute(query, value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info", "Your Password has been Reset, please login with New Password", parent=self.root2)
                    self.root2.destroy()
                    self.txtuser.focus()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due To:{str(es)}", parent=self.root2)





    # ----------------------- FORGOT PASSWORD ---------------------------------------------------

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error", "Please  enter username to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="BlackBerry@0314",database="face_recognition")
            my_cursor=conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            

            if row==None:
                messagebox.showerror("My Error", "Please Enter the Valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+650+170")

                l = Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2, font=("times new roman",15,"bold"), state="readonly")
                self.combo_security_Q["values"]=("Select", "Your Birth Place","Your College Name","Your Roll No")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2, font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)


                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=250)

                self.txt_newpass=ttk.Entry(self.root2, font=("times new roman",15))
                self.txt_newpass.place(x=50,y=280,width=250)


                btn = Button(self.root2, text="Reset", command=self.reset_pass, font=("times new roman", 15, "bold"), bg="green", fg="white")
                btn.place(x=140, y=320)









class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #===========variable============

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()



        #============bg image=========

        self.bg=ImageTk.PhotoImage(file=r"Images\reg_bg1.png")
        bg_lbl =Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)



        #============left image=========

        self.bg1=ImageTk.PhotoImage(file=r"Images\left4.jpg")
        left_lbl =Label(self.root,image=self.bg1)
        left_lbl.place(x=100,y=150,width=470,height=550)
        


        #============main Frame==========

        frame=Frame(self.root,bg="white")
        frame.place(x=600,y=150,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)



        #==========label and entry===========

        #-------------row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.txt_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.txt_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame, textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #-------------row2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_lname.place(x=50,y=200,width=250)

        email=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_lname.place(x=370,y=200,width=250)

        #--------------row3
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"), state="readonly")
        self.combo_security_Q["values"]=("Select", "Your Birth Place","Your College Name","Your Roll No")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_lname.place(x=370,y=270,width=250)
        


        #----------------row4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_lname.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)



         #==============checkbutton========

        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)



         #==============Buttons==========

        img=Image.open(r"Images\register-now-button1.jpg")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=30,y=430,width=200)


        img1=Image.open(r"Images\loginpng.png")
        img1=img1.resize((200,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1, command=self.return_login, borderwidth=0,cursor="hand2")
        b1.place(x=360,y=430,width=200)


    # ================function decleration=================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same", parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree to our Terms and Conditions", parent=self.root)
        #Pass@123, BlackBerry@0314, BlueBerry14
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="BlackBerry@0314",database="face_recognition")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email", parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
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
                messagebox.showinfo("Success", "Register successfully", parent=self.root)
                self.root.destroy()


    def return_login(self):
        self.root.destroy()


 


if __name__== "__main__":
    main()
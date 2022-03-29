#User Interface Calculator
from tkinter import *
from tkinter import messagebox
import json
from utils.user_db_handler import * # asteric sign(*) imports all

def clear():
    userentry.delete("0", "end")
    passentry.delete("0", "end")

def close():
    window.destroy()

def login1():
    if user_name.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent = window)
    else:
        try:
            user = user_name.get()
            passw = password.get()

            result = login(user, passw)
            if result:
                messagebox.showinfo("Success", "Login success", parent = window)
                close()
                Calc()
            else:
                messagebox.showerror("Error", "Login failure :  Invalid User Name Or Password", parent = window)
        except Exception as  es:
            messagebox.showerror("Error", "Error Dui to : {0}".format(str(es)), parent = window)

def Calc():
    calc = Tk()#instantiation
    calc.title("simple calculator")
    calc.geometry("270x150")

    def popone():
        entry1.insert("end", "1")
    def poptwo():
        entry1.insert("end", "2")
    def popthree():
        entry1.insert("end", "3")
    def popfour():
        entry1.insert("end", "4")
    def popfive():
        entry1.insert("end", "5")
    def popsix():
        entry1.insert("end", "6")
    def popseven():
        entry1.insert("end", "7")
    def popeight():
        entry1.insert("end", "8")
    def popnine():
        entry1.insert("end", "9")
    def popzero():
        entry1.insert("end", "0")
    def addnum():
        entry1.insert("end", "+")
    def subtractnum():
        entry1.insert("end", "-")
    def multiplynum():
        entry1.insert("end", "*")
    def dividenum():
        entry1.insert("end", "/")
    def clear():
        #re = entry1.get()
        entry1.delete("0", "end")
    def equalsto():
        re = entry1.get()
        result = eval(re)
        entry1.delete("0", "end")
        entry1.insert("end", result)

    entry1 = Entry(calc)#Entry is a widget
    entry1.grid(columnspan=4, ipadx=70)#it will place our widget on row0 and column0

    btn1 = Button(calc, text = "1", fg = "white", bg = "dark blue", command=popone, height = 1, width = 7)
    btn1.grid(row=1, column=0)

    btn2 =  Button(calc, text="2", fg = "white", bg = "dark blue", command=poptwo, height = 1, width = 7)
    btn2.grid(row=1, column=1)

    btn3 =  Button(calc, text="3", fg = "white", bg = "dark blue", command=popthree, height = 1, width = 7)
    btn3.grid(row=1, column=2)

    btn4 =  Button(calc, text="4", fg = "white", bg = "dark blue", command = popfour, height = 1, width = 7)
    btn4.grid(row=2, column=0)

    btn5 =  Button(calc, text="5", fg = "white", bg = "dark blue", command = popfive, height = 1, width = 7)
    btn5.grid(row=2, column=1)

    btn6 =  Button(calc, text="6", fg = "white", bg = "dark blue", command = popsix, height = 1, width = 7)
    btn6.grid(row=2, column=2)

    btn7 =  Button(calc, text="7", fg = "white", bg = "dark blue", command = popseven, height = 1, width = 7)
    btn7.grid(row=3, column=0)

    btn8 =  Button(calc, text="8", fg = "white", bg = "dark blue", command = popeight, height = 1, width = 7)
    btn8.grid(row=3, column=1)

    btn9 =  Button(calc, text="9", fg = "white", bg = "dark blue", command = popnine, height = 1, width = 7)
    btn9.grid(row=3, column=2)

    btn0 =  Button(calc, text="0", fg = "white", bg = "dark blue", command = popzero, height = 1, width = 7)
    btn0.grid(row=4, column=0)

    add =  Button(calc, text="+", fg = "white", bg = "dark green", command = addnum, height = 1, width = 7)
    add.grid(row=1, column=3)

    subtract = Button(calc, text="-", fg = "white", bg = "dark green", command = subtractnum, height = 1, width = 7)
    subtract.grid(row=2, column=3)

    multiply = Button(calc, text="*", fg = "white", bg = "dark green", command = multiplynum, height = 1, width = 7)
    multiply.grid(row=3, column=3)

    divide = Button(calc, text="/", fg = "white", bg = "dark green", command = dividenum, height = 1, width = 7)
    divide.grid(row=4, column=3)

    equals =  Button(calc, text="=", fg = "white", bg = "dark blue", command=equalsto, height = 1, width = 7)
    equals.grid(row=4, column=2)

    clean = Button(calc, text="clear", fg = "white", bg = "dark red", command = clear, height = 1, width = 7)
    clean.grid(row=4, column=1)

    calc.mainloop()

def signup():
    def action():
        if user_name.get() == "" or password.get == "" or very_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required",  parent = registerwindow)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error", "Password And Verify Password Must Be The Same", parent = registerwindow)
        else:
            try:
                userName = user_name.get()
                passw = password.get()

                result = create_user(userName, passw)
                if result:
                    messagebox.showinfo("Success", "Registration Successful", parent = registerwindow)
                    clear()
                    switch()
                else:
                    messagebox.showerror("Error", "User Name Already Exists", parent = registerwindow)
            except Exception as  es:
                messagebox.showerror("Error", "Error Dui to : {0}".format(str(es)), parent = registerwindow)

    def switch():
        registerwindow.destroy()

    def clear():
        user_name.delete("0", "end")
        password.delete("0", "end")
        very_pass.delete("0", "end")

    registerwindow = Tk()
    registerwindow.title("Registration Form")
    registerwindow.maxsize(width = 500, height = 500)
    registerwindow.minsize(width = 500, height = 500)

    heading = Label(registerwindow, text = "Register", font = "Candara 25 bold")
    heading.place(x = 80, y = 150)

    user_name = Label(registerwindow, text = "User Name :", font = "Candara 10 bold")
    user_name.place(x = 80, y = 220)

    password = Label(registerwindow, text = "Password :", font = "Candara 10 bold")
    password.place(x = 80, y = 260)

    very_pass = Label(registerwindow, text = "Verify Password :", font = "Candara 10 bold")
    very_pass.place(x = 80, y = 300)

    user_name = StringVar()
    password = StringVar()
    very_pass = StringVar()

    user_name = Entry(registerwindow, width = 40, textvariable = user_name)
    user_name.place(x = 200, y = 223)

    password = Entry(registerwindow, width = 40, textvariable = password)
    password.place(x = 200, y = 260)

    very_pass = Entry(registerwindow, width = 40, textvariable = very_pass)
    very_pass.place(x = 200, y = 297)

    btn_signup = Button(registerwindow, text = "Signup", font = "Candara 10 bold", command = action) #command is missing
    btn_signup.place(x = 200, y = 334)

    btn_login = Button(registerwindow, text = "Clear", font = "Candara 10 bold", command = clear) #command is missing
    btn_login.place(x = 260, y = 334)

    switchLogin = Button(registerwindow, text = "Switch To Login", command = switch) #command is missing
    switchLogin.place(x = 350, y = 20)

    registerwindow.mainloop()

window = Tk()#instantiation
window.title("Login Portal")
window.maxsize(width = 500,  height = 500)
window.minsize(width = 500,  height = 500)

heading = Label(window, text = "Login", font = "Candara 25 bold")
heading.place(x = 80, y = 150)

username = Label(window, text = "User Name :", font = "Candara 10 bold")
username.place(x = 80, y = 220)

userpass = Label(window, text = "Password :", font = "Candara 10 bold")
userpass.place(x = 80, y = 260)

user_name = StringVar()
password = StringVar()

userentry = Entry(window, width = 40, textvariable = user_name)
userentry.focus()
userentry.place(x = 200, y = 223)

passentry = Entry(window, width = 40, show = "*", textvariable = password)
passentry.place(x = 200, y = 260)

btn_login = Button(window, text = "Login", font = "Candara 10 bold", command = login1) #command missing
btn_login.place(x = 200, y = 293)

btn_login = Button(window, text = "Clear", font = "Candara 10 bold", command = clear) #command missing
btn_login.place(x = 260, y = 293)

sign_up_btn = Button(window, text = "Switch To Sign Up", command = signup) #command missing
sign_up_btn.place(x = 350, y = 20)

window.mainloop()

import tkinter as tk
import ttkbootstrap as ttk 
from ttkbootstrap.constants import * 
from tkinter import messagebox
from PIL import Image,ImageTk,ImageFile


app = ttk.Window(themename='cosmo') 
app.geometry('750x400') 
app.title('login/sign up')


# functions_login


def back_to_login():
    image6.place_forget() 
    c1.place_forget() 
    b3.place_forget() 
    a1.place(x=358,y=91)
    a2.place(x=268,y=125)
    a3.place(x=270,y=150)
    a4.place(x=268,y=185)
    a5.place(x=270,y=210) 
    a6.place(x=270,y=265)
    a7.place(x=270,y=297)
    image_login2.place(x=335,y=3)
    image_login5.place(x=493,y=268)

def page_login():
    image_login5.place_forget() 
    l_login.place_forget() 
    image3.place_forget() 
    l1.place_forget() 
    l2.place_forget() 
    l3.place_forget() 
    e1.place_forget() 
    e2.place_forget() 
    e3.place_forget() 
    b1.place_forget() 
    b2.place_forget()
    a1.place(x=358,y=91)
    a2.place(x=268,y=125)
    a3.place(x=270,y=150)
    a4.place(x=268,y=185)
    a5.place(x=270,y=210) 
    a6.place(x=270,y=265)
    a7.place(x=270,y=297)
    image_login2.place(x=335,y=3)
    image_login5.place(x=493,y=268) 

def checkfill_login():
    text4 = a3.get()
    text5 = a5.get()
    with open('database.txt','r') as file:
           file1 = file.read()
           file2 = file1.split(',')
           if text4 == "" or text5 == "":
               messagebox.showerror(message='Fill In Your Information Completely')
           else:
              if len(file2[1]) == len(text4) and text4 in file2 and len(file2[2]) == len(text5) and text5 in file2:
                a1.place_forget()
                a2.place_forget()
                a3.place_forget()
                a4.place_forget()
                a5.place_forget()
                a6.place_forget()
                a7.place_forget()
                image_login5.place_forget()
                image_login2.place_forget()
                image_login8.place(x=310,y=40)
                succes.place(x=255,y=195)
                a8.place(x=343,y=240)
              else:
                messagebox.showerror(message='Enter The Correct Username Or Password')

# functions_signin

def page_signin():
   a1.place_forget()
   a2.place_forget()
   a3.place_forget()
   a4.place_forget()
   a5.place_forget()
   a6.place_forget()
   a7.place_forget()
   image_login5.place_forget()
   image_login2.place_forget()
   image3.place(x=341,y=10)
   image_login5.place(x=477,y=318)
   l_login.place(x=307,y=75)
   l1.place(x=270,y=110)
   l2.place(x=270,y=170)
   l3.place(x=270,y=230)
   e1.place(x=270,y=135)
   e2.place(x=270,y=195)
   e3.place(x=270,y=255)
   b1.place(x=269.5,y=315) 
   b2.place(x=269,y=345)
 
def checkfill_signin():
   text1 = e1.get() 
   text2 = e2.get() 
   text3 = e3.get()  
   if text1 == "" or text2 == "" or text3 == "":
        messagebox.showerror(message='Fill In Your Information Completely')
   else:
        image_login5.place_forget() 
        l_login.place_forget() 
        image3.place_forget() 
        l1.place_forget() 
        l2.place_forget() 
        l3.place_forget() 
        e1.place_forget() 
        e2.place_forget() 
        e3.place_forget() 
        b1.place_forget() 
        b2.place_forget() 
        c1.place(x=255,y=195) 
        image6.place(x=310,y=40) 
        b3.place(x=343,y=240)    
        with open('database.txt','a') as f: 
           f.write('{},{},{}'.format(text1,text2,text3))
  

 
def check_number(new_value): 
    if new_value.isdigit() or new_value == "": 
        return True 
    else: 
        messagebox.showerror(message='Only Numbers') 
        return False 
    

# **********login***********


# style

style1 = ttk.Style() 
style1.configure('Custom.TEntry',bordercolor='red')

# lable_login 
  
a1 = ttk.Label(app,text='Login',font=('calibri',14,'bold'),foreground='red')
a1.place(x=358,y=91)

# lable_username 
 
a2 = ttk.Label(app,text='Username',font=('tohama',11),foreground='black') 
a2.place(x=268,y=125) 
 
# entry_username 
 
a3 = ttk.Entry(app,foreground='black',width=35,style='Custom.TEntry,danger') 
a3.place(x=270,y=150) 
 
# lable_password 
 
a4 = ttk.Label(app,text='Password',font=('tohama',11),foreground='black') 
a4.place(x=268,y=185) 
 
# entry_password 
 
a5 = ttk.Entry(app,foreground='black',width=35,style='Custom.TEntry,danger') 
a5.place(x=270,y=210) 

# lable_successfuly

succes = ttk.Label(app,text='Your Login Is Successfuly',font=('calibri',18,'bold'),foreground='black') 
succes.place(x=255,y=195) 
succes.place_forget() 

# button 
 
a6 = ttk.Button(app,text='Login',style='danger-outline',width=33,command=checkfill_login) 
a6.place(x=270,y=265) 

a7 = ttk.Button(app,text='Or,Sign up',style='light',width=33,command=page_signin) 
a7.place(x=270,y=297) 

a8 = ttk.Button(app,text='Back',style='dark-outline',width=10) 
a8.place(x=343,y=240) 
a8.place_forget() 

# image
 
image_login = Image.open("6734512.png").resize((90,90))
image_login1 = ImageTk.PhotoImage(image_login)
image_login2 = ttk.Label(app,image=image_login1)
image_login2.place(x=335,y=3)

image_login3 = Image.open("55245-200.png").resize((30,30))
image_login4 = ImageTk.PhotoImage(image_login3)
image_login5 = ttk.Label(app,image=image_login4)
image_login5.place(x=493,y=268)

image_login6 = Image.open("istockphoto-963523770-1024x1024.jpg").resize((150,140)) 
image_login7 = ImageTk.PhotoImage(image_login6) 
image_login8 = ttk.Label(app,image=image_login7) 
image_login8.place(x=310,y=40) 
image_login8.place_forget() 



# ***********signin**********


#style 
 
style = ttk.Style() 
style.configure("Custom.TEntry", bordercolor="red") 
 
#image 
 
image1 = Image.open("6734512.png").resize((70,70)) 
image2 = ImageTk.PhotoImage(image1) 
image3 = ttk.Label(app,image=image2) 
image3.place(x=341,y=10)
image3.place_forget() 
 
image_login3 = Image.open("55245-200.png").resize((30,30)) 
image_login4 = ImageTk.PhotoImage(image_login3) 
image_login5 = ttk.Label(app,image=image_login4) 
image_login5.place(x=477,y=318)
image_login5.place_forget() 
 
image4 = Image.open("istockphoto-963523770-1024x1024.jpg").resize((150,140)) 
image5 = ImageTk.PhotoImage(image4) 
image6 = ttk.Label(app,image=image5) 
image6.place(x=310,y=40) 
image6.place_forget() 
 
#label 

l_login = ttk.Label(app,text="create an account",font=("Calibri",14,"bold"),foreground="red")  
l_login.place(x=307,y=75)
l_login.place_forget()
 
l1 = ttk.Label(app,text="Phone number",font=("tohama",11),foreground="black") 
l1.place(x=270,y=110)
l1.place_forget() 
 
l2 = ttk.Label(app,text="Username",font=("tohama",11),foreground="black") 
l2.place(x=270,y=170)
l2.place_forget() 
 
l3 = ttk.Label(app,text="Password",font=("tohama",11),foreground="black") 
l3.place(x=270,y=230)
l3.place_forget() 
 
c1 = ttk.Label(app,text='Your Sign In Is Successfuly',font=('calibri',18,'bold'),foreground='black') 
c1.place(x=255,y=195) 
c1.place_forget() 
 
#entry 
check_number1 = app.register(check_number)
e1 = ttk.Entry(app,foreground="black",style="Custom.TEntry,danger",width=33,validate='key',validatecommand=(check_number1,'%P')) 
e1.place(x=270,y=135)
e1.place_forget() 
 
e2 = ttk.Entry(app,foreground="black",style="Custom.TEntry,danger",width=33) 
e2.place(x=270,y=195)
e2.place_forget() 
 
e3 = ttk.Entry(app,foreground="black",style="Custom.TEntry,danger",width=33) 
e3.place(x=270,y=255) 
e3.place_forget()
 
#button 

b1 = ttk.Button(app,text="register",style='danger-outline',width=31,command=checkfill_signin) 
b1.place(x=269.5,y=315)
b1.place_forget() 
 
b2 = ttk.Button(app,text="Or,Login",style='light',width=31,command=page_login) 
b2.place(x=269,y=345)
b2.place_forget() 
 
b3 = ttk.Button(app,text='Back',style='dark-outline',width=10,command=back_to_login) 
b3.place(x=343,y=240) 
b3.place_forget() 
 
       
app.mainloop()







from tkinter import *   
import tkinter.messagebox
from random import randint
import customtkinter 
from PIL import Image,ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
u = 0
c = 0

def RPS(user):
    y = randint(1,3)
    arr = ('R','P', 'S')
    l = arr[y-1]
    if l == "R":
      strin = "ROCK"
    elif l == "P":
      strin = "PPAPER"
    else:
      strin = "SCISSOR"
    tkinter.messagebox.showinfo('Computer Played=',message=strin)
    comp = arr[y-1]

    global u
    global c
    if user == 'P':    
        if comp == 'P':
            res = "ITS A TIE"
        elif comp == 'R' :
            u+=1
            comp_label.configure(text = f"YOU: {u}")
            res = "YOU WIN"
        elif comp == 'S' :
            c += 1
            res = "YOU LOSE"
            player_label.configure(text = f"COMPUTER: {c}")
         
        return(c,u)
    elif user == 'S'  :
        if comp == 'P'  :
            u+=1
            res = "YOU WIN"
            comp_label.configure(text = f"YOU: {u}")   
        elif comp == 'R'  :
            c += 1
            res = "YOU LOSE"
            player_label.configure(text = f"COMPUTER: {c}")
        elif comp == 'S'  :
            res = "ITS A TIE"
         
    elif user == 'R'  :
        if comp == 'P'  :
            c += 1
            res = "YOU LOSE"
            player_label.configure(text = f"COMPUTER: {c}") 
        elif comp == 'R'  :
            res = "ITS A TIE"
        elif comp == 'S'  :
            u+=1
            res = "YOU WIN"
            comp_label.configure(text = f"YOU: {u}")
    if c == 6 and u == 9:
        d = "NOICC"
        flash_label1(d)
    elif c-3 >= u :
        d = "you are shit fam"
        flash_label1(d)
    elif c <= u-3 :
        d = "daayummmm bro chill"
        flash_label1(d)  
    elif c + u == 10:
        d = "Bhai kuch Kaam dhund le"
        flash_label1(d)    
    flash_label(res)


top = customtkinter.CTk()  
  
top.geometry("600x300")  
top.title("ROCK PAPER SCISSORS")
rock = ImageTk.PhotoImage(Image.open("C:/Users/Jay Ajmera/Downloads/rock.png").resize((150,150), Image.ANTIALIAS))
paper = ImageTk.PhotoImage(Image.open("C:/Users/Jay Ajmera/Downloads/paper.png").resize((150,150), Image.ANTIALIAS))
scissor = ImageTk.PhotoImage(Image.open("C:/Users/Jay Ajmera/Downloads/scissor.png").resize((150,150), Image.ANTIALIAS))

msg = Message(top, text = "Choose from the below options",bg="pink",width = 7000, font="italics",relief=RAISED  )  
player_label = customtkinter.CTkLabel(top, text="COMPUTER: 0",bg_color="blue",width=100)
comp_label = customtkinter.CTkLabel(top, text="YOU: 0",bg_color="red",width=100)
def fun():   
    user = "R"
    RPS(user) 
    RPS()
def fun1():  
      
    user = "P"
    RPS(user)
def fun2():  
      
    user = "S"
    RPS(user)
  
player_label.pack(side = BOTTOM)
comp_label.pack(side =BOTTOM) 
b1 = Button(master = top,text = "Rock", image = rock ,command = fun)
b1.place(relx =0.2, rely =0.2, anchor = N ) 
b2 = Button(top,text = "Paper", image = paper,activeforeground = "blue",command = fun1,activebackground = "pink")  
b2.place(relx =0.5, rely =0.2, anchor = N)   
b3 = Button(top,text = "Scissor", image =scissor ,activeforeground = "green",command = fun2,activebackground = "pink")  
b3.place(relx =0.8, rely =0.2, anchor = N) 


def flash_label(d):
    label = customtkinter.CTkLabel(top, text=d, font=("Helvetica", 15))
    label.pack(side = BOTTOM)
    top.after(1200, label.pack_forget)

flash_label("STARt")

def flash_label1(d):
    label1 = customtkinter.CTkLabel(top, text=d, font=("Georgia", 33),bg_color="#001e3c",fg_color="#22a6f2")
    label1.place(x =100,y=100)
    top.after(1100, label1.place_forget)
msg.pack(side=TOP)
top.mainloop()

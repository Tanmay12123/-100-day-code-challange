from tkinter import *
from tkinter import messagebox
from random import choice, choice,randint,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generate():
  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

  password_list = password_letters + password_numbers + password_symbols
  shuffle(password_list)

  password = "".join(password_list)
  pass_entry.insert(0,password)
  pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
# Shows some warnings if any fielsd is empty and shows some dialoge boxes and it also saves the data which the user has added in the text box
def text_adder():
    
    if len(web_entry.get())  == 0 :
        messagebox.showwarning(title = "Oops",message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web_entry.get(), message= f"These Are The Detalis Entered: \n\nEmail: {username_entry.get()}\n\nPassword: {pass_entry.get()}\n\nIs It Okay To Save?")
        
        if is_ok:
            with open("C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_15/data.txt",mode = "a") as data:
                data.write(f"{web_entry.get()}  |  {username_entry.get()}  |  {pass_entry.get()}\n")
                
            
            web_entry.delete(0,END)
            pass_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
FONT= ("Modern serifs",12,"italic")

# THe Canvas in which everythong appears on 
canvas = Canvas(width = 200,height=200,highlightthickness=0)
logo= PhotoImage(file = "C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_15/logo.png")
canvas.create_image(100,100,image = logo)
canvas.grid(column=1,row = 0)

#The Labels whose work is to just display text's
website = Label(text = "Website:",font =(FONT) )
website.grid(row=1,column=0)

username = Label(text = "Email / Username:",font =(FONT) )
username.grid(row=2,column=0)

password =  Label(text = "Password:",font =(FONT) )
password.grid(row = 3,column=0)

#Entries whose work is to take in text as input
web_entry = Entry(width=60)
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()

username_entry = Entry(width = 60)
username_entry.grid(row=2,column=1,columnspan=2)
username_entry.insert(0,"mutalikdesaitanmay@gmail.com")

pass_entry = Entry(width = 34)
pass_entry.grid(row=3,column=1)

#The Buttons which help to do commands
generatate_pass_button = Button(text = "Generate Password",width = 20,command = password_generate)
generatate_pass_button.grid(row=3,column=2)

add_button =  Button(text="Add",width=50,command=text_adder)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
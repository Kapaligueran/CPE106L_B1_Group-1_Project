import customtkinter
import businesslogic as bl
import time
import bcrypt
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title('Login')
app.geometry('450x360')
app.config(bg='#001220')

font1 = ('Helvetica', 25, 'bold')
font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold', 'underline')

frame1 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=470, height=360)
frame1.place(x=0, y=0)

signup_label = customtkinter.CTkLabel(frame1, font=font1, text='Sign up', text_color='#fff', bg_color='#001220')
signup_label.place(x=280, y=20)

username_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Username', placeholder_text_color='#a3a3a3', width=200, height=50)
username_entry.place(x=230, y=80)

password_entry = customtkinter.CTkEntry(frame1, font=font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Password', placeholder_text_color='#a3a3a3', width=200, height=50)
password_entry.place(x=230, y=150)

signup_button = customtkinter.CTkButton(frame1, font=font2, text_color='#fff', text='Sign up', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=120)
signup_button.place(x=230, y=220)

login_label = customtkinter.CTkLabel(frame1, font=font3, text='Already have an account?', text_color='#fff', bg_color='#001220')
login_label.place(x=230, y=250)

login_button = customtkinter.CTkButton(frame1, font=font4, text_color='#00bf77', text='Login', fg_color='#001220', hover_color='#001220', cursor='hand2', width=40)
login_button.place(x=395, y=250)

# Insert into database


# Display movies


# Display movies previously rented by the user


#
app.mainloop()

import customtkinter as ctk
import businesslogic as bl
import time
import bcrypt
from tkinter import *
from tkinter import messagebox

app = ctk.CTk()
app.title('Movie Rental')
app.geometry('900x600')
app.config(bg='#001220')
app.resizable(False, False)

font1 = ('Helvetica', 25, 'bold')
font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold', 'underline')

# Window to choose Signup or Login
frame1 = ctk.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=900, height=600)
frame1.place(x=0, y=0)


# Signup function
def signup_account():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    phone_number = phone_number_entry.get()
    given_name = given_name_entry.get()
    middle_name = middle_name_entry.get()
    last_name = last_name_entry.get()
    suffix = suffix_entry.get()
    if bl.check_if_signup_not_empty(username, password, given_name, middle_name, last_name, suffix, email,
                                    phone_number):
        if bl.check_if_user_does_not_exist(username):
            bl.create_account(username, password, given_name, middle_name, last_name, suffix, email, phone_number)
            messagebox.showinfo('Success', 'Account has been created.')
            home()
        else:
            messagebox.showerror('Error', 'Username already exists.')
    else:
        messagebox.showerror('Error', 'Enter all required data.')


# Login function
def login_account():
    username = username_entry2.get()
    password = password_entry2.get()
    if bl.check_if_login_not_empty(username, password):
        if not bl.check_if_user_does_not_exist(username):
            if bl.verify_password(username, password):
                messagebox.showinfo('Success', 'Logged in successfully.')
                home()
            else:
                messagebox.showerror('Error', 'Invalid password.')
        else:
            messagebox.showerror('Error', 'Invalid username.')
    else:
        messagebox.showerror('Error', 'Enter all data.')


# Signup window
def signup():
    frame2 = ctk.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=900, height=600)
    frame2.place(x=0, y=0)

    signup_label = ctk.CTkLabel(frame2, font=font1, text='Sign up', text_color='#fff', bg_color='#001220')
    signup_label.place(x=400, y=50)

    global username_entry
    global password_entry
    global email_entry
    global phone_number_entry
    global given_name_entry
    global middle_name_entry
    global last_name_entry
    global suffix_entry

    username_entry = ctk.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111',
                                  border_color='#004780', border_width=3, placeholder_text='Username (Required)',
                                  placeholder_text_color='#a3a3a3', width=200, height=50)
    username_entry.place(x=237.5, y=110)

    password_entry = ctk.CTkEntry(frame2, font=font2, show='*', text_color='#fff', fg_color='#001a2e',
                                  bg_color='#121111', border_color='#004780', border_width=3,
                                  placeholder_text='Password (Required)', placeholder_text_color='#a3a3a3', width=200,
                                  height=50)
    password_entry.place(x=237.5, y=180)

    email_entry = ctk.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111',
                               border_color='#004780', border_width=3, placeholder_text='Email (Required)',
                               placeholder_text_color='#a3a3a3', width=200, height=50)
    email_entry.place(x=237.5, y=250)

    phone_number_entry = ctk.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111',
                                      border_color='#004780', border_width=3,
                                      placeholder_text='Phone Number (Required)',
                                      placeholder_text_color='#a3a3a3', width=200, height=50)
    phone_number_entry.place(x=237.5, y=320)

    given_name_entry = ctk.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111',
                                    border_color='#004780', border_width=3, placeholder_text='First Name (Required)',
                                    placeholder_text_color='#a3a3a3', width=200, height=50)
    given_name_entry.place(x=462.5, y=110)

    middle_name_entry = ctk.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111',
                                     border_color='#004780', border_width=3, placeholder_text='Middle Name (Optional)',
                                     placeholder_text_color='#a3a3a3', width=200, height=50)
    middle_name_entry.place(x=462.5, y=180)

    last_name_entry = ctk.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111',
                                   border_color='#004780', border_width=3, placeholder_text='Last Name (Required)',
                                   placeholder_text_color='#a3a3a3', width=200, height=50)
    last_name_entry.place(x=462.5, y=250)

    suffix_entry = ctk.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111',
                                border_color='#004780', border_width=3, placeholder_text='Suffix (Optional)',
                                placeholder_text_color='#a3a3a3', width=200, height=50)
    suffix_entry.place(x=462.5, y=320)

    signup_button1 = ctk.CTkButton(frame2, command=signup_account, font=font2, text_color='#fff', text='Sign up',
                                   fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2',
                                   corner_radius=5, width=120)
    signup_button1.place(x=390, y=400)

    login_label1 = ctk.CTkLabel(frame2, font=font3, text='Already have an account?', text_color='#fff',
                                bg_color='#001220')
    login_label1.place(x=350, y=450)

    login_button1 = ctk.CTkButton(frame2, command=login, font=font4, text_color='#00bf77', text='Login',
                                  fg_color='#001220',
                                  hover_color='#001220', cursor='hand2', width=40)
    login_button1.place(x=515, y=450)


# Login window
def login():
    frame3 = ctk.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=900, height=600)
    frame3.place(x=0, y=0)

    login_label2 = ctk.CTkLabel(frame3, font=font1, text='Log in', text_color='#fff', bg_color='#001220')
    login_label2.place(x=412, y=150)

    global username_entry2
    global password_entry2

    username_entry2 = ctk.CTkEntry(frame3, font=font2, text_color='#fff', fg_color='#001a2e',
                                   bg_color='#121111',
                                   border_color='#004780', border_width=3, placeholder_text='Username',
                                   placeholder_text_color='#a3a3a3', width=200, height=50)
    username_entry2.place(x=350, y=210)

    password_entry2 = ctk.CTkEntry(frame3, font=font2, show='*', text_color='#fff', fg_color='#001a2e',
                                   bg_color='#121111', border_color='#004780', border_width=3,
                                   placeholder_text='Password', placeholder_text_color='#a3a3a3', width=200,
                                   height=50)
    password_entry2.place(x=350, y=270)

    login_button2 = ctk.CTkButton(frame3, command=login_account, font=font2, text_color='#fff', text='Log in',
                                  fg_color='#00965d', hover_color='#006e44', bg_color='#121111',
                                  cursor='hand2',
                                  corner_radius=5, width=120)
    login_button2.place(x=390, y=330)

    signup_label2 = ctk.CTkLabel(frame3, font=font3, text="Don't have an account?", text_color='#fff',
                                 bg_color='#001220')
    signup_label2.place(x=355, y=380)

    signup_button2 = ctk.CTkButton(frame3, command=signup, font=font4, text_color='#00bf77', text='Signup',
                                   fg_color='#001220',
                                   hover_color='#001220', cursor='hand2', width=40)
    signup_button2.place(x=505, y=380)


# Home window
def home():
    frame4 = ctk.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=900, height=600)
    frame4.place(x=0, y=0)


welcome_label = ctk.CTkLabel(frame1, font=font1, text='Welcome!', text_color='#fff', bg_color='#001220')
welcome_label.place(x=395, y=200)

signup_button = ctk.CTkButton(frame1, command=signup, font=font2, text_color='#fff', text='Sign up',
                              fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2',
                              corner_radius=5, width=120)
signup_button.place(x=390, y=260)

login_button = ctk.CTkButton(frame1, command=login, font=font2, text_color='#fff', text='Log in',
                             fg_color='#00965d', hover_color='#006e44', bg_color='#121111',
                             cursor='hand2',
                             corner_radius=5, width=120)
login_button.place(x=390, y=310)


app.mainloop()

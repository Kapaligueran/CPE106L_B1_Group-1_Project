import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import businesslogic as bl


class MovieRentalApp:
    def __init__(self):
        self.reviews_tab = None
        self.rented_tab = None
        self.wishlist_tab = None
        self.cart_tab = None
        self.catalog_tab = None
        self.tabView = None
        self.password_entry2 = None
        self.last_name_entry = None
        self.middle_name_entry = None
        self.given_name_entry = None
        self.phone_number_entry = None
        self.email_entry = None
        self.suffix_entry = None
        self.password_entry = None
        self.username_entry2 = None
        self.username_entry = None
        self.app = ctk.CTk()
        self.app.title('Movie Rental')
        self.app.geometry('900x600')
        self.app.config(bg='#001220')
        self.app.resizable(False, False)
        self.font1 = ('Helvetica', 25, 'bold')
        self.font2 = ('Arial', 17, 'bold')
        self.font3 = ('Arial', 13, 'bold')
        self.font4 = ('Arial', 13, 'bold', 'underline')
        self.current_frame = None
        self.create_home_frame()

    def create_home_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = ctk.CTkFrame(self.app, bg_color='#001220', fg_color='#001220', width=900, height=600)
        self.current_frame.place(x=0, y=0)

        welcome_label = ctk.CTkLabel(self.current_frame, font=self.font1, text='Welcome!', text_color='#fff',
                                     bg_color='#001220')
        welcome_label.place(x=395, y=200)

        signup_button = ctk.CTkButton(self.current_frame, command=self.create_signup_frame, font=self.font2,
                                      text_color='#fff', text='Sign up',
                                      fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2',
                                      corner_radius=5, width=120)
        signup_button.place(x=390, y=260)

        login_button = ctk.CTkButton(self.current_frame, command=self.create_login_frame, font=self.font2,
                                     text_color='#fff', text='Log in',
                                     fg_color='#00965d', hover_color='#006e44', bg_color='#121111',
                                     cursor='hand2',
                                     corner_radius=5, width=120)
        login_button.place(x=390, y=310)

    def create_signup_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = ctk.CTkFrame(self.app, bg_color='#001220', fg_color='#001220', width=900, height=600)
        self.current_frame.place(x=0, y=0)

        signup_label = ctk.CTkLabel(self.current_frame, font=self.font1, text='Sign up', text_color='#fff',
                                    bg_color='#001220')
        signup_label.place(x=400, y=50)

        self.username_entry = ctk.CTkEntry(self.current_frame, font=self.font2, text_color='#fff', fg_color='#001a2e',
                                           bg_color='#121111',
                                           border_color='#004780', border_width=3,
                                           placeholder_text='Username (Required)',
                                           placeholder_text_color='#a3a3a3', width=200, height=50)
        self.username_entry.place(x=237.5, y=110)

        self.password_entry = ctk.CTkEntry(self.current_frame, font=self.font2, show='*', text_color='#fff',
                                           fg_color='#001a2e',
                                           bg_color='#121111', border_color='#004780', border_width=3,
                                           placeholder_text='Password (Required)', placeholder_text_color='#a3a3a3',
                                           width=200,
                                           height=50)
        self.password_entry.place(x=237.5, y=180)

        self.email_entry = ctk.CTkEntry(self.current_frame, font=self.font2, text_color='#fff', fg_color='#001a2e',
                                        bg_color='#121111',
                                        border_color='#004780', border_width=3, placeholder_text='Email (Required)',
                                        placeholder_text_color='#a3a3a3', width=200, height=50)
        self.email_entry.place(x=237.5, y=250)

        self.phone_number_entry = ctk.CTkEntry(self.current_frame, font=self.font2, text_color='#fff',
                                               fg_color='#001a2e', bg_color='#121111',
                                               border_color='#004780', border_width=3,
                                               placeholder_text='Phone Number (Required)',
                                               placeholder_text_color='#a3a3a3', width=200, height=50)
        self.phone_number_entry.place(x=237.5, y=320)

        self.given_name_entry = ctk.CTkEntry(self.current_frame, font=self.font2, text_color='#fff', fg_color='#001a2e',
                                             bg_color='#121111',
                                             border_color='#004780', border_width=3,
                                             placeholder_text='First Name (Required)',
                                             placeholder_text_color='#a3a3a3', width=200, height=50)
        self.given_name_entry.place(x=462.5, y=110)

        self.middle_name_entry = ctk.CTkEntry(self.current_frame, font=self.font2, text_color='#fff',
                                              fg_color='#001a2e',
                                              bg_color='#121111',
                                              border_color='#004780', border_width=3,
                                              placeholder_text='Middle Name (Optional)',
                                              placeholder_text_color='#a3a3a3', width=200, height=50)
        self.middle_name_entry.place(x=462.5, y=180)

        self.last_name_entry = ctk.CTkEntry(self.current_frame, font=self.font2, text_color='#fff', fg_color='#001a2e',
                                            bg_color='#121111',
                                            border_color='#004780', border_width=3,
                                            placeholder_text='Last Name (Required)',
                                            placeholder_text_color='#a3a3a3', width=200, height=50)
        self.last_name_entry.place(x=462.5, y=250)

        self.suffix_entry = ctk.CTkEntry(self.current_frame, font=self.font2, text_color='#fff', fg_color='#001a2e',
                                         bg_color='#121111',
                                         border_color='#004780', border_width=3, placeholder_text='Suffix (Optional)',
                                         placeholder_text_color='#a3a3a3', width=200, height=50)
        self.suffix_entry.place(x=462.5, y=320)

        signup_button1 = ctk.CTkButton(self.current_frame, command=self.signup_account, font=self.font2,
                                       text_color='#fff', text='Sign up',
                                       fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2',
                                       corner_radius=5, width=120)
        signup_button1.place(x=390, y=400)

        login_label1 = ctk.CTkLabel(self.current_frame, font=self.font3, text='Already have an account?',
                                    text_color='#fff',
                                    bg_color='#001220')
        login_label1.place(x=350, y=450)

        login_button1 = ctk.CTkButton(self.current_frame, command=self.create_login_frame, font=self.font4,
                                      text_color='#00bf77', text='Login',
                                      fg_color='#001220',
                                      hover_color='#001220', cursor='hand2', width=40)
        login_button1.place(x=515, y=450)

    def create_login_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = ctk.CTkFrame(self.app, bg_color='#001220', fg_color='#001220', width=900, height=600)
        self.current_frame.place(x=0, y=0)

        login_label = ctk.CTkLabel(self.current_frame, font=self.font1, text='Log in', text_color='#fff',
                                   bg_color='#001220')
        login_label.place(x=412, y=150)

        self.username_entry2 = ctk.CTkEntry(self.current_frame, font=self.font2, text_color='#fff', fg_color='#001a2e',
                                            bg_color='#121111',
                                            border_color='#004780', border_width=3, placeholder_text='Username',
                                            placeholder_text_color='#a3a3a3', width=200, height=50)
        self.username_entry2.place(x=350, y=210)

        self.password_entry2 = ctk.CTkEntry(self.current_frame, font=self.font2, show='*', text_color='#fff',
                                            fg_color='#001a2e',
                                            bg_color='#121111', border_color='#004780', border_width=3,
                                            placeholder_text='Password', placeholder_text_color='#a3a3a3', width=200,
                                            height=50)
        self.password_entry2.place(x=350, y=270)

        login_button2 = ctk.CTkButton(self.current_frame, command=self.login_account, font=self.font2,
                                      text_color='#fff', text='Log in',
                                      fg_color='#00965d', hover_color='#006e44', bg_color='#121111',
                                      cursor='hand2',
                                      corner_radius=5, width=120)
        login_button2.place(x=390, y=330)

        signup_label2 = ctk.CTkLabel(self.current_frame, font=self.font3, text="Don't have an account?",
                                     text_color='#fff',
                                     bg_color='#001220')
        signup_label2.place(x=355, y=380)

        signup_button2 = ctk.CTkButton(self.current_frame, command=self.create_signup_frame, font=self.font4,
                                       text_color='#00bf77', text='Signup',
                                       fg_color='#001220',
                                       hover_color='#001220', cursor='hand2', width=40)
        signup_button2.place(x=505, y=380)

    def create_navigation_tabs(self):
        self.tabView = ctk.CTkTabview(self.app, bg_color='#001220', fg_color='#fff', segmented_button_selected_color='#001220',
                                      border_color='#001220', corner_radius=10, width=880, height=550)
        self.tabView.pack(padx=10, pady=10)

        self.tabView.add('Movie Catalog')
        self.tabView.add('Cart')
        self.tabView.add('Wish List')
        self.tabView.add('Rented Movies')
        self.tabView.add('Reviews')

        self.tabView.set('Movie Catalog')

    def signup_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        phone_number = self.phone_number_entry.get()
        given_name = self.given_name_entry.get()
        middle_name = self.middle_name_entry.get()
        last_name = self.last_name_entry.get()
        suffix = self.suffix_entry.get()
        if bl.check_if_signup_not_empty(username, password, given_name, middle_name, last_name, suffix, email,
                                        phone_number):
            if bl.check_if_user_does_not_exist(username):
                bl.create_account(username, password, given_name, middle_name, last_name, suffix, email, phone_number)
                messagebox.showinfo('Success', 'Account has been created.')
                self.create_navigation_tabs()
            else:
                messagebox.showerror('Error', 'Username already exists.')
        else:
            messagebox.showerror('Error', 'Enter all required data.')

    def login_account(self):
        username = self.username_entry2.get()
        password = self.password_entry2.get()
        if bl.check_if_login_not_empty(username, password):
            if not bl.check_if_user_does_not_exist(username):
                if bl.verify_password(username, password):
                    messagebox.showinfo('Success', 'Logged in successfully.')
                    self.create_navigation_tabs()
                else:
                    messagebox.showerror('Error', 'Invalid password.')
            else:
                messagebox.showerror('Error', 'Invalid username.')
        else:
            messagebox.showerror('Error', 'Enter all data.')

    def start(self):
        self.app.mainloop()


app = MovieRentalApp()
app.start()

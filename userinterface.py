import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import businesslogic as bl


class MovieRentalApp:
    def __init__(self):
        self.rating_entry = None
        self.review_entry = None
        self.movie_review_frame = None
        self.current_user_id = None
        self.movie_table_frame = None
        self.movie_details_frame = None
        self.reviews_tab = None
        self.rented_tab = None
        self.wishlist_tab = None
        self.cart_tab = None
        self.catalog_tab = None
        self.tabView = None
        self.password_entry2 = None
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
        signup_label.place(x=400, y=150)

        self.username_entry = ctk.CTkEntry(self.current_frame, font=self.font2, text_color='#fff', fg_color='#001a2e',
                                           bg_color='#121111',
                                           border_color='#004780', border_width=3, placeholder_text='Username',
                                           placeholder_text_color='#a3a3a3', width=200, height=50)
        self.username_entry.place(x=350, y=210)

        self.password_entry = ctk.CTkEntry(self.current_frame, font=self.font2, show='*', text_color='#fff',
                                           fg_color='#001a2e',
                                           bg_color='#121111', border_color='#004780', border_width=3,
                                           placeholder_text='Password', placeholder_text_color='#a3a3a3', width=200,
                                           height=50)
        self.password_entry.place(x=350, y=270)

        signup_button1 = ctk.CTkButton(self.current_frame, command=self.signup_account, font=self.font2,
                                       text_color='#fff', text='Sign up',
                                       fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2',
                                       corner_radius=5, width=120)
        signup_button1.place(x=390, y=330)

        login_label1 = ctk.CTkLabel(self.current_frame, font=self.font3, text='Already have an account?',
                                    text_color='#fff',
                                    bg_color='#001220')
        login_label1.place(x=350, y=380)

        login_button1 = ctk.CTkButton(self.current_frame, command=self.create_login_frame, font=self.font4,
                                      text_color='#00bf77', text='Login',
                                      fg_color='#001220',
                                      hover_color='#001220', cursor='hand2', width=40)
        login_button1.place(x=515, y=380)

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
        self.tabView = ctk.CTkTabview(self.app, bg_color='#001220', fg_color='#fff',
                                      segmented_button_selected_color='#001220',
                                      border_color='#001220', corner_radius=10, width=880, height=550)
        self.tabView.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.tabView.grid_rowconfigure(0, weight=1)
        self.tabView.grid_columnconfigure(0, weight=1)

        self.tabView.add('Movie Catalog')
        self.display_movie_catalog()
        self.tabView.add('Cart')
        self.display_cart()
        self.tabView.add('Wish List')
        self.display_wishlist()
        self.tabView.add('Rented Movies')
        self.display_rented_movies()
        self.tabView.add('Reviews')
        self.display_reviews()

        self.tabView.set('Movie Catalog')

    def signup_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if bl.check_if_signup_not_empty(username, password):
            if bl.check_if_user_does_not_exist(username):
                bl.create_account(username, password)
                messagebox.showinfo('Success', 'Account has been created.')
                self.current_user_id = bl.get_current_user_id(username)
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
                    # messagebox.showinfo('Success', 'Logged in successfully.')
                    self.current_user_id = bl.get_current_user_id(username)
                    self.create_navigation_tabs()
                else:
                    messagebox.showerror('Error', 'Invalid password.')
            else:
                messagebox.showerror('Error', 'Invalid username.')
        else:
            messagebox.showerror('Error', 'Enter all data.')

    def add_to_cart(self, movie_id):
        user_id = self.current_user_id
        if not bl.check_if_movie_in_cart(user_id, movie_id):
            bl.add_to_cart(user_id, movie_id)
            messagebox.showinfo('Success', 'Movie added to your cart.')
            self.display_cart()
        else:
            messagebox.showerror('Error', 'Movie is already in your cart.')

    def add_to_cart_from_wishlist(self, title):
        # TO BE IMPLEMENTED
        user_id = self.current_user_id
        if not bl.check_if_movie_in_cart_from_title(user_id, title):
            bl.add_to_cart_from_wishlist(user_id, title)
            messagebox.showinfo('Success', 'Movie added to your cart.')
            self.remove_from_wishlist(title)
            self.display_cart()
            self.display_wishlist()
        else:
            messagebox.showerror('Error', 'Movie is already in your cart.')
        pass

    def add_to_wishlist(self, movie_id):
        user_id = self.current_user_id
        if not bl.check_if_movie_in_wishlist(user_id, movie_id):
            bl.add_to_wishlist(user_id, movie_id)
            messagebox.showinfo('Success', 'Movie added to your wish list.')
            self.display_wishlist()
        else:
            messagebox.showerror('Error', 'Movie is already in your wish list.')

    def remove_from_cart(self, title):
        user_id = self.current_user_id
        bl.remove_from_cart(user_id, title)
        messagebox.showinfo('Success', 'Movie removed from your cart.')
        self.display_cart()

    def remove_from_wishlist(self, title):
        user_id = self.current_user_id
        # Implement the remove from wishlist functionality here
        bl.remove_from_wishlist(user_id, title)
        messagebox.showinfo('Success', 'Movie removed from your wishlist.')
        self.display_wishlist()

    def checkout(self, title):
        user_id = self.current_user_id
        bl.checkout(user_id, title)
        messagebox.showinfo('Success', 'Movie rented.')
        self.display_rented_movies()
        self.display_cart()

    def return_movie(self, title, rental_date, return_date):
        user_id = self.current_user_id
        bl.return_movie(user_id, rental_date, return_date, title)
        messagebox.showinfo('Success', 'Movie returned.')
        self.display_rented_movies()

    # Display movie catalog
    def display_movie_catalog(self):
        movies = bl.get_movie_catalog()
        headers = ['ID', 'Title']
        self.movie_table_frame = ctk.CTkScrollableFrame(self.tabView.tab("Movie Catalog"), bg_color='#001220')
        self.movie_table_frame.grid(row=0, column=0, sticky='nsew')

        column_widths = [10, 100]
        for i, (header, width) in enumerate(zip(headers, column_widths)):
            label = ctk.CTkLabel(self.movie_table_frame, text=header, font=self.font2, bg_color='#001220',
                                 text_color='#fff')
            label.grid(row=0, column=i, padx=5, pady=5, ipadx=width, sticky='ew')

        for row, movie in enumerate(movies, start=1):
            for col, (data, width) in enumerate(zip(movie, column_widths), start=0):
                label = ctk.CTkLabel(self.movie_table_frame, text=str(data), font=self.font3, bg_color='#001220',
                                     text_color='#fff')
                label.grid(row=row, column=col, padx=5, pady=5, ipadx=width,
                           sticky='ew')
                if col == 1:
                    label.bind("<Button-1>",
                               lambda event, movie_id=movie[0]: self.display_movie_details(bl.select_movie(movie_id)))

    def display_movie_details(self, movie_details):
        # Check if movie_details_frame exists and destroy it if it does
        if hasattr(self, 'movie_details_frame') and self.movie_details_frame:
            self.movie_details_frame.destroy()
        # Create a new movie_details_frame
        self.movie_details_frame = ctk.CTkFrame(self.tabView.tab("Movie Catalog"), bg_color='#001220')
        self.movie_details_frame.grid(row=0, column=5, rowspan=10, padx=20, pady=20)
        self.movie_details_frame.columnconfigure(0, weight=1)
        self.movie_details_frame.columnconfigure(1, weight=1)
        self.movie_details_frame.columnconfigure(2, weight=1)

        title_label = ctk.CTkLabel(self.movie_details_frame, text=f"Title: {movie_details[1]}", font=self.font3,
                                   bg_color='#001220', text_color='#fff', justify='left')
        title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky='w')

        synopsis_label = ctk.CTkLabel(self.movie_details_frame, text=f"Synopsis: {movie_details[2]}", font=self.font3,
                                      bg_color='#001220', text_color='#fff', wraplength=600, justify='left')
        synopsis_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky='w')

        genre_label = ctk.CTkLabel(self.movie_details_frame, text=f"Genre: {movie_details[3]}", font=self.font3,
                                   bg_color='#001220', text_color='#fff', justify='left')
        genre_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky='w')

        price_label = ctk.CTkLabel(self.movie_details_frame, text=f"Price: {movie_details[4]}", font=self.font3,
                                   bg_color='#001220', text_color='#fff', justify='left')
        price_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky='w')

        add_to_cart_button = ctk.CTkButton(self.movie_details_frame,
                                           command=lambda movie_id=movie_details[0]: self.add_to_cart(movie_id),
                                           text="Add to Cart", fg_color='#00965d', hover_color='#006e44',
                                           bg_color='#121111', cursor='hand2', corner_radius=5, width=30)
        add_to_cart_button.grid(row=4, column=0, padx=10, pady=10, sticky='ew')

        add_to_wishlist_button = ctk.CTkButton(self.movie_details_frame,
                                               command=lambda movie_id=movie_details[0]: self.add_to_wishlist(movie_id),
                                               text="Add to Wish List", fg_color='#00965d', hover_color='#006e44',
                                               bg_color='#121111', cursor='hand2', corner_radius=5, width=30)
        add_to_wishlist_button.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

        review_button = ctk.CTkButton(self.movie_details_frame,
                                      command=lambda movie_id=movie_details[0]: self.display_review_form(movie_id),
                                      text="Review", fg_color='#00965d', hover_color='#006e44',
                                      bg_color='#121111', cursor='hand2', corner_radius=5, width=30)
        review_button.grid(row=4, column=2, padx=10, pady=10, sticky='ew')

    def display_cart(self):
        if hasattr(self, 'cart_tab') and self.cart_tab is not None:
            self.cart_tab.destroy()

        cart_items = bl.get_user_cart(self.current_user_id)
        headers = ['Title', 'Price']
        cart_tab = ctk.CTkFrame(self.tabView.tab("Cart"), bg_color='#001220')
        cart_tab.grid(row=0, column=0, sticky='nsew')
        cart_tab.grid_rowconfigure(0, weight=1)
        cart_tab.grid_columnconfigure(0, weight=1)

        for i, header in enumerate(headers):
            label = ctk.CTkLabel(cart_tab, text=header, font=self.font2, bg_color='#001220', text_color='#fff')
            label.grid(row=0, column=i, padx=5, pady=5, sticky='nsew')

        for row, item in enumerate(cart_items, start=1):
            for col, data in enumerate(item, start=0):
                label = ctk.CTkLabel(cart_tab, text=str(data), font=self.font3, bg_color='#001220',
                                     text_color='#fff')
                label.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

            title = item[0]
            # Add "Checkout" and "Remove" buttons in the last column
            checkout_button = ctk.CTkButton(cart_tab, text="Checkout",
                                            command=lambda: self.checkout(title),
                                            fg_color='#00965d', hover_color='#006e44', bg_color='#121111',
                                            cursor='hand2', corner_radius=5, width=8)
            checkout_button.grid(row=row, column=3, padx=5, pady=5, sticky='nsew')

            remove_button = ctk.CTkButton(cart_tab, text="Remove",
                                          command=lambda: self.remove_from_cart(title),
                                          fg_color='#00965d', hover_color='#006e44', bg_color='#121111',
                                          cursor='hand2', corner_radius=5, width=8)
            remove_button.grid(row=row, column=4, padx=5, pady=5, sticky='nsew')

    def display_wishlist(self):
        if hasattr(self, 'wishlist_tab') and self.wishlist_tab is not None:
            self.wishlist_tab.destroy()

        wishlist_items = bl.get_user_wishlist(self.current_user_id)
        headers = ['Title']
        wishlist_tab = ctk.CTkFrame(self.tabView.tab("Wish List"), bg_color='#001220')
        wishlist_tab.grid(row=0, column=0, sticky='nsew')
        wishlist_tab.grid_rowconfigure(0, weight=1)
        wishlist_tab.grid_columnconfigure(0, weight=1)

        for i, header in enumerate(headers):
            label = ctk.CTkLabel(wishlist_tab, text=header, font=self.font2, bg_color='#001220', text_color='#fff')
            label.grid(row=0, column=i, padx=5, pady=5, sticky='nsew')

        for row, item in enumerate(wishlist_items, start=1):
            for col, data in enumerate(item, start=0):
                label = ctk.CTkLabel(wishlist_tab, text=str(data), font=self.font3, bg_color='#001220',
                                     text_color='#fff')
                label.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

            # Add "Add to Cart" and "Remove" buttons in the last columns
            add_to_cart_button = ctk.CTkButton(wishlist_tab, text="Add to Cart",
                                               command=lambda title=item[0]: self.add_to_cart_from_wishlist(
                                                   title),
                                               fg_color='#00965d', hover_color='#006e44', bg_color='#121111',
                                               cursor='hand2', corner_radius=5, width=8)
            add_to_cart_button.grid(row=row, column=len(headers), padx=5, pady=5, sticky='nsew')

            remove_button = ctk.CTkButton(wishlist_tab, text="Remove",
                                          command=lambda title=item[0]: self.remove_from_wishlist(title),
                                          fg_color='#00965d', hover_color='#006e44', bg_color='#121111',
                                          cursor='hand2', corner_radius=5, width=8)
            remove_button.grid(row=row, column=len(headers) + 1, padx=5, pady=5, sticky='nsew')

    def display_rented_movies(self):
        if hasattr(self, 'rented_tab') and self.rented_tab is not None:
            self.rented_tab.destroy()

        rented_movies = bl.get_user_rented_movies(self.current_user_id)
        headers = ['Title', 'Rental Date', 'Return Date']
        rented_tab = ctk.CTkFrame(self.tabView.tab("Rented Movies"), bg_color='#001220')
        rented_tab.grid(row=0, column=0, sticky='nsew')
        rented_tab.grid_rowconfigure(0, weight=1)
        rented_tab.grid_columnconfigure(0, weight=1)

        for i, header in enumerate(headers):
            label = ctk.CTkLabel(rented_tab, text=header, font=self.font2, bg_color='#001220', text_color='#fff')
            label.grid(row=0, column=i, padx=5, pady=5, sticky='nsew')

        for row, movie in enumerate(rented_movies, start=1):
            title = movie[0]
            rental_date = movie[1]
            return_date = movie[2]
            for col, data in enumerate(movie, start=0):
                label = ctk.CTkLabel(rented_tab, text=str(data), font=self.font3, bg_color='#001220', text_color='#fff')
                label.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

            return_movie_button = ctk.CTkButton(rented_tab, text="Return Movie", font=self.font3, bg_color='#001220',
                                                text_color='#fff',
                                                command=lambda: self.return_movie(title, rental_date, return_date))
            return_movie_button.grid(row=row, column=len(headers), padx=5, pady=5, sticky='nsew')

    def display_reviews(self):
        if hasattr(self, 'reviews_tab') and self.reviews_tab is not None:
            self.reviews_tab.destroy()

        reviews = bl.get_reviews()  # Retrieve the list of reviews from the business logic layer
        headers = ['Movie Title', 'Rating', 'Review']
        reviews_tab = ctk.CTkFrame(self.tabView.tab("Reviews"), bg_color='#001220')
        reviews_tab.grid(row=0, column=0, sticky='nsew')
        reviews_tab.grid_rowconfigure(0, weight=1)
        reviews_tab.grid_columnconfigure(0, weight=1)

        for i, header in enumerate(headers):
            label = ctk.CTkLabel(reviews_tab, text=header, font=self.font2, bg_color='#001220', text_color='#fff')
            label.grid(row=0, column=i, padx=5, pady=5, sticky='nsew')

        for row, review in enumerate(reviews, start=1):
            for col, data in enumerate(review, start=0):
                label = ctk.CTkLabel(reviews_tab, text=str(data), font=self.font3, bg_color='#001220',
                                     text_color='#fff')
                label.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

    def display_review_form(self, movie_id):
        # Check if movie_review_frame exists and destroy it if it does
        if hasattr(self, 'movie_review_frame') and self.movie_review_frame:
            self.movie_review_frame.destroy()
        # Create a new movie_review_frame
        self.movie_review_frame = ctk.CTkFrame(self.tabView.tab("Movie Catalog"), bg_color='#001220')
        self.movie_review_frame.grid(row=0, column=5, rowspan=10, padx=20, pady=20)
        self.movie_review_frame.columnconfigure(0, weight=1)
        self.movie_review_frame.columnconfigure(1, weight=1)

        movie_details = bl.select_movie(movie_id)
        title_label = ctk.CTkLabel(self.movie_review_frame, text=f"Title: {movie_details[1]}", font=self.font3,
                                   bg_color='#001220', text_color='#fff', justify='left')
        title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky='w')

        rating_label = ctk.CTkLabel(self.movie_review_frame, text="Rating (1-5):", font=self.font3,
                                    bg_color='#001220', text_color='#fff', justify='left')
        rating_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.rating_entry = ctk.CTkEntry(self.movie_review_frame, font=self.font3,
                                         bg_color='#121111', fg_color='#121111',
                                         border_color='#121111', text_color='#fff', width=10)
        self.rating_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        review_label = ctk.CTkLabel(self.movie_review_frame, text="Review:", font=self.font3,
                                    bg_color='#001220', text_color='#fff', justify='left')
        review_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.review_entry = ctk.CTkTextbox(self.movie_review_frame, font=self.font3,
                                           bg_color='#121111', fg_color='#121111',
                                           border_color='#121111', text_color='#fff', width=500, height=200)
        self.review_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        submit_button = ctk.CTkButton(self.movie_review_frame,
                                      command=lambda selected_movie_id=movie_id: self.submit_review(movie_id),
                                      text="Submit", fg_color='#00965d', hover_color='#006e44',
                                      bg_color='#121111', cursor='hand2', corner_radius=5, width=30)
        submit_button.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

    def submit_review(self, movie_id):
        rating = int(self.rating_entry.get())
        review = self.review_entry.get("1.0", "end-1c")
        bl.submit_review(movie_id, rating, review)
        messagebox.showinfo('Success', 'Review submitted')
        self.display_reviews()
        self.movie_review_frame.destroy()

    def start(self):
        self.app.mainloop()


app = MovieRentalApp()
app.start()

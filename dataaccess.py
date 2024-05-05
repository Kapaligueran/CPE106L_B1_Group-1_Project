import sqlite3


# class DatabaseManagement to perform CRUD operations on database
class DatabaseManagement:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    # Creating a new user account
    def create_user(self, username, password, given_name, middle_name, last_name, suffix, email, phone_number):
        self.cur.execute("""INSERT INTO [User] (Username, Password, Given_Name, Middle_Name, Last_Name, Suffix, 
        Email, Phone_Number) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                         (username, password, given_name, middle_name, last_name, suffix, email, phone_number))
        self.conn.commit()

    # Selecting user via username
    def select_user_by_username(self, username):
        self.cur.execute("SELECT Username from [User] WHERE Username=?", (username,))
        return self.cur.fetchone()

    # Getting an existing user's password
    def get_password(self, username):
        self.cur.execute("SELECT Password from [User] WHERE Username=?", (username,))
        return self.cur.fetchone()

    # Getting a user's ID from their username
    def get_user_id(self, username):
        self.cur.execute("SELECT User_ID FROM [User] WHERE Username=?", (username,))
        return self.cur.fetchone()

    # Deleting a user's account

    # Adding a movie to the catalog

    # Viewing a movie's details
    def get_movie_details(self, movie_id):
        self.cur.execute("SELECT * FROM Movie WHERE Movie_ID=?", (movie_id,))
        return self.cur.fetchone()

    # Viewing the entire movie catalog
    def view_movie_catalog(self):
        self.cur.execute("SELECT * FROM Movie")
        return self.cur.fetchall()

    # Updating a movie's details

    # Deleting a movie from the catalog

    # Creating a new rental for a user

    # Viewing a user's rentals

    # Updating a rental's status

    # Creating a user's cart
    def add_movie_to_cart(self, user_id, movie_id):
        self.cur.execute("INSERT INTO Cart (User_ID, Movie_ID) VALUES (?, ?)", (user_id, movie_id))
        self.conn.commit()

    # Viewing a user's cart
    def select_movie_in_cart(self, user_id, movie_id):
        self.cur.execute("SELECT * FROM Cart WHERE (User_ID=? AND Movie_ID=?)", (user_id, movie_id))
        return self.cur.fetchone()

    # Updating a user's cart

    # Emptying a user's cart

    # Adding a review of a movie

    # Viewing a movie's reviews

    # Deleting a movie's reviews

    # Creating a user's wish list

    # Viewing a user's wish list

    # Updating a user's wish list

    # Removing a movie from a user's wish list

    # Reading data from database

    # Closing connection to database
    def close_connection(self):
        self.conn.close()

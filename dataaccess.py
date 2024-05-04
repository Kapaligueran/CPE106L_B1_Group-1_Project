import sqlite3


# class DatabaseManagement to perform CRUD operations on database
class DatabaseManagement:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    # Creating a new user account with details
    def create_user(self, username, password, given_name, middle_name, last_name, suffix, email, phone_number):
        self.cur.execute("""INSERT INTO [User] (Username, Password, Given_Name, Middle_Name, Last_Name, Suffix, 
        Email, Phone_Number) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                         (username, password, given_name, middle_name, last_name, suffix, email, phone_number))
        self.conn.commit()

    # Selecting user via username
    def select_user_by_username(self, username):
        self.cur.execute("SELECT Username from [User] WHERE Username=?", [username])
        return self.cur.fetchone()

    # Getting an existing user's password
    def get_password(self, username):
        self.cur.execute("SELECT Password from [User] WHERE Username=?", [username])
        return self.cur.fetchone()


    # Deleting a user's account

    # Adding a movie to the catalog

    # Viewing a movie's details

    # Viewing the entire movie catalog
    def view_movie_catalog(self):
        self.cur.execute("SELECT * FROM Movie")

    # Updating a movie's details

    # Deleting a movie from the catalog

    # Creating a new rental for a user

    # Viewing a user's rentals

    # Updating a rental's status

    # Creating a user's cart

    # Viewing a user's cart

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

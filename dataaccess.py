import sqlite3


# class DatabaseManagement to perform CRUD operations on database
class DatabaseManagement:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    # Creating a new user account
    def create_user(self, username, password):
        self.cur.execute("""INSERT INTO [User] (Username, Password) VALUES (?, ?)""",
                         (username, password))
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

    # Getting a movie's ID from its title
    def get_movie_id_from_title(self, title):
        self.cur.execute("SELECT Movie_ID FROM Movie WHERE Title=?", (title,))
        movie_id = self.cur.fetchone()
        return movie_id

    # Viewing the entire movie catalog
    def view_movie_catalog(self):
        self.cur.execute("SELECT * FROM Movie")
        return self.cur.fetchall()

    # Updating a movie's details

    # Deleting a movie from the catalog

    # Creating a new rental for a user
    def create_rental(self, user_id, rental_date, return_date, movie_id):
        self.cur.execute("INSERT INTO Rental (User_ID, Rental_Date, Return_Date, Movie_ID, isOngoing) VALUES (?, ?, "
                         "?, ?, 1)", (user_id, rental_date, return_date, movie_id))
        self.conn.commit()
        pass

    # Viewing a user's rentals

    def view_user_rented_movies(self, user_id):
        self.cur.execute(
            "SELECT Movie.Title, Rental.Rental_Date, Rental.Return_Date FROM (Rental INNER JOIN Movie ON "
            "Rental.Movie_ID = Movie.Movie_ID) WHERE User_ID=? AND isOngoing = 1",
            (user_id,))
        return self.cur.fetchall()

    # Updating a rental's status to designate that the rental is done
    def finish_rental(self, user_id, rental_date, return_date, movie_id):
        self.cur.execute("UPDATE Rental SET isOngoing = 0 WHERE User_ID=? AND Rental_Date=? AND Return_Date=? AND "
                         "Movie_ID=?", (user_id, rental_date, return_date, movie_id))
        self.conn.commit()

    # Adding a movie to  a user's cart
    def add_movie_to_cart(self, user_id, movie_id):
        self.cur.execute("INSERT INTO Cart (User_ID, Movie_ID) VALUES (?, ?)", (user_id, movie_id))
        self.conn.commit()

    # Selecting a specific movie in a user's cart
    def select_movie_in_cart(self, user_id, movie_id):
        self.cur.execute("SELECT * FROM Cart WHERE (User_ID=? AND Movie_ID=?)", (user_id, movie_id))
        return self.cur.fetchone()

    # Viewing a user's whole cart
    def view_user_cart(self, user_id):
        self.cur.execute(
            "SELECT Movie.Title, Movie.Renting_Fee FROM (Cart INNER JOIN Movie ON Cart.Movie_ID = Movie.Movie_ID) "
            "WHERE User_ID=?",
            (user_id,))
        return self.cur.fetchall()

    # Updating a user's cart

    # Emptying a user's cart
    def remove_from_cart(self, user_id, movie_id):
        self.cur.execute("DELETE FROM Cart WHERE User_ID=? AND Cart.Movie_ID=?", (user_id, movie_id))
        self.conn.commit()

    # Adding a review of a movie
    def submit_review(self, movie_id, rating, review):
        self.cur.execute("INSERT INTO Review (Movie_ID, Rating, Review_Text) VALUES (?, ?, ?)",
                         (movie_id, rating, review))
        self.conn.commit()

    # Viewing a movie's reviews
    def view_reviews(self):
        self.cur.execute(
            "SELECT Movie.Title, Review.Rating, Review.Review_Text FROM Review INNER JOIN Movie ON Review.Movie_ID = "
            "Movie.Movie_ID")
        return self.cur.fetchall()

    # Deleting a movie's reviews

    # Creating a user's wish list
    def add_movie_to_wishlist(self, user_id, movie_id):
        self.cur.execute("INSERT INTO WishList (User_ID, Movie_ID) VALUES (?, ?)", (user_id, movie_id))
        self.conn.commit()

    # Selecting a specific movie in a user's wish list
    def select_movie_in_wishlist(self, user_id, movie_id):
        self.cur.execute("SELECT * FROM WishList WHERE (User_ID=? AND Movie_ID=?)", (user_id, movie_id))
        return self.cur.fetchone()

    # Viewing a user's whole wishlist
    def view_user_wishlist(self, user_id):
        self.cur.execute(
            "SELECT Movie.Title FROM (WishList INNER JOIN Movie ON WishList.Movie_ID = Movie.Movie_ID) WHERE User_ID=?",
            (user_id,))
        return self.cur.fetchall()

    # Updating a user's wish list

    # Removing a movie from a user's wish list
    def remove_from_wishlist(self, user_id, movie_id):
        self.cur.execute("DELETE FROM WishList WHERE User_ID=? AND Movie_ID=?", (user_id, movie_id))
        self.conn.commit()

    # Closing connection to database
    def close_connection(self):
        self.conn.close()

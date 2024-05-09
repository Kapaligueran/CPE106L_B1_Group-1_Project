import bcrypt
import datetime
import dataaccess as da

database = da.DatabaseManagement('MovieRentalDB.db')


# class for user information
class User:
    def __init__(self, user_id, username, password):
        self.User_ID = user_id
        self.Username = username
        self.Password = password


# class for movie catalog
class Movie:
    def __init__(self, movie_id, title, synopsis, renting_fee, genre):
        self.Movie_ID = movie_id
        self.Title = title
        self.Synopsis = synopsis
        self.Renting_Fee = renting_fee
        self.Genre = genre


# class for user rental
class Rental:
    def __init__(self, rental_id, user_id, rental_date, return_date, movie_id, is_ongoing):
        self.Rental_ID = rental_id
        self.User_ID = user_id
        self.Rental_Date = rental_date
        self.Return_Date = return_date
        self.Movie_ID = movie_id
        self.isOngoing = is_ongoing


# class for user shopping cart
class Cart:
    def __init__(self, cart_id, user_id, movie_id):
        self.Cart_ID = cart_id
        self.User_ID = user_id
        self.Movie_ID = movie_id


# class for movie reviews
class Review:
    def __init__(self, review_id, movie_id, review_text, rating):
        self.Review_ID = review_id
        self.Movie_ID = movie_id
        self.Review_Text = review_text
        self.Rating = rating


# class for user's wish list
class WishList:
    def __init__(self, wish_list_id, user_id, movie_id):
        self.WishList_ID = wish_list_id
        self.User_ID = user_id
        self.Movie_ID = movie_id


# Function for checking if user entered all data for signup
def check_if_signup_not_empty(username, password):
    if username != '' and password != '':
        return True
    else:
        return False


# Function for checking if user entered all data for login
def check_if_login_not_empty(username, password):
    if username != '' and password != '':
        return True
    else:
        return False


# Function for checking user's existence in database
def check_if_user_does_not_exist(username):
    database.select_user_by_username(username)
    if database.select_user_by_username(username) is not None:
        return False
    else:
        return True


# Function to create new account
def create_account(username, password):
    encoded_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
    database.create_user(username, hashed_password)


# Function to verify is user inputted correct password
def verify_password(username, password):
    saved_password = database.get_password(username)
    if bcrypt.checkpw(password.encode('utf-8'), saved_password[0]):
        return True
    else:
        return False


# Function for getting the whole movie catalog
def get_movie_catalog():
    return database.view_movie_catalog()


# Function for selecting a movie
def select_movie(movie_id):
    current_movie_id = movie_id
    selected_movie = database.get_movie_details(current_movie_id)
    return selected_movie


# Function to get the current user's ID
def get_current_user_id(username):
    user_id_tuple = database.get_user_id(username)
    user_id = user_id_tuple[0] if user_id_tuple else None
    return user_id


# Function for getting a user's cart
def get_user_cart(user_id):
    return database.view_user_cart(user_id)


# Function to add a movie to a user's cart
def add_to_cart(user_id, movie_id):
    database.add_movie_to_cart(user_id, movie_id)


# Function to add a movie to a user's cart from wishlist
def add_to_cart_from_wishlist(user_id, title):
    movie_id_tuple = database.get_movie_id_from_title(title)
    movie_id = movie_id_tuple[0]
    database.add_movie_to_cart(user_id, movie_id)


# Function to remove a movie from a user's cart
def remove_from_cart(user_id, title):
    movie_id_tuple = database.get_movie_id_from_title(title)
    movie_id = movie_id_tuple[0]
    database.remove_from_cart(user_id, movie_id)


# Function for getting a user's wishlist
def get_user_wishlist(user_id):
    return database.view_user_wishlist(user_id)


# Function to add a movie to a user's wishlist
def add_to_wishlist(user_id, movie_id):
    database.add_movie_to_wishlist(user_id, movie_id)


# Function to remove a movie from a user's wishlist
def remove_from_wishlist(user_id, title):
    movie_id_tuple = database.get_movie_id_from_title(title)
    movie_id = movie_id_tuple[0]
    database.remove_from_wishlist(user_id, movie_id)


# Function to check if movie is already in a user's cart
def check_if_movie_in_cart(user_id, movie_id):
    if database.select_movie_in_cart(user_id, movie_id) is not None:
        return True
    else:
        return False


# Function to check if a movie is in a user's cart based on its title
def check_if_movie_in_cart_from_title(user_id, title):
    movie_id_tuple = database.get_movie_id_from_title(title)
    movie_id = movie_id_tuple[0]
    if database.select_movie_in_cart(user_id, movie_id) is not None:
        return True
    else:
        return False


# Function to check if movie is already in a user's wishlist
def check_if_movie_in_wishlist(user_id, movie_id):
    if database.select_movie_in_wishlist(user_id, movie_id) is not None:
        return True
    else:
        return False


# Function for getting the list of a user's rented movies
def get_user_rented_movies(user_id):
    return database.view_user_rented_movies(user_id)


# Function for checking a movie out of a user's cart and renting that movie
def checkout(user_id, title):
    movie_id_tuple = database.get_movie_id_from_title(title)
    movie_id = movie_id_tuple[0]
    rental_date = datetime.datetime.now().date()
    return_date = rental_date + datetime.timedelta(days=7)
    database.create_rental(user_id, rental_date, return_date, movie_id)
    database.remove_from_cart(user_id, movie_id)


# Function for returning a movie from being rented
def return_movie(user_id, rental_date, return_date, title):
    movie_id_tuple = database.get_movie_id_from_title(title)
    movie_id = movie_id_tuple[0]
    database.finish_rental(user_id, rental_date, return_date, movie_id)


# Function for viewing all reviews
def get_reviews():
    return database.view_reviews()


# Function for submitting review
def submit_review(movie_id, rating, review):
    database.submit_review(movie_id, rating, review)

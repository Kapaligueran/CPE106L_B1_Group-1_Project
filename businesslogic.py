import bcrypt
import dataaccess as da

database = da.DatabaseManagement('MovieRentalDB.db')


# class for user information
class User:
    def __init__(self, user_id, username, password, given_name, middle_name, last_name, suffix, email, phone_number):
        self.User_ID = user_id
        self.Username = username
        self.Password = password
        self.Given_Name = given_name
        self.Middle_Name = middle_name
        self.Last_Name = last_name
        self.Suffix = suffix
        self.Email = email
        self.Phone_Number = phone_number


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
def check_if_signup_not_empty(username, password, given_name, middle_name, last_name, suffix, email, phone_number):
    if username != '' and password != '' and email != '' and phone_number != '' and given_name != '' and last_name != '':
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
def create_account(username, password, given_name, middle_name, last_name, suffix, email, phone_number):
    encoded_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
    if middle_name == '':
        middle_name = None
    if suffix == '':
        suffix = None
    print(hashed_password)
    database.create_user(username, hashed_password, given_name, middle_name, last_name, suffix, email, phone_number)


def verify_password(username, password):
    saved_password = database.get_password(username)
    if bcrypt.checkpw(password.encode('utf-8'), saved_password[0]):
        return True
    else:
        return False

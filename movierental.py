class MovieCatalog:
    def __init__(self, title, genre, price):
        self.title = title
        self.genre = genre
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, movie):
        self.items.append(movie)

    def remove_item(self, index):
        del self.items[index]

    def display_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Your Shopping Cart:")
            for idx, item in enumerate(self.items, start=1):
                print(f"{idx}. {item.title} - {item.genre} (${item.price})")

def homepage():
        # Initialize movie catalogs
        movies = [
            MovieCatalog("Inception", "Science Fiction", 10),
            MovieCatalog("The Shawshank Redemption", "Drama", 8),
            MovieCatalog("The Dark Knight", "Action", 12),
            MovieCatalog("Pulp Fiction", "Crime", 9)
        ]

        # Initialize shopping cart
        cart = ShoppingCart()

        # Display home page with movie catalogs
        print("\nWelcome to the Movie Catalog:")
        for idx, movie in enumerate(movies, start=1):
            print(f"{idx}. {movie.title} - {movie.genre} (${movie.price})")

        while True:
            choice = input("\nEnter the number of the movie you want to add to your cart (or 'checkout' to finish): ")

            if choice.lower() == 'checkout':
                if cart.items:
                    shopping_cart_page(cart)
                    break
                else:
                    print("Your shopping cart is empty.")
            else:
                try:
                    choice_idx = int(choice)
                    if 1 <= choice_idx <= len(movies):
                        selected_movie = movies[choice_idx - 1]
                        cart.add_item(selected_movie)
                        print(f"{selected_movie.title} has been added to your cart.")
                    else:
                        print("Invalid choice. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number or 'checkout'.")

def shopping_cart_page(cart):
    while True:
        print("\nShopping Cart:")
        cart.display_cart()
        print("\n1. Checkout/Pay")
        print("2. Delete a movie")
        print("3. Go back to Home Page")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            print("Your checkout/pay functionality goes here.")
            break
        elif choice == '2':
            if not cart.items:
                print("Your shopping cart is empty.")
            else:
                cart.display_cart()
                index_to_delete = input("Enter the number of the movie you want to delete: ")
                try:
                    index_to_delete = int(index_to_delete)
                    if 1 <= index_to_delete <= len(cart.items):
                        cart.remove_item(index_to_delete - 1)
                        print("Movie deleted from your cart.")
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid input.")
        elif choice == '3':
            homepage()
        else:
            print("Invalid choice.")

registered_users = {"user1":"pass1"}  # Database of registered users (username: password)

def login():
    # Ask for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username exists and if the password matches
    if username in registered_users and registered_users[username] == password:
        print("Login successful!")
        homepage()
    else:
        print("Invalid username or password. Please try again.")
        login()

def signup():
    # Ask for username and password
    username = input("Enter your desired username: ")

    # Check if the username already exists
    if username in registered_users:
        print("Username already exists. Please choose a different one.")
        signup()
    else:
        password = input("Enter your password: ")
        # Store the username and password in the database
        registered_users[username] = password
        print("Signup successful! You can now login with your credentials.")
        
    print("Welcome!")
    print("1. Login")
    print("2. Signup")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        login()
    elif choice == "2":
        signup()
    else:
        print("Invalid choice. Please choose either 1 or 2.")

# Ask the user to choose between login and signup
print("Welcome!")
print("1. Login")
print("2. Signup")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    login()
elif choice == "2":
    signup()
else:
    print("Invalid choice. Please choose either 1 or 2.")

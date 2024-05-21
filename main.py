from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Database to store registered users
registered_users = {}
artists_by_genre = {
    "rock": ["Led Zeppelin", "Queen", "The Beatles"],
    "pop": ["Michael Jackson", "Madonna", "Taylor Swift"],
    "hip-hop": ["Tupac", "The Notorious B.I.G.", "Kanye West"],
    "jazz": ["Miles Davis", "John Coltrane", "Louis Armstrong"]
}


def login():
    print(Fore.YELLOW + "=== Login ===")
    print(Fore.CYAN + "Choose login method:")
    print(Fore.CYAN + "1. Username + Password")
    print(Fore.CYAN + "2. Name + Password")
    print(Fore.RED + "Beware little information is required. Therefore you can easily get hacked")
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
    elif choice == "2":
        name = input("Enter name: ")
        username = get_username_by_name(name)
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
        login()
        return

    password = input("Enter password: ")

    if username in registered_users and registered_users[username]["password"] == password:
        print(Fore.GREEN + "Login successful!")
        print(Fore.YELLOW + "🏠")  # Display home symbol
        main_menu(username)
    else:
        print(Fore.RED + "Invalid username or password.")
        choice = input("Do you want to register? (yes/no): ").lower()
        if choice == "yes":
            register()
        else:
            print("Goodbye!")


def register():
    print(Fore.YELLOW + "=== Registration ===")
    name = input("Enter your name: ")
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    registered_users[username] = {"name": name, "password": password, "saved_artists": []}
    print(Fore.GREEN + "Registration successful!")
    print(Fore.CYAN + "Welcome to Music Fashion App, " + name + "!")


def main_menu(username):
    print(Fore.YELLOW + f"=== Welcome, {registered_users[username]['name']} ===")
    print(Fore.CYAN + "1. View fashion aesthetic based on music taste")
    print(Fore.CYAN + "2. Manage saved artists")
    print(Fore.CYAN + "3. Search for artists by genre")
    print(Fore.CYAN + "4. Settings")
    print(Fore.CYAN + "5. Logout (X)")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("View fashion aesthetic")
        # Implement this functionality
    elif choice == "2":
        manage_saved_artists(username)
    elif choice == "3":
        search_artists_by_genre(username)
    elif choice == "4":
        settings(username)
    elif choice.lower() == "x" or choice == "5":
        print("Logout successful!")
        return
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
        main_menu(username)


def manage_saved_artists(username):
    print(Fore.YELLOW + "=== Manage Saved Artists ===")
    if not registered_users[username]["saved_artists"]:
        print(Fore.CYAN + "You have no saved artists.")
    else:
        print(Fore.CYAN + "Your saved artists:")
        for artist in registered_users[username]["saved_artists"]:
            print(Fore.CYAN + f"- {artist}")
        artist_to_delete = input("Enter the name of the artist you want to delete: ")
        if artist_to_delete in registered_users[username]["saved_artists"]:
            registered_users[username]["saved_artists"].remove(artist_to_delete)
            print(Fore.GREEN + f"Artist {artist_to_delete} deleted successfully!")
        else:
            print(Fore.RED + f"Artist {artist_to_delete} not found in your saved artists.")
    main_menu(username)


def search_artists_by_genre(username):
    print(Fore.YELLOW + "=== Search Artists by Genre ===")
    genre = input("Enter a genre: ").lower()
    if genre in artists_by_genre:
        print(Fore.CYAN + f"Artists in {genre} genre:")
        for artist in artists_by_genre[genre]:
            print(Fore.CYAN + f"- {artist}")
        save_artist = input("Do you want to save any artist to your list? (yes/no): ").lower()
        if save_artist == "yes":
            artist_to_save = input("Enter the name of the artist you want to save: ")
            if artist_to_save in artists_by_genre[genre]:
                registered_users[username]["saved_artists"].append(artist_to_save)
                print(Fore.GREEN + f"Artist {artist_to_save} saved successfully!")
            else:
                print(Fore.RED + "Artist not found in the selected genre.")
    else:
        print(Fore.RED + "Genre not found. Please try again.")
    main_menu(username)

def settings(username):
    print(Fore.YELLOW + "=== Settings ===")
    print(Fore.CYAN + "1. Change password")
    print(Fore.CYAN + "2. Delete account")
    print(Fore.CYAN + "3. Go back to main menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_password = input("Enter new password: ")
        registered_users[username]["password"] = new_password
        print(Fore.GREEN + "Password changed successfully!")
        settings(username)
    elif choice == "2":
        confirm = input("Are you sure you want to delete your account? This action cannot be undone. (yes/no): ").lower()
        if confirm == "yes":
            del registered_users[username]
            print(Fore.GREEN + "Account deleted successfully!")
            return
        else:
            print("Account deletion cancelled.")
            settings(username)
    elif choice == "3":
        main_menu(username)
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
        settings(username)

def get_username_by_name(name):
    for username, user_data in registered_users.items():
        if user_data["name"].lower() == name.lower():
            return username
    return None

# Main program loop
while True:
    print(Fore.BLUE + "=== Music Fashion App ===")
    print(Fore.CYAN + "Welcome to Music Fashion App!")
    print(Fore.CYAN + "Whether you're a new user or returning, we've got something special for you!")
    print(Fore.CYAN + "Unlock your personalized fashion journey now.")
    print(Fore.CYAN + "1. Login")
    print(Fore.CYAN + "2. Register")
    print(Fore.CYAN + "3. Quit (X)")

    option = input("Enter your choice: ")

    if option == "1":
        login()
    elif option == "2":
        register()
    elif option.lower() == "x" or option == "3":
        print("Goodbye!")
        break
    else:
        print(Fore.RED + "Invalid choice. Please try again.")

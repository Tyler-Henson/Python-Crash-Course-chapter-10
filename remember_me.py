import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    loop = True

    if username:
        while loop:  # determines if this is a returning user
            response = input("Are you " + username + '? (y/n) ')
            if response == 'y':
                print("Welcome back, " + username + "!")
                loop = False
            elif response == 'n':
                username = get_new_username()
                print(
                    "We'll remember you when you come back, " +
                    username + "!")
                loop = False

    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


if __name__ == '__main__':
        greet_user()

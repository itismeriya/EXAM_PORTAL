import json
from getpass import getpass
from utils import load_data, save_data

class Auth:
    def __init__(self):
        self.users_file = 'data/users.json'
        self.users = load_data(self.users_file)

    def register(self):
        username = input("Enter username: ")
        password = getpass("Enter password: ")

        if username in self.users:
            print("Username already exists. Try a different one.")
        else:
            self.users[username] = {'password': password}
            save_data(self.users_file, self.users)
            print("Registration successful.")

    def login(self):
        username = input("Enter username: ")
        password = getpass("Enter password: ")

        if username in self.users and self.users[username]['password'] == password:
            print("Login successful.")
        else:
            print("Invalid username or password.")

# Example demonstrating Single Responsibility Principle

# Class responsible for handling user data
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    # Method responsible for formatting user data
    def format_user_data(self):
        return f"Username: {self.username}, Email: {self.email}"

# Class responsible for persisting user data to a database
class UserRepository:
    def __init__(self):
        self.users = []

    # Method responsible for adding a user to the repository
    def add_user(self, user):
        self.users.append(user)

    # Method responsible for retrieving all users from the repository
    def get_all_users(self):
        return self.users

# Usage
if __name__ == "__main__":
    # Creating a user
    user1 = User("john_doe", "john@example.com")

    # Adding the user to the repository
    user_repo = UserRepository()
    user_repo.add_user(user1)

    # Retrieving all users from the repository and printing their data
    for user in user_repo.get_all_users():
        print(user.format_user_data())

    
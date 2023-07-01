# Password-Manager-GUI
A well-encrypted open-source password-manager program for personal use

 # To use this password management tool, follow these steps:

Make sure you have Python installed on your system. Python can be downloaded and installed for free from the official Python website: # https://www.python.org/downloads/

Install the cryptography package to use the cryptographic functionality. You can install the package using pip by running the following command in the command line:
# pip install cryptography

Create a new Python file and open it in your preferred editor.
Copy the provided code for the PasswordManager class into the Python file.
Ensure that in the same folder where the Python file is located, you have write and execute permissions. This is necessary for creating the passwords.json file in that directory.

In the Python file, create an instance of the PasswordManager class and specify the path to the key file (key_file). For example:
# manager = PasswordManager('key.key')

Use the methods in the PasswordManager class to store, retrieve, and delete passwords. You can use the following methods:

-store_password(username, password):    Stores a password for a specified username.
-retrieve_password(username, password): Retrieves a password for a specified username.
-delete_password(username):             Deletes the password associated with a specified username.
For example:
# Store password
manager.store_password('user1', 'password123')

# Retrieve password
hashed_password = manager.retrieve_password('user1', 'password123')
print("Hashed Password:", hashed_password)

# Delete password
manager.delete_password('user1')

Run the Python file in a terminal or in a Python development environment to execute the code and use the password manager.

Enjoy ! 

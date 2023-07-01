from cryptography.fernet import Fernet
import bcrypt
import json
import tkinter as tk
from tkinter import messagebox

class PasswordManagerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Manager")
        
        self.key_file = 'key.key'
        self.key = self.load_key()

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.store_button = tk.Button(self.root, text="Store Password", command=self.store_password)
        self.store_button.pack()

        self.retrieve_button = tk.Button(self.root, text="Retrieve Password", command=self.retrieve_password)
        self.retrieve_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete Password", command=self.delete_password)
        self.delete_button.pack()

    def load_key(self):
        try:
            with open(self.key_file, 'rb') as f:
                key = f.read()
                return key
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
            return key

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password

    def verify_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode(), hashed_password)

    def encrypt_password(self, password):
        cipher_suite = Fernet(self.key)
        encrypted_password = cipher_suite.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        cipher_suite = Fernet(self.key)
        decrypted_password = cipher_suite.decrypt(encrypted_password)
        return decrypted_password.decode()

    def store_password(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            hashed_password = self.hash_password(password)
            encrypted_password = self.encrypt_password(hashed_password.decode())
            password_data = {username: encrypted_password.decode()}

            try:
                with open('passwords.json', 'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = {}

            data.update(password_data)

            with open('passwords.json', 'w') as f:
                json.dump(data, f)
            
            messagebox.showinfo("Success", "Password stored successfully.")
        else:
            messagebox.showwarning("Error", "Please enter both username and password.")

    def retrieve_password(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            with open('passwords.json', 'r') as f:
                data = json.load(f)

            if username in data:
                encrypted_password = data[username]
                hashed_password = self.decrypt_password(encrypted_password.encode())
                if self.verify_password(password, hashed_password.encode()):
                    messagebox.showinfo("Success", f"Retrieved password for {username}: {hashed_password}")
                else:
                    messagebox.showwarning("Error", "Incorrect username or password.")
            else:
                messagebox.showwarning("Error", "Username not found.")
        else:
            messagebox.showwarning("Error", "Please enter both username and password.")

    def delete_password(self):
        username = self.username_entry.get()

        if username:
            with open('passwords.json', 'r') as f:
                data = json.load(f)

            if username in data:
                del data[username]

                with open('passwords.json', 'w') as f:
                    json.dump(data, f)
                
                messagebox.showinfo("Success", "Password deleted successfully.")
            else:
                messagebox.showwarning("Error", "Username not found.")
        else:
            messagebox.showwarning("Error", "Please enter a username.")

    def run(self):
        self.root.mainloop()


# Creare și rulare interfață GUI
gui = PasswordManagerGUI()
gui.run()

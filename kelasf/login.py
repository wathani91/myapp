import tkinter as tk
from tkinter import messagebox

class LoginFrame(tk.Frame):
    def __init__(self, master, login_callback):
        super().__init__(master)
        self.login_callback = login_callback
        
        self.label_title = tk.Label(self, text="Login Form", font=("Arial", 14))
        self.label_username = tk.Label(self, text="Username:")
        self.entry_username = tk.Entry(self)
        self.label_password = tk.Label(self, text="Password:")
        self.entry_password = tk.Entry(self, show="*")
        self.btn_login = tk.Button(self, text="Login", command=self.attempt_login)
        
        # Layout
        self.label_title.pack(pady=10)
        self.label_username.pack()
        self.entry_username.pack()
        self.label_password.pack()
        self.entry_password.pack()
        self.btn_login.pack(pady=10)
        
    def attempt_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if username == "" or password == "":
            messagebox.showerror("Error", "Username dan password harus diisi!")
        else:
            self.login_callback(username)  # Panggil callback ke MainApp

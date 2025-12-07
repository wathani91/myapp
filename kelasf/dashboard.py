import tkinter as tk

class DashboardFrame(tk.Frame):
    def __init__(self, master, username, logout_callback):
        super().__init__(master)
        self.logout_callback = logout_callback
        
        self.label_welcome = tk.Label(
            self, 
            text=f"Selamat datang, {username}!",
            font=("Arial", 16)
        )
        self.btn_logout = tk.Button(
            self, 
            text="Logout", 
            command=self.logout,
            bg="red",
            fg="white"
        )
        
        # Layout
        self.label_welcome.pack(pady=50)
        self.btn_logout.pack()

    def logout(self):
        self.logout_callback()  # Panggil callback ke MainApp
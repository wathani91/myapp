import tkinter as tk
from kelasf.login import LoginFrame
from kelasf.dashboard import DashboardFrame

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("Aplikasi GUI")
        
        self.current_frame = None
        self.show_login()
        
    def show_login(self):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = LoginFrame(
            self.root, 
            login_callback=self.show_dashboard
        )
        self.current_frame.pack(padx=20, pady=20)
        
    def show_dashboard(self, username):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = DashboardFrame(
            self.root,
            username=username,
            logout_callback=self.show_login
        )
        self.current_frame.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
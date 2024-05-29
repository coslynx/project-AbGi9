import tkinter as tk

class AutomationGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Discord Account Automation")
        
        self.label_username = tk.Label(self.root, text="Username:")
        self.label_username.pack()
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack()
        
        self.label_email = tk.Label(self.root, text="Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack()
        
        self.label_password = tk.Label(self.root, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()
        
        self.button_create_account = tk.Button(self.root, text="Create Account", command=self.create_account)
        self.button_create_account.pack()
        
    def create_account(self):
        username = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        # Add logic here to create a Discord account using the provided details
        
        # Display success or failure message
        success_label = tk.Label(self.root, text="Account created successfully!")
        success_label.pack()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AutomationGUI()
    app.run()
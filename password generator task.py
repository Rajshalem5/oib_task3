
import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip


class PasswordGenerator:
    def __init__(self, window):
        self.window = window
        self.window.title("Password Generator🔑🔐")
        self.l1 = tk.Label(window, text="Welcome to Password generator:", fg="Blue", font='18')
        self.l1.pack(pady=20)

        self.f1 = tk.Frame(window)
        self.f1.pack(pady=20)
        self.l2 = tk.Label(self.f1, text="Enter length of Password: ")
        self.l2.pack(side=tk.LEFT)
        self.length = tk.Entry(self.f1, width=20)
        self.length.pack(side=tk.LEFT, padx=10)

        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()

        self.c3 = tk.Checkbutton(window, text="Character", variable=self.var3, onvalue=1, offvalue=0)
        self.c3.pack(pady=0)
        self.c1 = tk.Checkbutton(window, text="Special_Character", variable=self.var1, onvalue=1, offvalue=0)
        self.c1.pack(pady=0)
        self.c2 = tk.Checkbutton(window, text="Numbers", variable=self.var2, onvalue=1, offvalue=0)
        self.c2.pack(pady=0)

        self.sp = tk.Button(window, text="Submit", command=self.check)
        self.sp.pack(pady=10)

        self.copy_button = tk.Button(window, text="Copy Password", command=self.copy_password)
        self.copy_button.pack(pady=10)

    def check(self):
        if self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0:
            tk.messagebox.showwarning("Missing", "At least one option must be selected!!")
            return
        self.click()

    def click(self):
        password = []
        x = 0
        if self.var1.get() == 1 and self.var2.get() == 1 and self.var3.get() == 1:
            character = string.ascii_letters + string.punctuation + string.digits
            while x != int(self.length.get()):
                password.append(random.choice(character))
                x += 1
        elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1:
            character = string.ascii_letters
            while x != int(self.length.get()):
                password.append(random.choice(character))
                x += 1
        elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0:
            character = string.digits
            while x != int(self.length.get()):
                password.append(random.choice(character))
                x += 1
        elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 1:
            character = string.ascii_letters + string.digits
            while x != int(self.length.get()):
                password.append(random.choice(character))
                x += 1
        elif self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 0:
            character = string.punctuation
            while x != int(self.length.get()):
                password.append(random.choice(character))
                x += 1
        elif self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 1:
            character = string.ascii_letters + string.punctuation
            while x != int(self.length.get()):
                password.append(random.choice(character))
                x += 1
        elif self.var1.get() == 1 and self.var2.get() == 1 and self.var3.get() == 0:
            character = string.punctuation + string.digits
            while x != int(self.length.get()):
                password.append(random.choice(character))
                x += 1

        password = "".join(password)

        self.c1.destroy()
        self.c2.destroy()
        self.c3.destroy()
        self.l1.config(text=f"Your New Password:\n\n {password}", fg="Green")
        self.l1.pack(pady=20)
        self.l2.destroy()
        self.length.destroy()
        self.sp.destroy()
        self.generated_password = password

    def copy_password(self):
        pyperclip.copy(self.generated_password)
        tk.messagebox.showinfo("Copied", "Password copied to clipboard!")


if __name__ == "__main__":
    window = tk.Tk()
    app = PasswordGenerator(window)
    window.geometry('500x300')
    window.mainloop()

import tkinter as tk
from tkinter import messagebox

class Calclutur:
    def __init__(self, root):
        self.root = root
        self.root.title("Calclutur - Simple Python Calculator")

        self.entry = tk.Entry(root, width=25, borderwidth=3, font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        for (text, row, col, colspan) in [(*btn, 1) if len(btn) == 3 else btn for btn in buttons]:
            button = tk.Button(self.root, text=text, width=10, height=2, font=("Arial", 14),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew")

    def on_button_click(self, char):
        if char == "C":
            self.entry.delete(0, tk.END)
        elif char == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.entry.delete(0, tk.END)
            except Exception:
                messagebox.showerror("Error", "Invalid input")
                self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calclutur(root)
    root.mainloop()

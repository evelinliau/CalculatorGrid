import tkinter as tk
import ttkbootstrap as tb 
from ttkbootstrap import Style

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.style = Style(theme='superhero')  

        self.entry = tk.Entry(master, width=20, font=("Arial", 14), justify="right")
        self.entry.grid(padx=10, pady=10, row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(master, text=text, width=5, height=2, font=("Arial", 12),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5)

    def on_button_click(self, char):
        if char == '=':
            
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))

            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, char)


if __name__ == "__main__":

    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

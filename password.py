import string
import random
import tkinter as tk
from tkinter import Label, Entry, Button, Checkbutton, IntVar

def generate_password():
    length = length_var.get()
    character_list = ""

    if use_letters_var.get():
        character_list += string.ascii_letters
    if use_digits_var.get():
        character_list += string.digits
    if use_special_chars_var.get():
        character_list += string.punctuation

    if not character_list:
        result_label.config(text="Please select at least one character set.")
        return

    password = [random.choice(character_list) for _ in range(length)]
    password_str = "".join(password)
    result_label.config(text="Generated Password: " + password_str)

window = tk.Tk()
window.title("Password Generator")

length_label = Label(window, text="Enter password length:")
length_label.pack()
length_var = tk.IntVar()
length_entry = Entry(window, textvariable=length_var)
length_entry.pack()

use_letters_var = IntVar()
use_digits_var = IntVar()
use_special_chars_var = IntVar()

letters_checkbox = Checkbutton(window, text="Letters", variable=use_letters_var)
digits_checkbox = Checkbutton(window, text="Digits", variable=use_digits_var)
special_chars_checkbox = Checkbutton(window, text="Special characters", variable=use_special_chars_var)

letters_checkbox.pack()
digits_checkbox.pack()
special_chars_checkbox.pack()


generate_button = Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = Label(window, text="")
result_label.pack()

window.mainloop()

from primality import primalCheck
from factorial import fact
import tkinter as tk
import re

# Checks if number is prime
# Biggest prime number = 67,280,421,310,721
# Max factorial before it throws an error = 1558!

def isPrime(new_val):
    if primalCheck(new_val)==True:
        value1["text"] = str(f"{new_val:,}") + " is a prime number."
    else: value1["text"] = str(f"{new_val:,}") + " is not a prime number."

# Displays the factorial of a value
def factorial(new_val):
    value2["text"] = str(new_val)+ "! is " + str(fact(new_val)) + "."

# Button event
def handle_click():
    value = entry.get()

    if re.search("^\d{1,3}(?:,\d{3})*$", value):
        value = value.replace(',','')

    if value.isdigit() == False or int(value) < 0:
        value1["text"] = ""
        value2["text"] = ""
        warning["text"] = "Invalid input!"
    
    elif int(value) > 1558:
        value1["text"] = ""
        value2["text"] = "Factorial error: Please input a number less than or equal to 1558."
        isPrime(int(value))

    else:
        warning["text"] = ""
        isPrime(int(value))
        factorial(int(value))
    
# Create new window
window = tk.Tk()

greeting = tk.Label(text="Input entry")

entry = tk.Entry()
submit = tk.Button(text="Submit",command=handle_click)
frame = tk.Frame(width=500, height=100)
warning = tk.Label()
value1 = tk.Label()
value2 = tk.Label(wraplength=450)


greeting.pack()
entry.pack()
submit.pack()
frame.pack()
warning.pack()
value1.pack()
value2.pack()
frame.pack()

# Main event must be executed
window.mainloop()
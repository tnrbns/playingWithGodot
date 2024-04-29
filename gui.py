from primality import primalCheck
from factorial import fact
import tkinter as tk

# Checks if number is prime
def isPrime(new_val):
    if primalCheck(new_val)==True:
        value1["text"] = str(new_val) + " is a prime number"
    else: value1["text"] = str(new_val) + " is not a prime number"

# Displays the factorial of a value
def factorial(new_val):
    value2["text"] = fact(new_val)

# Button event
def handle_click():
    value = entry.get()

    if value.isalpha() == True or int(value) < 0:
        warning["text"] = "Invalid input!"

    else:
        value = int(value)    
        isPrime(value)
        factorial(value)
    
# Create new window
window = tk.Tk()

greeting = tk.Label(text="Input entry")

entry = tk.Entry()
submit = tk.Button(text="Submit",command=handle_click)
frame = tk.Frame(width=400, height=100)
warning = tk.Label()
value1 = tk.Label()
value2 = tk.Label()


greeting.pack()
entry.pack()
submit.pack()
frame.pack()
warning.pack()
value1.pack()
value2.pack()




# Main event must be executed
window.mainloop()
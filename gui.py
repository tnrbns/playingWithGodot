from primality import primalCheck
from factorial import fact
import tkinter as tk

def isPrime(new_val):
    if primalCheck(new_val)==True:
        value1["text"] = str(new_val) + " True dawg"
    else: value1["text"] = str(new_val) + " Naw not"

def factorial(new_val):
    value2["text"] = fact(new_val)

def handle_click():
    value = int(entry.get())
    isPrime(value)
    factorial(value)
    
# Declare new 
window = tk.Tk()

greeting = tk.Label(text="Input entry")

entry = tk.Entry()
submit = tk.Button(text="Submit",command=handle_click)
frame = tk.Frame(width=400, height=100)
value1 = tk.Label(text="prime")
value2 = tk.Label(text="fact")


greeting.pack()
entry.pack()
submit.pack()
frame.pack()
value1.pack()
value2.pack()




# Main event must be executed
window.mainloop()
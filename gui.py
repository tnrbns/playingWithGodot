from primality import primalCheck # Primality function from primality.py
from factorial import fact # Factorial function from factorial.py
from tkinter import ttk # Module for our GUI
from ttkthemes import ThemedTk # Better UI design
import re # Module to check regular expressions

# Biggest prime number = 67,280,421,310,721
# Max factorial before it throws an error = 1558!

# Displays in tkinter Label whether a number is prime or not
def isPrime(new_val):
    if primalCheck(new_val)==True:
        primeLabel["text"] = str(f"{new_val:,}") + " is a prime number."
    else: primeLabel["text"] = str(f"{new_val:,}") + " is not a prime number."

# Displays the factorial of a value
def factorial(new_val):
    factLabel["text"] = str(new_val)+ "! is " + str(fact(new_val)) + "."

# Function to handle labels given input
def handle_click():
    value = entry.get() # Gets number value from textbox input
    
# Regular expression to determine if input is a valid number 
# e.g. 1,234,567 is considered valid, but 1,23,456 is not a valid number
    if re.search("^\d{1,3}(?:,\d{3})*$", value):
        value = value.replace(',','')           # Removes all the commas in the value so it can be used for prime and factorial

# Invalid input warning occurs when:
    # Invalid characters on input (i.e)
    # Value is less than zero (i.e. negative numbers)
    # Input starts with zero followed by a nonzero number (i.e. phone numbers)
    if value.isdigit() == False or int(value) < 0 or value[0]=='0':
        primeLabel["text"] = "" # Resets prime label
        factLabel["text"] = "" # Resets factorial label
        warningLabel["text"] = "Invalid input!" # Display error

# Factorial or prime error: required due to computational limitations
    elif int(value) > 1558: # Throw factorial error if value greater than 1558
        primeLabel["text"] = ""
        factLabel["text"] = "Factorial error: Please input a number less than or equal to 1558."
        if int(value) > 67280421310721: # Throw prime error if value greater than 67280421310721
            primeLabel["text"] = "Prime error: Highest possible value reached."
        else: isPrime(int(value))
        warningLabel["text"] = "" # Resets warning label

# Proceed with function as usual if no errors
    else:
        warningLabel["text"] = ""
        isPrime(int(value))
        factorial(int(value))
    
# GUI that will be displayed in the exeutable
window = ThemedTk(theme="yaru") # Display a window 
window.title("PrimeFact") # Title of program

window.geometry("650x250") # Fixed sized of 650x250 pixels
# Ensured window is not resizable
window.minsize(650,250)
window.maxsize(650,250)

# Changed BGM color 
window.config(background="#F5F6F7")

# Header of program
greeting = ttk.Label(window, text="PrimeFact", font=('Montserrat', '25', 'bold'))
greeting.grid(row=0,columnspan=2,padx=10,pady=15)

# Label to input number
inputLabel = ttk.Label(window, text="Input a number:", font=('Montserrat', '15','bold'))
inputLabel.grid(row=1,column=0,sticky="W",padx=10,pady=3)

# Textbox for input
entry = ttk.Entry(window,width=40,font=('Montserrat', '12'))
entry.grid(row=2,column=0,sticky="W",padx=8)

# Submit button
submit = ttk.Button(window, text="Submit", width=25, command=handle_click)
submit.grid(row=2,column=1)

# Label that appears when input is invalid.
warningLabel = ttk.Label(window, text="",font=('Montserrat', '10','bold'), foreground='red')
warningLabel.grid(row=3,column=0,sticky="W",padx=10,pady=3)

# Displays primaility check of input
primeLabel = ttk.Label(window, text="",font=('Montserrat', '12', 'bold'))
primeLabel.grid(row=4,column=0,columnspan=2,sticky="W",padx=10,pady=2)

# Displays factorial of input
factLabel = ttk.Label(window, text="", font=('Montserrat', '12', 'bold'))
factLabel.grid(row=5,column=0,columnspan=2,sticky="W",padx=10,pady=2)

# Main event GUI that will be executed
window.mainloop()
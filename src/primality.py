from math import sqrt # Module needed for sqrt() function

# Function to check if number is prime
def primalCheck(n):
    if n < 2: 
        return False # 0 and 1 are not prime numbers, return false
    for i in range(2, int(sqrt(n)) + 1): # Divide from 2 to sqrt(n)+1 of a given number 
        if n % i == 0: 
            return False # If number has no remainder, return false
    return True # Else return true
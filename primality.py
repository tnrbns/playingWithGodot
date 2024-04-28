from math import sqrt # Module needed for sqrt() function
# Function to check if number is prime

def primalCheck(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
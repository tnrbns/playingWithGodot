# Function to get factorial
from decimal import Decimal # Decimal needed for larger numbers

def fact(n):
    result = 1 # Start result with 1 (0! = 1)
    for i in range(1,n+1):
        result *= i # Iterate by multiplying iterator from the result

    if len(str(result)) < 15: # Display comma-separated results for less than 15 digits 
        return f"{result:,}"
    else: return f"{Decimal(result):.10e}" # Otherwise, display scientific notation of result (for larger numbers)




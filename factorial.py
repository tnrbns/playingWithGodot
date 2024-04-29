# Function to get factorial
from decimal import Decimal

def fact(n):
    result = 1
    for i in range(1,n+1):
        result = result * i

    if len(str(result)) < 15:
        return f"{result:,}"
    else: return f"{Decimal(result):.10e}"




import re

# ^\d{1,3}(?:,\d{3})*$
#Check if the string starts with "The" and ends with "Spain":

def rematch(a):
    x = re.search("^\d{1,3}(?:,\d{3})*$", a)
    if x:
        print(x)
    else:
        print("No match")

rematch('12,555,333')
rematch("12,333")
rematch("1243")
rematch("1243,6")
rematch("1243,6,6,788,111")






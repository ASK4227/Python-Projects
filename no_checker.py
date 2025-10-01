def number_checker(n):
    x = int(n)
    if x > 0:
        return("no is +ve")
    elif x == 0:
        return("no is zero")
    else:
        return("no is negative")
        
    
n = input("enter a number")

print(number_checker(n))

def positive_number_checker(n):
    if n.isdigit():
        return("u entered a +ve no")
    else:
        return("no isn't positive -ve")
    
n = input("enter a number")

print(positive_number_checker(n))

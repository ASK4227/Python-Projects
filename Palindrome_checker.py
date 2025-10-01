def Palindrome_Checker(n):
    x = list(str(n))
    if x[0] == x[-1]:
        return True
    else:
        return False
        
print(Palindrome_Checker(125))
lst = list()

def is_it_palindrome(x):
    
    if len(x) <= 1:
        return True
    
    if x[0] == x[-1]:  
        
        return is_it_palindrome(x[1:-1])
    
    return False

    
def file_loader(file_open):
    with open(file_open, "r") as fil_opn:
        fil_opn = fil_opn.read().strip().split()
        for t in fil_opn:
            if len(t) > 1 and is_it_palindrome(t):
                lst.append(t)
    
    return(lst)

file_open = input("Enter a file location here")

rek = file_loader(file_open)

print(rek)
def recursive_func(n):
    if n == 0:
        return 0
    else:
        return n + recursive_func(n-1)
    
print(recursive_func(10))
    
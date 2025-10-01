def paramter_acceptor(a, b):
    a = int(a)
    b = int(b)
    def additioner():
        nonlocal a
        nonlocal b
        return(a + b)
    
    return(additioner())
        
print(paramter_acceptor(10, 20))
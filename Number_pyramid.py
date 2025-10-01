def number_pyramid(n):
    for i in range(1, n):
        for x in range(i):
            print(i, end = " ")
        print("")
        
        
print(number_pyramid(6))
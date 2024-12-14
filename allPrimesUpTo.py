def allPrimesUpTo(num):
    
    lst = list()

    for number in range(2, num+1):
        for factor in range(2, int(number ** 0.5) + 1):
            if number % factor == 0:
                break
        else:
            lst.append(number)
        
    return lst

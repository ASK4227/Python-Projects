def even_numbers(x, y):
    z = list()
    for i in range(x,y+1):
        if i % 2 == 0:
            z.append(i)
    
    return(z)

print(even_numbers(1, 30))
  
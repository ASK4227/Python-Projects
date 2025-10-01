def divisible_by_three(n, y):
    for i in range(n, y):
        if i % 3 == 0:
            print(i)

print(divisible_by_three(9, 100))
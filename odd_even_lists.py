list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

odd_list = [i for i in list1 if i % 2 != 0]

even_list = [x for x in list2 if x % 2 == 0]

print (odd_list + even_list)


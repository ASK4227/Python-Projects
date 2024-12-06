# Python code​​​​​​‌‌​​​‌​​​​‌​​​‌​‌​​‌‌​‌‌‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None

def hexToDec(hexNum):

    lst = list(hexNum)
    total = 0

# checks if the input is correct and in hexNumbers
    for x in lst:
        if x not in hexNumbers.keys():
            return None
    
    
    if len(lst) == 1:
        total = 1 * hexNumbers[lst[0]]
        return total

    if len(lst) == 2:
        total = 16 * hexNumbers[lst[0]] + 1 * hexNumbers[lst[1]]
        return total

    if len(lst) == 3:
        total = 256 * hexNumbers[lst[0]] + 16 * hexNumbers[lst[1]] + 1 * hexNumbers[lst[2]]
        return total

    else:
        return None


        
hexToDec("A6G")

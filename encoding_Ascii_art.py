def encodeString(stringVal):
    lst = []
    prevChar = None
    count = 0
    
    for char in stringVal:
        if char != prevChar:
            if prevChar is not None:  # Only append after the first character is processed
                lst.append((prevChar, count)) 
            count = 1  
            # Reset count for the new character
        else:
            count += 1  # Increase count if the character is the same as the previous one
        prevChar = char
    
    # Append the last character and its count
    if prevChar is not None:
        lst.append((prevChar, count))
    
    return lst
    


        


def decodeString(encodedList):

    ttl = ""
    z = ""

    for tup in encodedList:

        
        z = tup[0] * tup[1]
        ttl = ttl + z

    return ttl

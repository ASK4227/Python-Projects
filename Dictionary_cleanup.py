def file_cleanup():
    print ("Enter a file destination")
    x = input("Enter a file location")
    
    try:

        with open(x, "r") as in_file:
            in_file = in_file.read().strip().split()
            for word in in_file:
                if len(word) < 1:
                    in_file.remove(word)
                
        
        return(len(in_file))
    
    except ValueError:

        return("enter a valid location bro")


dic_cleanup = file_cleanup()

print(dic_cleanup)

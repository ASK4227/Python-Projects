# text function formatter

def text_formatter(first_name, last_name):
    return(" His 1st name is {0} and last name is {1} ".format(first_name, last_name))

first_name = input("enter ur name")
last_name = input("enter ur last name")

print(text_formatter(first_name, last_name))

x = input("enter a word:-")

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

t = ""

if x[0] in vowels:
    x = x + "way"
    print(x)
else:
    y = list(x)

    y +=  y[0]

    y.pop(0)

    t = "".join(y) + "ay"

    print(t)

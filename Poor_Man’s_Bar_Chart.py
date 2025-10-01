import pprint
from collections import defaultdict

y = defaultdict(list)

Sentence = input("Enter a sentence here")

x = ['e','t','a','o','i','n']


for sntnce in Sentence:
    if (sntnce.lower()) in x:
        y[sntnce.lower()].append(sntnce)

pprint.pp(y)

#First is frequency of words overall
    #Done - Implemented in dictionary "d"

#Then frequency of words in a parargaph
    #Split paragraphs by new line characters
    #Create a 2d? list, each spot of the first dimension is a paragraph

#Then attempt to find definitions if any

#Then attempt to cut out most useful part

#Add ability to find proper names like "John" and keep capitalization
    #In Progress - Currently finds all capitalized words
    #Need to add that if capitalized words come back to back with no punctuation between that it is "one word/name"
    #Need to figure out how to seperate a name like "WIRED" which is all caps but not part of the title or first few words

from collections import OrderedDict
from operator import itemgetter
import re

nlf = '\n'

f = open("article.txt", "rb")
text = (f.read()).decode('utf-8')
s = text.split()


paragraphs = []
properNouns = []
lastLetter = ''
slastLetter = ''

sp = []
zzz = 0
ccc = ''

for letter in text:
    sp.append(letter)

    if letter == '\n' and slastLetter == '\n':
        print(sp)
        ccc = ''.join(sp)
        paragraphs.append(ccc)
        sp = []
        zzz = zzz+1

    slastLetter = lastLetter
    lastLetter = letter


for x in paragraphs:
    print(paragraphs, '\n')

#removes special characters and capitalization of each word
for x in range(len(s)):
    s[x] = ''.join(e for e in s[x] if e.isalnum())

    #Adds capitalized words into properNouns list
    if any(z.isupper() for z in s[x]):
        properNouns.append(s[x])
    #Sets all words to lower case as for loop itterates
    s[x] = (s[x]).lower()


#list of just one occurence of values
unique = []
#Empty string for loop
z = ''
#Dictionary for frequency
occurences = {}

for x in range(len(s)):
    c = 0
    z = s[x]
    c = s.count(z)

    if z not in unique:
        unique.append(z)
        occurences[z] = c


unique.sort()
#This line orders the dictionary by value lowest to highest
d = OrderedDict(sorted(occurences.items(), key=itemgetter(1)))
#print(d)

f.close()

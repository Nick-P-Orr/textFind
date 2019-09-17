from collections import OrderedDict
from operator import itemgetter
import re, plotly.graph_objects as go
import plotly.io as pio

nlf = '\n'

f = open("Article3.txt", "rb")
text = (f.read()).decode('utf-8')
s = text.split()

#removes special characters and capitalization of each word
for x in range(len(s)):
    s[x] = ''.join(e for e in s[x] if e.isalnum())

    #Sets all words to lower case as for loop itterates
    s[x] = (s[x]).lower()

#list of just one occurence of values
unique = []
#Empty string for loop
z = ''
#Dictionary for frequency
occurences = {}
numbs = []

for x in range(len(s)):
    c = 0
    z = s[x]
    c = s.count(z)

    if z not in unique:
        unique.append(z)
        occurences[z] = c
        numbs.append(c)

unique.sort()
numbs.sort()

#This line orders the dictionary by value lowest to highest

d = OrderedDict(sorted(occurences.items(), key=itemgetter(1)))
del d[""]

datad = d.items

print(datad())

datak = d.keys

fig = go.Figure(
    #x is position that y is adding a value to
    data=[go.Bar(x=list(range(1, len(numbs)+1)), y=numbs)],
    layout=go.Layout(
        title=go.layout.Title(text="A Bar Chart")
    )
)

fig.show()


f.close()
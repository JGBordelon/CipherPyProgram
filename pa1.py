# Author: Joseph Bordelon
# ULID: c00286756
# Course: CMPS 315
# Assignment: pa1 - Monoalphabetic substitution cipher
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work
from collections import Counter
infile = open ("cipher1.txt", 'r')
data = infile.read()
#print(data)

#freqency analysis
ListCount = Counter(data)
print("Top 5 most common letters: " + str(Counter(data).most_common(5)))

#bigram counts
bicount = Counter([data[i:i+2] for i in range(0, len(data), 3)])
print("Top 5 most common bigrams: " + str(bicount.most_common(5)))

#trigram counts
tricount = Counter([data[i:i+3] for i in range(0, len(data), 3)])
print("Top 5 most common trigrams: " + str(tricount.most_common(5)))

#print("total length of data: " + str(len(data))) #686 letters

#Frequency chart I used - http://norvig.com/mayzner.html

outdata = data
outfile = open('decipher.txt', 'a')
#empty the outfile of the last debug attempt
outfile.truncate(0)

#testing trigrams
#outdata = outdata.replace("gta", "the")
#outdata = outdata.replace("oby", "ing")
#outdata = outdata.replace("tjm", "h  ")
#outdata = outdata.replace("fak", " e ")
#outdata = outdata.replace("tou", "hi ")

#testing bigrams
#outdata = outdata.replace("ob", "in")
#outdata = outdata.replace("tj", "")
#outdata = outdata.replace("ta", "he")
#outdata = outdata.replace("ju", "")
#outdata = outdata.replace("gt", "th")

outdata = outdata.replace('a', 'e') #a=e
outdata = outdata.replace('t', 'h') #t=h
outdata = outdata.replace('g', 't') #g=t
outdata = outdata.replace('o', 'i') #o=i
outdata = outdata.replace('b', 'n') #b=n
outdata = outdata.replace('y', 'g') #y=g


outfile.write(outdata)
outfile.close()
infile.close()
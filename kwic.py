wordlist = open('input.tx', 'r').read().split()
#print(wordlist)

# Next we run a sliding window over the word list to create a list of n-grams. 
# In this case we are going to be using a window of five words, which will give us two words of context on either side of our keyword.

ngrams = [wordlist[i:i+5] for i in range(len(wordlist)-4)]
# We then need to put each n-gram into a dictionary, indexed by the middle word. Since we are using 5-grams,
# and since Python sequences are numbered starting from zero, we want to use 2 for the index.

kwicdict = {}
for n in ngrams:
    if n[2] not in kwicdict:
        kwicdict[n[2]] = [n]
    else:
        kwicdict[n[2]].append(n)

print (str(kwicdict))

# Finally, we will want to do a bit of formatting so that our results are printed in a way that is easy to read.

for key in sorted(kwicdict.keys()):
    for val in kwicdict[key]:
       outstring = ' '.join(val[:2]).rjust(20)
       outstring += ' '
       outstring += ' '.join(str(val[2]).center(len(n[2])+6))
       outstring +=' '
       outstring += ' '.join(val[3:])
       print (outstring)

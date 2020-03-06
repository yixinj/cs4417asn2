#!/usr/bin/env python

# take as input the name of a city and return the number of Starbucks counted in the output file when run in a bash terminal with 'python query.py' used to start the program.
import sys

d = {}
with open('cityInformation', 'rb') as f:
    for line in f:
        line = line.strip()
        word, count = line.split('\t')
        d[word] = count

for query in sys.stdin:
    query = query.strip().upper()
    print d[query]

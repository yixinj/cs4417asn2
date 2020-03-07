#!/usr/bin/env python

# take as input the name of a city and
# return the number of Starbucks counted in the output file
# when run in a bash terminal with 'python query.py' used to start the program.
import sys

for query in sys.stdin:
    # Process query
    query = query.strip().upper()

    # Get results
    with open('part1/cityInformation', 'r') as f:
        for line in f:
            line = line.strip()
            word, count = line.split('\t')
            if query == word:
                print count

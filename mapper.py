#!/usr/bin/env python
import sys
import csv

# with open("starbucks-locations-sort.csv") as f:
with sys.stdin as f:
    for line in csv.reader(
            f,
            quotechar='"',
            delimiter=',',
            quoting=csv.QUOTE_ALL,
            skipinitialspace=True):
        # Strip whitespace and change to upper to prevent case mismatch
        city = line[9].strip().upper()
        print '%s\t%s' % (city, 1)


# for line in sys.stdin:
#     line = line.strip()
#     words = line.split(',')  # Separate by comma not space

#     # City is at index 9 in each line 9 (and strip whitespace of city)
#     city = words[9].strip()
#     # Print tab-delimited results
#     print '%s\t%s' % (city, 1)

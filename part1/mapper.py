#!/usr/bin/env python
import sys
import csv

for line in csv.reader(sys.stdin):
    # line[9] is city
    city = line[9].strip().upper()
    print '%s\t%s' % (city, 1)

# with open('starbucks-locations-sort.csv') as f:
#     for line in csv.reader(f):
#         city = line[9].strip().upper()
#         print '%s\t%s' % (city, 1)

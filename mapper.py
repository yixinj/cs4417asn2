#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split(',')  # Separate by comma not space

    # City is at index 9 in each line 9 (and strip whitespace of city)
    city = words[9].strip()
    # Print tab-delimited results
    print('%s\t%s' % (city, 1))

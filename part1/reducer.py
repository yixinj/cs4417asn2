#!/usr/bin/env python
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    # Convert count to an int
    try:
        count = int(count)
    except ValueError:
        continue

    # Add the counts (works because Hadoop sorts entries)
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Write result to stdout
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# Output last word if needed
if current_word == word:
    print('%s\t%s' % (current_word, current_count))


# with open('output.txt', 'rb') as f:

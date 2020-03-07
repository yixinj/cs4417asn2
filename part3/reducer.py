#!/usr/bin/env python
import sys

current_genre = None
current_movies = 0
genre = None

for line in sys.stdin:
    # stdin: each line contains a genre (UPPER), tab, and movie name
    line = line.strip()
    genre, movie_name = line.split('\t', 1)

    # Add the counts (works because Hadoop sorts entries)
    if current_genre == genre:
        current_movies += movie_name + "\t"
    else:
        if current_genre:
            # Write result to stdout
            print('%s\t%s' % (current_genre, current_movies))
        current_movies = movie_name + "\t"
        current_genre = genre

# Output last word if needed
if current_genre == genre:
    print('%s\t%s' % (current_genre, current_movies.strip()))
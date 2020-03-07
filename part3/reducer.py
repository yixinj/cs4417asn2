#!/usr/bin/env python
import sys

current_genre = None
current_movies = 0
genre = None

for line in sys.stdin:
    # stdin: each line contains a genre (UPPER), tab, and movie name
    line = line.strip()
    genre, movie_name = line.split('\t', 1)

    if current_genre == genre:
        current_movies += movie_name + "|"
    else:
        if current_genre:
            # Write result to stdout
            print('%s\t%s' % (current_genre, current_movies))
        current_movies = movie_name + "|"
        current_genre = genre

# Output last word if needed
if current_genre == genre:
    print('%s\t%s' % (current_genre, current_movies.strip()))

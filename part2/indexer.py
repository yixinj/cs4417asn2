# Read CSV
# Convert to an index form
# Movie name -> all lines that contain this

# import sys

d = {}

with open('./movies.dat', 'r') as f:
    for line in f:
        # Processes each line of the file
        movie_id, movie_name, movie_genres = line.split('::', 2)

        # Strip blank spaces
        movie_id = movie_id.strip()
        movie_name = movie_name.strip()
        movie_genres = movie_genres.strip()

        # Processes the genres
        movie_genres = movie_genres.split('|')
        for genre in movie_genres:
            # If genre is blank, replace it with 'None'
            if genre == '':
                genre = 'None'
            # If genre is not yet in dictionary, add it
            if genre not in d:
                d[genre] = set()
            d[genre].add(movie_name)

print(d)

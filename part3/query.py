# Take query
for 
# Get results
with open('part3/movieInformation', 'r') as f:
    for line in f:
        line = line.strip()
        genre, movies = line.split('\t')
        movies = movies.split('|')


# lines = ['None and Documentary']

# for line in lines:
#     line = line.upper()
#     words = line.split()

#     # If the query has no operator, print all movies with that genre
#     if len(words) == 1:
#         genre = words[0]
#         print(d[genre])
#     # Otherwise ...
#     else:
#         genre_first, operator, genre_second = words
#         if operator == 'AND':
#             # AND is the intersection of the sets
#             print(d[genre_first].intersection(d[genre_second]))
#         if operator == 'OR':
#             # OR is the union of the sets
#             print(d[genre_first].union(d[genre_second]))

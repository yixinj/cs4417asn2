import sys

for query in sys.stdin:
    # Take query and process it
    query = query.strip().upper().split()

    # If length of query is 1 (so 1 search term)
    if len(query) == 1:
        genre_first = query[0]  # genre1 is genre to search for
        with open('part3/movieInformation', 'r') as f:
            for line in f:
                line = line.strip()
                genre, movies = line.split('\t')
                if genre_first == genre:
                    movies = movies.split('|')
                    print(movies)

    # Otherwise ...
    else:
        genre_first, operator, genre_second = query
        first_set = second_set = None

        with open('part3/movieInformation', 'r') as f:
            for line in f:
                line = line.strip()
                genre, movies = line.split('\t')
                if genre_first == genre:
                    movies = movies.split('|')
                    first_set = set(movies)
                if genre_second == genre:
                    movies = movies.split('|')
                    second_set = set(movies)

        # Output set that fits the operator
        if operator == 'AND':
            # AND is the intersection of the sets
            print(first_set.intersection(second_set))

        if operator == 'OR':
            # OR is the union of the sets
            print(first_set.union(second_set))

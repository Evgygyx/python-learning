fav_movies = ["Dune", "Harry Potter", "The French Dispatch"]
print(fav_movies[0])
print(len(fav_movies))
fav_movies.append("Iron Man")
print(len(fav_movies))
fav_movies.insert(1, "Bathman")
print(fav_movies)
del(fav_movies[2])
print(fav_movies)


del(fav_movies[0:2])
del(fav_movies[-1])
print(fav_movies)
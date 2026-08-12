class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating

    def show_info(self):
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Rating: {self.rating}")

    def is_high_rating(self):
        if self.rating >= 9.0:
            return True
        else:
            return False

#1
movies = []
movies.append(Movie("Interstellar",2014,9.1))
movies.append(Movie("Inception",2010,8.8))
movies.append(Movie("Parasite",2019,8.6))
movies.append(Movie("The Dark Knight",2008,9.0))

#2
for movie in movies:
    movie.show_info()
    print()

#3
print("High Rated Movies")
for movie in movies:
    if movie.is_high_rating():
        print(f"{movie.title}")
print()

#4
class StreamingMovie(Movie):
    def __init__(self, title, year, rating, platform):
        super().__init__(title, year, rating)
        self.platform = platform

    def show_info(self):
        super().show_info()
        print(f"Platform: {self.platform}")

#5
movies.append(StreamingMovie("Dune",2021,8.5,"Netflix"))
movies.append(StreamingMovie("Oppenheimer",2023,8.9,"Watcha"))
for movie in movies:
    movie.show_info()
    print()

#6
top_rating_movie = movies[0]
for i in range(1,len(movies)):
    if movies[i].rating > top_rating_movie.rating:
        top_rating_movie = movies[i]
print("Top Movie")
print(f"Title: {top_rating_movie.title}")
print(f"Rating: {top_rating_movie.rating}")
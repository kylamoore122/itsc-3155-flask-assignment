# TODO: Feature 1
from src.repositories.movie_repository import MovieRepository
from src.models.movie import Movie

def test_get_all_movies():
    movie_repo = MovieRepository()
    movie1 = Movie("Last of the Mohicans", "Michael Mann", 8)
    movie2 = Movie("No Country for Old Men", "Joel and Ethan Coen", 8)
    movie3 = Movie("Dunghole the Movie", "Micheal Bay", 7) #this one is an inside joke
    movie4 = Movie("Dunkirk", "Christopher Nolan", 8)
    movie_repo._db.append(movie1)
    movie_repo._db.append(movie2)
    movie_repo._db.append(movie3)
    movie_repo._db.append(movie4)
    movie_list = movie_repo.get_all_movies()
    assert movie_list[0] == movie1
    assert movie_list[1] == movie2
    assert movie_list[2] == movie3
    assert movie_list[3] == movie4
    
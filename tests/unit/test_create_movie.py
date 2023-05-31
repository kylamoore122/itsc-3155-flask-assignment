# TODO: Feature 2
from src.repositories.movie_repository import MovieRepository
from src.models.movie import Movie

def test_create_movie():
    movie_repo = MovieRepository()
    movie = movie_repo.create_movie("It Follows", "David Robert Mitchell", 7)
    assert type(movie) == Movie
    assert movie.title == "It Follows"
    assert movie.rating == 7
    assert movie.director == "David Robert Mitchell"
    movie = movie_repo.create_movie("The Babadook", "Jennifer Kent", 7)
    assert type(movie) == Movie
    assert movie.title == "The Babadook"
    assert movie.rating == 7
    assert movie.director == "Jennifer Kent"
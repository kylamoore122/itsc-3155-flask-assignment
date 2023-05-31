# TODO: Feature 3
from src.repositories.movie_repository import MovieRepository
from src.models.movie import Movie

def test_get_movie_by_title():
    movie_repo = MovieRepository()
    movie1 = Movie("Last of the Mohicans", "Michael Mann", 8)
    movie2 = Movie("No Country for Old Men", "Joel and Ethan Coen", 8)
    movie3 = Movie("Armageddon", "Michael Bay", 7)
    movie4 = Movie("Toy Story 2", "John Lasseter", 8)
    movie_repo._db.append(movie1)
    movie_repo._db.append(movie2)
    movie_repo._db.append(movie3)
    movie_repo._db.append(movie4)
    assert movie_repo.get_movie_by_title('Toy Story 2') == movie4
    assert movie_repo.get_movie_by_title('No Country for Old Men') == movie2
    assert movie_repo.get_movie_by_title('Armageddon') == movie3
    assert movie_repo.get_movie_by_title('Last of the Mohicans') == movie1
    assert movie_repo.get_movie_by_title('Toy Story') == None
    assert movie_repo.get_movie_by_title('Kung Fu Panda') == None


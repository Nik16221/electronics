from unittest.mock import MagicMock
import pytest
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


# Создаем фикстуру с моком для  MovieDAO
@pytest.fixture
def movie_dao():
    movie_init = MovieDAO(None)

    movie_1 = Movie(
        id=1,
        title="title_1",
        description="test",
        trailer="test",
        year=2022,
        rating=4,
        genre_id=1,
        genre=1,
        director_id=1,
        director=1
    )
    movie_2 = Movie(
        id=2,
        title="title_2",
        description="test2",
        trailer="test2",
        year=2021,
        rating=5,
        genre_id=2,
        genre=2,
        director_id=2,
        director=2
    )

    movie_init.get_one = MagicMock(return_value=movie_1)
    movie_init.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_init.create = MagicMock(return_value=movie_1)
    movie_init.delete = MagicMock()
    movie_init.update = MagicMock()

    return movie_init


# Пишем класс с тестами для MovieService
class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        assert self.movie_service.get_one(1).title == "title_1"
        assert self.movie_service.get_one(1) is not None
        assert self.movie_service.get_one(1).id is not None

    def test_get_all(self):
        assert len(self.movie_service.get_all()) == 2
        assert len(self.movie_service.get_all()) > 0

    def test_create(self):
        data = {
            "id": 1,
            "title": "title_1",
            "description": "test",
            "trailer": "test",
            "year": 2022,
            "rating": 4,
            "genre_id": 1,
            "genre": 1,
            "director_id": 1,
            "director": 1
        }
        assert self.movie_service.create(data).title == data.get("title")

    def test_update(self):
        data = {
            "id": 1,
            "title": "title_1",
            "description": "test",
            "trailer": "test",
            "year": 2022,
            "rating": 4,
            "genre_id": 1,
            "genre": 1,
            "director_id": 1,
            "director": 1
        }

        self.movie_service.update(data)

    def test_delete(self):
        self.movie_service.delete(1)

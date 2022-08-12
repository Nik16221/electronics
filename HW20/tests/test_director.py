from unittest.mock import MagicMock
import pytest
from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


# Создаем фикстуру с моком для DirectorDAO
@pytest.fixture
def director_dao():
    director_init = DirectorDAO(None)

    director_1 = Director(id=1, name="user_1")
    director_2 = Director(id=2, name="user_2")

    director_init.get_one = MagicMock(return_value=director_1)
    director_init.get_all = MagicMock(return_value=[director_1, director_2])
    director_init.create = MagicMock(return_value=director_1)
    director_init.delete = MagicMock()
    director_init.update = MagicMock()

    return director_init


# Пишем класс с тестами для DirectorService
class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        assert self.director_service.get_one(1).name == "user_1"
        assert self.director_service.get_one(1) is not None
        assert self.director_service.get_one(1).id is not None

    def test_get_all(self):
        assert len(self.director_service.get_all()) == 2
        assert len(self.director_service.get_all()) > 0

    def test_create(self):
        data = {
            "name": "user_1",
            "id": 1
        }
        assert self.director_service.create(data).name == data.get("name")

    def test_update(self):
        data = {
            "name": "user_1",
            "id": 1
        }
        self.director_service.update(data)

    def test_delete(self):
        self.director_service.delete(1)

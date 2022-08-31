from typing import Dict

from abstractstorage import AbstractStorage
from exeptions import NotEnoughSpace, NotEnoughProduct


class BaseStorage(AbstractStorage):
    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int):
        if self.get_free_space() < amount:
            raise NotEnoughSpace

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def get_free_space(self):
        busy_place = 0  # занято места
        for value in self.__items.values():
            busy_place += value
        return self.__capacity - busy_place

    def remove(self, name: str, amount: int):
        if name not in self.__items or self.__items[name] < amount:
            raise NotEnoughProduct
        self.__items[name] -= amount

        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)

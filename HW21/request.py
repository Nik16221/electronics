from typing import Dict

from abstractstorage import AbstractStorage
from exeptions import InvalidRequest, InvalidStorageName


class Request:
    def __init__(self, request: str, storages: Dict[str, AbstractStorage]):

        split_request = request.lower().split(' ')
        if len(split_request) != 7:
            raise InvalidRequest

        self.amount = int(split_request[1])
        self.product = split_request[2]
        self.departure = split_request[4]
        self.destination = split_request[6]

        if self.departure not in storages or self.destination not in storages:
            raise InvalidStorageName


    
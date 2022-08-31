class BaseError(Exception):
    message = "Что-то пошло не так"


class NotEnoughSpace(BaseError):
    message = "Недостаточно места на складе"


class NotEnoughProduct(BaseError):
    message = "Недостаточно товара на складе"


class TooManyDifferentProducts(BaseError):
    message = "Слишком много разных товаров"


class InvalidRequest(BaseError):
    message = "Неверный запрос"


class InvalidStorageName(BaseError):
    message = "Выбран неверный путь"

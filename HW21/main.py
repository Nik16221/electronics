from courier import Courier
from request import Request
from exeptions import BaseError
from shop import Shop
from store import Store

store = Store(items={
    "печенька": 10,
    "собачка": 10,
    "коробка": 10})

shop = Shop(items={
    "печенька": 1,
    "собачка": 1,
    "коробка": 2})

storages = {
    "магазин": shop,
    "склад": store}


def main():
    print("Добрый день!")
    while True:
        for storage_name in storages:
            print(f"Сейчас в {storage_name}:\n{storages[storage_name].get_items()}")

        user_input = input(
            'Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Для выхода введите "стоп" или "stop":\n'
        )

        if user_input.lower() in ('stop', 'стоп'):
            break
        try:
            request = Request(request=user_input, storages=storages)
        except BaseError as e:
            print(e.message)
            continue

        courier = Courier(
            request=request,
            storages=storages
        )

        try:
            courier.move()
        except BaseError as e:
            print(e.message)
            courier.cancel()


if __name__ == "__main__":
    main()

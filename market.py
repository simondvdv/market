def price_list_view(price_list):  # Список товаров в магазине
    print('\nСписок товаров:\n--------------------')
    counter = 0
    for key, value in price_list.items():
        counter += 1
        print(f'{counter}. {key} - {value}р.')
        print('--------------------')


def cart_list_view(price_list):  # Список товаров в корзине
    print('\nСписок товаров:\n--------------------')
    counter = 0
    for key, value in price_list.items():
        if value == 0:
            continue
        counter += 1
        print(f'{counter}. {key} x {value} - {value * price_dict[key]}р')
        print('--------------------')


def shopping_cart_add():  # Ввод товара
    product = input('\nВведите название товара:\n').title()
    return product


price_dict = {'Карандаш': 50, 'Ручка': 75.5, 'Пачка бумаги': 389.9, 'Линейка': 25.85}
product_cart = {'Карандаш': 0, 'Ручка': 0, 'Пачка бумаги': 0, 'Линейка': 0}
command = ''
while command != 'end':

    task = input('Введите команду:\n').lower()
    match task:
        case 'add':  # Не смог это поместить в фукнцию, оставил в теле программы
            while True:
                try:
                    key_ = shopping_cart_add()
                    product_cart[key_] += 1
                    add_flag = input('Добавить ещё товар?:\nДа - добавить товар\n "любая команда" - вернутся в меню\n"')
                    if add_flag.lower() == 'да':
                        continue
                    else:
                        break
                except KeyError:
                    print('Такого товара нет, попробуйте ещё раз')
                    continue
        case 'del':
            product_cart.clear()
            print('Корзина очищена')
        case 'view':
            price_list_view(price_dict)
        case 'remove':
            print('remove')
        case 'cart':
            cart_list_view(product_cart)
        case 'end':
            break
        case _:
            print('Такой команды нет')

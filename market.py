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


def shopping_cart_add(cart_dict):  # Ввод товара
    while True:
        product = input('\nВведите название товара:\n').title()
        try:
            key_ = product
            cart_dict[key_] += 1
            add_flag = input('Добавить ещё товар?:\nДа - добавить товар\n "любая команда" - вернутся в меню\n"')
            if add_flag.lower() == 'да':
                continue
            else:
                break
        except KeyError:
            print('Такого товара нет, попробуйте ещё раз')
            continue


def galya_otmena(cart_dict):
    try:
        del_key = input('Введите название товара, который необходимо удалить\n').title()
        if cart_dict[del_key] > 0:
            cart_dict[del_key] -= 1
        else:
            print('Такого товара нет в корзине')
    except KeyError:
        print('Такого товара нет в нашем магазине')


def product_discount(cart_dict):
    if cart_summator(cart_dict) >= 5000:
        print(f'Стоимость вашей покупки {cart_summator(cart_dict)}'
              f'с учетом скидки {round(cart_summator(cart_dict) * 0.9, 2)}')
    else:
        print(f'Стоимость вашей покупки {cart_summator(cart_dict)} '
              f'до 10% скидки не хватает {5000 - cart_summator(cart_dict)}')


def shop_helper():
    print('Добро пожаловать в питон-магазин, "Рога и копыта"!\nДля работы введите одну из команд:\nadd - добавить '
          'товар\ndel - очистить корзину\nview - посмотреть весь товар в магазине\nremove - удалить одну из позиций в '
          'корзине\ncart - посмотреть все товары в корзине\nhelp - вывести ещё раз это сообщение с подсказками\nend - '
          'закончить работу с магазином напечатать чек.')


def cart_summator(cart_dict):
    summator = 0
    for key, value in cart_dict.items():
        summator += price_dict[key] * cart_dict[key]
    return summator


def check_print(cart_dict):
    print('\nСписок товаров:\n--------------------')
    counter = 0
    for key, value in cart_dict.items():
        if value == 0:
            continue
        counter += 1
        print(f'{counter}. {key} x {value} - {value * price_dict[key]}р')
        print('--------------------')
    if cart_summator(cart_dict) >= 5000:
        print(f'Итог: {round(cart_summator(cart_dict), 2)}')
    else:
        print(f'Итог: {cart_summator(cart_dict)}')


price_dict = {'Карандаш': 500, 'Ручка': 775.5, 'Пачка Бумаги': 3389.9, 'Линейка': 250.85}
product_cart = {'Карандаш': 0, 'Ручка': 0, 'Пачка Бумаги': 0, 'Линейка': 0}
command = ''
shop_helper()
while command != 'end':
    task = input('Введите команду:\n').lower()
    match task:
        case 'add':
            shopping_cart_add(product_cart)
        case 'del':
            product_cart.clear()
            print('Корзина очищена')
        case 'view':
            price_list_view(price_dict)
        case 'remove':
            galya_otmena(product_cart)
        case 'cart':
            cart_list_view(product_cart)
        case 'end':
            product_discount(product_cart)
            continue_question = input('Продолжить покупки? да/нет\n')
            if continue_question.lower() == 'да':
                continue
            check_print(product_cart)
            break
        case 'help':
            shop_helper()
        case _:
            print('Такой команды нет')


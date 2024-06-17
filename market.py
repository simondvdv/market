def price_list_view(price_list):
    print('\nСписок товаров:\n--------------------')
    counter = 0
    for key, value in price_list.items():
        counter += 1
        print(f'{counter}. {key} - {value}р.')
        print('--------------------')


def cart_list_view(price_list):
    print('\nСписок товаров:\n--------------------')
    counter = 0
    for key, value in price_list.items():
        counter += 1
        print(f'{counter}. {key} - {value}р.')
        print('--------------------')

def shopping_cart_add():
    product = input('\nВведите название товара:\n').title()
    return product


def shop_request_check(shop_request):
    pass


def did_i_nave_this(key, product):
    if key in product.keys():
        return 1
    else:
        return 0


price_dict = {'Карандаш': 50, 'Ручка': 75.5, 'Пачка бумаги': 389.9, 'Линейка': 25.85}
product_cart = {'Карандаш': 0, 'Ручка': 0, 'Пачка бумаги': 0, 'Линейка': 0}
command = ''
while command != 'end':

    task = input('Введите команду:\n').lower()
    match task:
        case 'add':
            while True:
                try:
                    key_ = shopping_cart_add()
                    product_cart[key_] += did_i_nave_this(key_, product_cart)
                    break
                except KeyError:
                    print('Такого товара нет, попробуйте ещё раз')
                    continue
        case 'del':
            print('del')
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

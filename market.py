def cash_receipt_maker_functional():
    task = input('Введите команду:\n').lower()
    match task:
        case 'add':
            shopping_cart_add()
        case 'del':
            print('del')
        case 'view':
            return price_list_view(price_dict)
        case 'remove':
            print('remove')
        case 'cart':
            pass
        case _:
            print('Такой команды нет')


def price_list_view(price_list):
    print('\nСписок товаров:\n--------------------')
    counter = 0
    for key, value in price_list.items():
        counter += 1
        print(f'{counter}. {key} - {value}р.')
    print('--------------------')


def shopping_cart_add():
    pass

def shop_request_check(shop_request):
    pass


price_dict = {'Карандаш': 50, 'Ручка': 75.5, 'Пачка бумаги': 389.9, 'Линейка': 25.85}


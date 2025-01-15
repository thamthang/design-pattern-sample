def pre_order_price(origin_price):
    return origin_price * 0.8

def promotion_price(origin_price):
    return origin_price * 0.9 if origin_price <= 200 else origin_price - 30

def default_price(origin_price):
    return origin_price

def day_price(origin_price):
    return origin_price * 0.7

price_strategy = {
    'pre_order': pre_order_price,
    'promotion': promotion_price,
    'default': default_price,
    'day': day_price
}

def get_price(price, strategy='default'):
    return price_strategy.get(strategy, default_price)(price)

if __name__ == '__main__':
    assert get_price(100, 'pre_order') == 80
    assert get_price(100, 'promotion') == 90
    assert get_price(100, 'default') == 100
    assert get_price(100, 'day') == 70
    assert get_price(100) == 100

    print('All test cases pass')
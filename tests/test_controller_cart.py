from tests.setup import setup_database
from MyCart.controller import CartController

mock_product = {
    'name': 'The Secret',
    'price': 1000.0,
    'category': 'Books'
}

def test_add_product(setup_database):
    cart_controller = CartController()
    message = cart_controller.add(
        mock_product['name'])
    assert message == 'Product {0} added to cart!'.format(mock_product['name'])

def test_remove(setup_database):
    cart_controller = CartController()
    message = cart_controller.remove(
        mock_product['name'])
    assert message == 'Product {0} removed from cart!'.format(mock_product['name'])

# def test_fail_remove(setup_database):
#     cart_controller = CartController()
#     message = cart_controller.remove(
#         mock_product['name'])
#     assert message == 'Product {0} not available'.format(mock_product['name'])

from tests.setup import setup_database
from product.controller import ProductController

mock_product = {
    'name': 'i10',
    'price': 10000.0,
    'category': 'Car'
}

def test_create(setup_database):
    product_controller = ProductController()
    message = product_controller.create(
        mock_product['name'], 
        mock_product['category'],
        mock_product['price'])
    assert message == 'Product {0} created!'.format(mock_product['name'])

def test_remove(setup_database):
    product_controller = ProductController()
    message = product_controller.remove(
        mock_product['name'])
    assert message == 'Product {0} removed!'.format(mock_product['name'])

def test_get_all_product(setup_database):
    product_controller = ProductController()
    data = product_controller.get_all_product()
    assert len(data) == 10

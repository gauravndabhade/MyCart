from tests.setup import setup_database
from category.controller import CategoryController

mock_category = {
    'name': 'Furniture',
}
mock_category_2 = {
    'name': 'Tables',
}



def test_create(setup_database):
    category_controller = CategoryController()
    message = category_controller.create(
        mock_category['name'])
    assert message == 'Category {0} created!'.format(mock_category['name'])


def test_remove(setup_database):
    category_controller = CategoryController()
    message = category_controller.remove(
        mock_category['name'])
    assert message == 'Category {0} removed!'.format(mock_category['name'])

def test_get(setup_database):
    category_controller = CategoryController()
    category = category_controller.get(name="Books")
    assert category.name == 'Books'


# def test_fail_get(setup_database):
#     category_controller = CategoryController()
#     message = category_controller.get(name=mock_category_2['name'])
#     assert message == '{0} doesn\'t exists'.format(mock_category_2['name'])

# def test_fail_create(setup_database):
#     category_controller = CategoryController()
#     message = category_controller.create(
#         mock_category['name'])
#     assert message == 'Category {0} already exist!'.format(mock_category['name'])
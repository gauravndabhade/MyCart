# Third party imports
import pytest
import config
from peewee import SqliteDatabase
from models import Product, User, Category, Cart

MODELS = (User, Category, Cart, Product)
db = SqliteDatabase(config.TEST_DATABASE)

@pytest.fixture(scope='module', autouse=True)
def setup_database():
    # print('Initialized test database')
    db.connect()
    db.create_tables(MODELS)

    # Default test data
    user = User(username='Foo', password='12345678',
                        is_admin=True)
    user.save()

    category = Category.create(name='Car', user=user)
    category.save()

    product = Product.create(name='Nano', user=user,
                                price=10000.0, category=category)
    product.save()
    
    product = Product.create(name='Alto', user=user,
                                price=10000.0, category=category)
    product.save()
    
    product = Product.create(name='Swift', user=user,
                                price=10000.0, category=category)
    product.save()

    category = Category.create(name='Mobile', user=user)
    category.save()
    
    product = Product.create(name='Realme', user=user,
                                price=10000.0, category=category)
    product.save()
    
    product = Product.create(name='OnePlus', user=user,
                                price=10000.0, category=category)
    product.save()
    
    product = Product.create(name='Mi', user=user,
                                price=10000.0, category=category)
    product.save()

    category = Category.create(name='Books', user=user)
    category.save()

    product = Product.create(name='The Alchemist', user=user,
                                price=10000.0, category=category)
    product.save()
    
    product = Product.create(name='The Secret', user=user,
                                price=10000.0, category=category)
    product.save()

    category = Category.create(name='Watch', user=user)
    category.save()
    
    product = Product.create(name='Titan', user=user,
                                price=10000.0, category=category)
    product.save()
    
    product = Product.create(name='Casio', user=user,
                                price=10000.0, category=category)
    product.save()

    yield db

    db.drop_tables(MODELS)
    db.close()
    # print('\nDropped test database')
# import click
import peewee

from models import Product
from user import user_session
from category import category_controller


def get_all_product():
    try:
        data = [[p.name, p.category.name, p.price]
                for p in Product.select()]
            
        return data
    except peewee.DoesNotExist:
        return None


def create(name, category, price):

    user = user_session.current_user()
    category = category_controller.get(category)
    product = Product.create(name=name, user=user,
                             price=price, category=category)
    product.save()

    return f'Product {product.name} created!'

def remove(name):
    product = Product.get(Product.name == name)
    product.delete_instance()
    return f'Product {product.name} removed!'
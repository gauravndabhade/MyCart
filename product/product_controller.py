# import click
import peewee

from models import Product
from user import user_session
from category import category_controller


# def display(product):
#     click.echo(click.style(product.name, fg='cyan'))


def all_products():
    return Product.select()


def create(name, category, price):

    user = user_session.current_user()
    category = category_controller.get(category)
    product = Product.create(name=name, user=user,
                             price=price, category=category)
    product.save()

    return f'Product {product.name} created successfully!'

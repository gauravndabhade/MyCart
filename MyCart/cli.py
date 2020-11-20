import os
import click
from tabulate import tabulate
from MyCart.controller import CartController
from category.controller import CategoryController
from product.controller import ProductController
from user.session import UserSession
import config
from models import db, Product, User, Category, Cart
from MyCart.utils import show_welcome, show_bills

MODELS = (User, Category, Cart, Product)
cart = CartController()
user_session = UserSession()
product_controller = ProductController()


@click.group()
@click.version_option("1.0.0")
def main():
    """MyCart, An E-commerce cli application"""
    show_welcome()

    
@main.command()
def add_item():
    """Add new product into cart"""
    click.echo("Creating new product")
    name = click.prompt('Please enter product name')
    click.echo(cart.add(name))


@main.command()
def remove_item():
    """Remove product from cart"""
    click.echo("Remove product")
    name = click.prompt('Please enter product name')
    click.echo(cart.remove(name))

@main.command()
def bill():
    """Create bill for your cart items"""
    show_bills()

@main.command()
def initdb():
    """Initialize database"""
    db.connect()
    db.create_tables(MODELS)
    click.echo('Initialized the database')


@main.command()
def dropdb():
    """Clear/Delete database"""
    db.drop_tables(MODELS)
    db.close()
    click.echo('Dropped the database')
    if os.path.isfile(config.USER_SECRET_FILE):
        os.remove(config.USER_SECRET_FILE)


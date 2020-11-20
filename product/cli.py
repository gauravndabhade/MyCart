import click
from product.controller import ProductController 
from category.controller import CategoryController

product_controller = ProductController()
category_controller = CategoryController()
@click.group()
def product():
    """Get all products from your cart"""
    pass


@ product.command()
def create():
    """Create new product"""
    categories = category_controller.all()

    if categories:
        click.echo("Creating new product")
        name = click.prompt('Enter product name')
        price = click.prompt('Enter price')
        category = click.prompt('Choose a category from list:',
                                type=click.Choice(categories))
        click.echo(product_controller.create(name, category, price))
    else:
        click.echo('Category list is empty. Add new categories...')

@ product.command()
def remove():
    """Remove product"""
    name = click.prompt('Enter product name')
    click.echo(product_controller.remove(name))

    

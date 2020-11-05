import click
from product import product_controller
from category import category_controller


@click.group()
def product():
    """Get all products from your cart"""
    pass


@ product.command()
@ click.argument('q', required=False)
def create(**kwargs):
    """Create new product"""
    click.echo("Creating new product")
    name = click.prompt('Please enter product name')
    price = click.prompt('Enter price')

    categories = category_controller.all()
    category = click.prompt('Choose a category from list:',
                            type=click.Choice(categories))
    click.echo(product_controller.create(name, category, price))


@ product.command()
@ click.argument('q', required=False)
def remove(**kwargs):
    """Remove product"""
    click.echo(kwargs)
    pass

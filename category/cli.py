import click
from category.controller import CategoryController 


@click.group()
def category():
    """Get all category from your cart"""
    pass


@category.command()
def create():
    """Create new category"""
    name = click.prompt('Enter category name')
    click.echo(CategoryController().create(name))


@category.command()
def remove():
    """Remove category"""
    name = click.prompt('Enter category name')
    click.echo(CategoryController().remove(name))
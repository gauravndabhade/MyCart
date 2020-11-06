import click
from category import category_controller


@click.group()
def category():
    """Get all category from your cart"""
    pass

# @ main.command()
# @ click.argument('q', required=False)
# def category(**kwargs):
#     click.echo(kwargs)
#     pass


@category.command()
def create(**kwargs):
    """Create new category"""
    name = click.prompt('Enter category name')
    click.echo(category_controller.create(name))


@category.command()
def remove(**kwargs):
    """Remove category"""
    click.echo(kwargs)
    pass

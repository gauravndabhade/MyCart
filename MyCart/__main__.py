import sys
import click


# Base
@click.group()
@click.version_option("1.0.0")
def main():
    """A Product Search and MyCart CLI"""
    click.echo(click.style('Signin as: Gaurav', bg='blue', fg='white'))
    pass


@main.command()
def status(**kwargs):
    """Get your cart status"""
    click.echo("Get your cart status!")
    pass

# User
@main.command()
def user_create(**kwargs):
    """Creating new user"""
    click.echo("Creating new user!")
    pass

@main.command()
def user_login(**kwargs):
    """User login"""
    click.echo("User login!")
    pass

@main.command()
def user_logout(**kwargs):
    """User logout"""
    click.echo("User logout!")
    pass

# Category
@main.command()
@click.argument('q', required=False)
def category(**kwargs):
    """Get all category from your cart"""
    click.echo(kwargs)
    pass
    
@main.command()
@click.argument('q', required=False)
def category_create(**kwargs):
    """Create new category"""
    click.echo(kwargs)
    pass

@main.command()
@click.argument('q', required=False)
def category_remove(**kwargs):
    """Remove category"""
    click.echo(kwargs)
    pass

# Products
@main.command()
@click.argument('q', required=False)
def products(**kwargs):
    """Get all products from your cart"""
    click.echo(kwargs)
    pass
    
@main.command()
@click.argument('q', required=False)
def product_create(**kwargs):
    """Create new product"""
    click.echo(kwargs)
    pass

@main.command()
@click.argument('q', required=False)
def product_remove(**kwargs):
    """Remove product"""
    click.echo(kwargs)
    pass

# Billing
@main.command()
@click.argument('q', required=False)
def bill(**kwargs):
    """Genrate bill for cart items"""
    click.echo(kwargs)
    pass

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("CVE")
    main()
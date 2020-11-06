import sys
import os
import click
from category.category_cli import category
from models import db, Product, User, Category, Cart
from product.product_cli import product
from tabulate import tabulate
from user import user_controller, user_session
from user.user_cli import user

from MyCart import cart_controller
from product import product_controller
from category import category_controller

MODELS = (User, Category, Cart, Product)
USER_SECRET_FILE = '.current_user.dat'

def add_admin(is_admin):
    if is_admin:
        return click.style(' [ADMIN]', fg='green')
    else:
        return click.style(' [CUSTOMER]', fg='green')

@click.group()
@click.version_option("1.0.0")
def main():
    """A Product Search and MyCart CLI"""
    username, is_admin = user_session.read_current_user()

    click.echo()
    click.echo()
    if username:
        click.echo('MyCart \t\t\t\t\t\t\t\t\t\t Login as: ' + click.style(username,
                                                                            fg='cyan') + add_admin(is_admin))
        click.echo(
                "----------------------------------------------------------------------------------------------------------------")
        # Categories
        click.echo(click.style('Categories', fg='cyan'))
        categories = category_controller.get_all_categories()
        if categories:
            click.echo(tabulate(categories, headers=[
                'Name'], tablefmt='pretty'))
        else:
            click.echo('Categories not found')

        # All products
        click.echo(click.style('Products', fg='cyan'))
        products = product_controller.get_all_product()
        if products:
            click.echo(tabulate(products, headers=[
                'Name', 'Category', 'Price'], tablefmt='pretty'))
        else:
            click.echo('Products not found')

        # Cart status
        # click.echo(click.style('Cart', fg='cyan'))
        # cart_products = cart_controller.get_cart_products(username)
        # click.echo(cart_products)
        # if cart_products:
        #     click.echo(tabulate(cart_products, headers=[
        #         'Name', 'Category', 'Price'], tablefmt='pretty'))

        # else:
        #     click.echo('Cart is empty. Add Products in Cart')
        
        click.echo(
                "----------------------------------------------------------------------------------------------------------------")
    else:
        click.echo('MyCart')
        click.echo(
            "----------------------------------------------------------------------------------------------------------------")

        click.echo(click.style(
            'User login or Create new account to MyCart', fg='yellow'))

@main.command()
def add_item():
    """Create new product"""
    click.echo("Creating new product")
    name = click.prompt('Please enter product name')
    click.echo(cart_controller.add(name))


@main.command()
def remove_item():
    """Remove product"""
    
@main.command()
def bill():
    """Create bill for your cart items"""
    username, _ = user_session.read_current_user()
    if username:
        cart_data = cart_controller.get_cart_products(username)
        if cart_data:
            total_amount = cart_controller.sum_price(cart_data, 2) # 2 -> price coloumn index
            discount_amount, _ = cart_controller.get_discount(total_amount)

            click.echo(click.style(' \tTotal : \t', fg='cyan') +
                            str(total_amount))
            click.echo(click.style(' \tDiscount :', fg='cyan') +
                    '\t' + str(discount_amount))
            click.echo(
                "\t\t\t--------")
            click.echo('\t\t\t' + str(total_amount - discount_amount))
    else:
        click.echo(click.style(
            'User login or Create new account to MyCart', fg='yellow'))

@main.command()
def initdb():
    """Initialize database"""
    db.connect()
    db.create_tables(MODELS)
    click.echo('Initialized the database')


@main.command()
def dropdb():
    """Clear database"""
    db.drop_tables(MODELS)
    click.echo('Dropped the database')
    if os.path.isfile(USER_SECRET_FILE):
        os.remove(USER_SECRET_FILE)


main.add_command(user)
main.add_command(category)
main.add_command(product)

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("cart")
    main()

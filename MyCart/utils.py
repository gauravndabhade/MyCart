import click
import peewee
from models import Cart, Category, Product, User, db
from tabulate import tabulate
from user.session import UserSession
from MyCart.controller import CartController
from product.controller import ProductController
from category.controller import CategoryController

cart = CartController()
user_session = UserSession()
product_controller = ProductController()


def get_discount(amount):
    if amount >= 10000:
        return 500.0, True
    else:
        return 0.0, False


def sum_price(matrix, index):
    return sum(row[index] for row in matrix)


def add_admin(is_admin):
    if is_admin:
        return click.style(' [ADMIN]', fg='green')
    else:
        return click.style(' [CUSTOMER]', fg='green')

def show_bills():
    username, _ = user_session.read_current_user()
    if username:
        click.echo(click.style('Bill : ', fg='cyan') + click.style('\t\t\tPURCHASE ORDER OF MINIMUM 10000/-, AND GET DISCOUNT!!!', fg='green'))
        cart_data = cart.get_cart_products(username)
        if cart_data:
            total_amount = sum_price(cart_data, 1) # 1 -> price coloumn index
            discount_amount, _ = get_discount(total_amount)

            click.echo(click.style(' \tTotal : \t', fg='cyan') +
                            str(total_amount))
            click.echo(click.style(' \tDiscount :', fg='cyan') +
                    '\t' + str(discount_amount))
            click.echo(
                "\t\t\t--------")
            click.echo('\t\t\t' + str(total_amount - discount_amount))
    else:
        show_login_require()

def show_welcome():
    try:
        username, is_admin = user_session.read_current_user()
        if username:
            show_nav(username, is_admin)
            show_categories()
            show_products()
            show_cart_status(username)        
            click.echo(
                    "--------------------------------------------------------------------------------")
        else:
            click.echo('MyCart')
            click.echo(
                "--------------------------------------------------------------------------------")
            show_login_require()
    
    except peewee.OperationalError:
        click.echo('MyCart')
        click.echo(
                "--------------------------------------------------------------------------------")
        show_init_database()


def show_login_require():
    click.echo(click.style(
            'User login or Create new account to MyCart', fg='yellow'))

def show_init_database():
    click.echo(click.style(
        'Not database found. Initalize database with command :  ', fg='yellow')
        +click.style('$ mycart initdb', fg='red'))

def show_nav(username, is_admin):
    click.echo()
    click.echo()
    click.echo('MyCart \t\t\t\t\t\t\t Login as: ' + click.style(username,
                                                                        fg='cyan') + add_admin(is_admin))
    click.echo(
            "--------------------------------------------------------------------------------")
                
def show_categories():
    click.echo(click.style('Categories', fg='cyan'))
    categories = [[cat] for cat in CategoryController().all()]
    if categories:
        click.echo(tabulate(categories, headers=[   
            'Name'], tablefmt='pretty'))
    else:
        click.echo('Categories not found')

def show_products():
    click.echo(click.style('Products', fg='cyan'))
    products = product_controller.get_all_product()
    if products:
        click.echo(tabulate(products, headers=[
            'Name', 'Price'], tablefmt='pretty'))
    else:
        click.echo('Products not found')

def show_cart_status(username):
    click.echo(click.style('Cart', fg='cyan'))
    cart_products = cart.get_cart_products(username)
    if cart_products:
        click.echo(tabulate(cart_products, headers=[
            'Name', 'Price'], tablefmt='pretty'))
    else:
        click.echo('Cart is empty. Add Products in Cart')
import sys

import click
from tabulate import tabulate

from bill.bill_cli import bill
from category.category_cli import category
from models import Product, User
from product.product_cli import product
from user import user_controller, user_session
from user.user_cli import user


def add_admin(is_admin):
    if is_admin:
        return click.style(' [ADMIN]', fg='green')
    else:
        return click.style(' [CUSTOMER]', fg='green')


def get_discount(amount):
    if amount >= 10000:
        return 500.0
    else:
        return 0.0


def sum_price(matrix, index):
    return sum(row[index] for row in matrix)


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

        u = User.select().where(User.username == username).get()
        data = [[p.name, p.category.name, p.price]
                for p in Product.select().where(Product.user == u.id)]
        click.echo(click.style('Products', fg='cyan'))
        click.echo(tabulate(data, headers=[
            'Name', 'Category', 'Price'], tablefmt='pretty'))

        total_amount = sum_price(data, 2)
        click.echo(click.style(' \tTotal : \t', fg='cyan') +
                   str(total_amount))
        click.echo(click.style(' \tDiscount :', fg='cyan') +
                   '\t' + str(get_discount(total_amount)))
        click.echo(
            "\t\t\t--------")
        click.echo('\t\t\t' + str(total_amount - get_discount(total_amount)))

        click.echo(
            "----------------------------------------------------------------------------------------------------------------")
    else:
        click.echo('MyCart')
        click.echo(
            "----------------------------------------------------------------------------------------------------------------")

        click.echo(click.style(
            'User login or Create new account to MyCart', fg='yellow'))


main.add_command(user)
main.add_command(category)
main.add_command(product)
main.add_command(bill)

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("cart")
    main()

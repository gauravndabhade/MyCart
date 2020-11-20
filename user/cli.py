import click
from user.controller import UserController

user_controller = UserController()


@click.group()
def user():
    """Manage user"""
    pass


@user.command()
def create():
    """Creating new user"""

    click.echo("Creating new user!")
    username = click.prompt('Please enter a username')
    password = click.prompt('Please enter password', hide_input=True)
    re_password = click.prompt('Please reenter password', hide_input=True)
    is_admin = 'y' == click.prompt('Creating account as Admin?',
                                   type=click.Choice(['y', 'n']), default='n')

    if password == re_password:
        click.echo(user_controller.create(username, password, is_admin))
    else:
        click.echo('Password mismatch!')


@user.command()
def login():
    """User login"""
    click.echo("User login!")
    username = click.prompt('Please enter a username')
    password = click.prompt('Please enter password', hide_input=True)

    click.echo(user_controller.login(username, password))


@user.command()
def logout(**kwargs):
    """User logout"""
    click.echo(user_controller.logout())

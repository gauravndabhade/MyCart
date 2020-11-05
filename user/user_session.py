import peewee
from models import User


def read_current_user():
    """ Read user data from file (offline session for terminal)
        Return [username, password, is_admin]
    """

    try:
        with open(".current_user.dat", "r") as f:
            data = f.readline().split(',')
            if len(data) == 2:
                return data
            else:
                return None, None
    except FileNotFoundError:
        return None, None


def write_current_user(username, is_admin):
    if username:
        with open(".current_user.dat", 'w', encoding='utf-8') as f:
            f.write(username + ',')
            f.write(str(is_admin))


def current_user():
    try:
        username, _ = read_current_user()
        user = User.select().where(User.username == username).get()
        if user and user.username == username:
            return user
        else:
            return f'User not found for {username}'

    except peewee.DoesNotExist:
        return f'{username} doesn\'t exists'

import peewee
from models import User
from user import user_session


def create(username, password, is_admin):
    try:
        user = User(username=username, password=password,
                    is_admin=is_admin)
        user.save()

        # Update to offline user session
        user_session.write_current_user(username, is_admin)

        return f'User {username} created successful'
    except peewee.IntegrityError:
        return f'User {username} already exist!'
    except peewee.OperationalError:
        return f'Not database found. Initalize database with `mycart initdb` command'


def login(username, password):
    try:
        user = User.select().where(User.username == username).get()
        if user and user.username == username:
            if password == user.password:
                # Update to offline user session
                user_session.write_current_user(user.username, user.is_admin)
                return f'Login successfully for {username}!'
            else:
                return f'Incorrect password'
        else:
            return f'User not found for {username}'

    except peewee.DoesNotExist:
        return f'{username} doesn\'t exists'
    except peewee.OperationalError:
        return f'Not database found. Initalize database with `mycart initdb` command'


def logout():
    user_session.write_current_user(username=None, is_admin=None)
    return f'Logout successfully!'

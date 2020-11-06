
import peewee

from models import Category
from user import user_session


def create(name):
    try:
        user = user_session.current_user()
        category = Category.create(name=name, user=user)
        category.save()

        return f'Category {category.name} created successfully!'
    except peewee.IntegrityError:
        return f'Category {name} already exist!'


def get(name):
    try:
        category = Category.select().where(Category.name == name).get()
        return category
    except peewee.DoesNotExist:
        return f'{name} doesn\'t exists'


def all():
    return [cat.name for cat in Category.select()]

def get_all_categories():
    try:
        data = [[cat.name]
                for cat in Category.select()]         
        return data
    except peewee.DoesNotExist:
        return None
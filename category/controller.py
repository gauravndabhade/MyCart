
import peewee

from models import Category
from user.session import UserSession
from base.controller import BaseController

user_session = UserSession()

class CategoryController(BaseController):
    def create(self, name):
        try:
            user = user_session.current_user()
            category = Category.create(name=name, user=user)
            category.save()

            return f'Category {category.name} created!'
        except peewee.IntegrityError:
            return f'Category {name} already exist!'

    def remove(self, name):
        try:
            category = Category.get(Category.name == name)
            category.delete_instance()
            return f'Category {category.name} removed!'
        except peewee.DoesNotExist:
            return f'{name} doesn\'t exists'


    def get(self, name):
        try:
            category = Category.select().where(Category.name == name).get()
            return category
        except peewee.DoesNotExist:
            return f'{name} doesn\'t exists'


    def all(self):
        try:
            return [cat.name for cat in Category.select()]
        except peewee.DoesNotExist:
            return None
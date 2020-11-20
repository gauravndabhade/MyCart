import peewee

from models import Product
from user.session import UserSession
from category.controller import CategoryController
from base.controller import BaseController

user_session = UserSession()

class ProductController(BaseController):
    def get_all_product(self):
        data = [[p.name, p.price]
                for p in Product.select()]
        return data


    def create(self, name, category, price):

        user = user_session.current_user()
        category = CategoryController().get(category)
        try:
            product = Product.create(name=name, user=user,
                                    price=price, category=category)
            product.save()
            return f'Product {product.name} created!'
        
        except peewee.IntegrityError:
            return f'Product {name} already exist!'

    def remove(self, name):
        product = Product.get(Product.name == name)
        product.delete_instance()
        return f'Product {product.name} removed!'
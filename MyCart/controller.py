import peewee

from models import Cart, User, Product
from user.session import UserSession
from category.controller import CategoryController 
from base.controller import BaseController

user_session = UserSession()

class CartController(BaseController):
    def get_cart_products(self, username):
        u = User.select().where(User.username == username).get()
        data = [[c.product.name, c.product.price]
                for c in Cart.select().where(Cart.user == u.id)]         
        return data

    def add(self, name):
        user = user_session.current_user()
        try:
            username, _ = user_session.read_current_user()
            user = User.select().where(User.username == username).get()
            product = Product.select().where(Product.name == name).get()
            
            cart = Cart.create(user=user, product=product)
            cart.save()
            
            return f'Product {product.name} added to cart!'

        except peewee.DoesNotExist:
            return f'Product {name} not available'

    def remove(self, name):
        try:
            username, _ = user_session.read_current_user()
            user = User.select().where(User.username == username).get()
            product = Product.select().where(Product.name == name).get()
            
            cart_item = Cart.get(Cart.user == user.id, Cart.product == product.id)
            cart_item.delete_instance()
            
            return f'Product {product.name} removed from cart!'

        except peewee.DoesNotExist:
            return f'Product {name} not available'
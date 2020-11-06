import peewee

from models import Cart, User, Product
from user import user_session
from category import category_controller


def get_cart_products(username):
    try:
        u = User.select().where(User.username == username).get()
        data = [[c.product.name, c.product.category.name, c.product.price]
                for c in Cart.select().where(Cart.user == u.id)]         
        return data
    except peewee.DoesNotExist:
        return None


def get_discount(amount):
    if amount >= 10000:
        return 500.0, True
    else:
        return 0.0, False


def sum_price(matrix, index):
    return sum(row[index] for row in matrix)


def add(name):
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


from peewee import SqliteDatabase, Model
from peewee import CharField, ForeignKeyField, TextField, DateTimeField, BooleanField, BigAutoField, FloatField
import datetime


db = SqliteDatabase('sqlite3.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    is_admin = BooleanField(default=False)
    created_date = DateTimeField(default=datetime.datetime.now)


class Category(BaseModel):
    id = BigAutoField()
    name = CharField()
    price = FloatField()
    user = ForeignKeyField(User, backref='categories')
    created_date = DateTimeField(default=datetime.datetime.now)


class Product(BaseModel):
    id = BigAutoField()
    name = CharField()
    user = ForeignKeyField(User, backref='products')
    category = ForeignKeyField(Category, backref='products')
    created_date = DateTimeField(default=datetime.datetime.now)


class Cart(BaseModel):
    id = BigAutoField()
    user = ForeignKeyField(User, backref='carts')
    product = ForeignKeyField(Product, backref='carts')
    created_date = DateTimeField(default=datetime.datetime.now)


class Bill(BaseModel):
    id = BigAutoField()
    user = ForeignKeyField(User, backref='bills')
    product = ForeignKeyField(Product, backref='bills')
    amount = FloatField()
    is_discount = BooleanField()
    created_date = DateTimeField(default=datetime.datetime.now)


db.connect()
db.create_tables([User, Category, Cart, Product, Bill])
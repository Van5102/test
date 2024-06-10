from .extentsion import db
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR, FLOAT, VARCHAR
from sqlalchemy import Column, ForeignKey, Boolean

class customer(db.Model):
    __tablename__ = 'customer'
    customer_id = Column(INTEGER, primary_key=True)
    customer_name = Column(NVARCHAR(50), nullable=False)
    customer_phone = Column(VARCHAR(20), unique=True, nullable=False)
    customer_address = Column(NVARCHAR(100), nullable=False)

    def __init__(self, customer_name, customer_phone, customer_address):
        self.customer_name = customer_name
        self.customer_phone = customer_phone
        self.customer_address = customer_address

class food(db.Model):
    __tablename__ = 'food'
    food_id = Column(INTEGER, primary_key=True)
    food_name = Column(NVARCHAR(50), nullable=False)
    price = Column(FLOAT, nullable=False)

    def __init__(self, food_name, price):
        self.food_name = food_name
        self.price = price

class order(db.Model):
    __tablename__ = 'order'
    order_id = Column(INTEGER, primary_key=True)
    customer_id = Column(INTEGER, ForeignKey(customer.customer_id))
    food_id = Column(INTEGER, ForeignKey(food.food_id))
    quantity = Column(INTEGER, default=1)
    order_price = Column(FLOAT, default = food.price * quantity)

    def __init__(self, customer_id, food_id, quantity):
        self.customer_id = customer_id
        self.food_id = food_id
        self.quantity = quantity
       
class ship(db.Model):
    __tablename__ = 'ship'
    id = Column(INTEGER, primary_key = True)
    customer_id = Column(INTEGER, ForeignKey(customer.customer_id))
    order_id = Column(INTEGER, ForeignKey(order.order_id))
    status = Column(Boolean, default = False)

    def __init__(self, customer_id, order_id):
        self.customer_id = customer_id
        self.order_id = order_id

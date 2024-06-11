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
    total = Column(FLOAT)
    status = Column(Boolean, default=False)

    def __init__(self, customer_id, total, status):
        self.customer_id = customer_id
        self.total = total
        self.status = status
       
class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = Column(INTEGER, primary_key = True)
    customer_id = Column(INTEGER, ForeignKey(customer.customer_id))
    food_id = Column(INTEGER, ForeignKey(food.food_id))
    quantity = Column(INTEGER, nullable = False)
    price = Column(FLOAT, default = 0)

    def __init__(self, customer_id, food_id, quantity, price):
        self.customer_id = customer_id
        self.food_id = food_id
        self.quantity = quantity
        self.price = price

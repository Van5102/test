from flask import Blueprint
from src.views.product import *

user_route = Blueprint('user', __name__)

@user_route.get('/add_food')
def add_food():
    return add_food_view()

@user_route.route('/add_customer')
def add_customer():
    return add_customer_view()

@user_route.route('/get_all_customer')
def get_all_customer():
    return get_all_customer_view()

@user_route.route('/add_order')
def add_order():
    return add_order_view()

@user_route.route('/add_ticket')
def add_ticket():
    return add_ticket_view()

@user_route.route('/order_action')
def order_action():
    return update_order_view()

@user_route.route('/get_all_order', methods=['GET'])
def get_all_order():
    return get_order_view()
from flask import Blueprint
from src.views.product import *

user_route = Blueprint('user', __name__)

@user_route.route('/add_food', methods=['POST'])
def add_food():
    return add_food_view()

@user_route.route('/add_customer', methods=['POST'])
def add_customer():
    return add_customer_view()

@user_route.route('/get_all_customer', methods=['GET'])
def get_all_customer():
    return get_all_customer_view()

@user_route.route('/add_order')
def add_order():
    return add_order_view()

@user_route.route('/add_ticket', methods=['POST'])
def add_ticket():
    return add_ticket_view()

@user_route.route('/order_action', methods=['PUT'])
def order_action():
    return update_order_view()

@user_route.route('/get_all_order')
def get_all_order():
    return get_order_view()

@user_route.route('/get_customer_order')
def get_customer_order():
    return get_customer_order_view()

@user_route.route('/get_order_infor')
def get_order_infor():
    return get_ticket_view()

@user_route.route('/get_food_with_quantity', methods=['GET'])
def get_food_with_quantity():
    return get_food_with_quantity_view()


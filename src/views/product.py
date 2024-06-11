from flask import request, jsonify
from http import HTTPStatus
from src.models import *
from src.extentsion import db
import json

def add_food_view():
    session = db.session()
    try:
        session.add(food("Burger", 10.0))
        session.add(food("Pizza", 20.0))
        session.add(food("Pasta", 15.0))
        session.add(food("Sandwich", 5.0))
        return '1'
    except Exception as e:
        session.rollback()

        return jsonify({
            "Message": "SERVER ERROR",
            "Status": f'{e}'
        }), HTTPStatus.BAD_REQUEST
    finally:
        session.commit()
        session.close()

def add_order_view():
    session = db.session()
    try:
        session.add(order(1, 30.0, False))
        session.add(order(2, 25.0, False))
        return '1'
    except Exception as e:
        session.rollback()

        return jsonify({
            "Message": "Server Error !",
            "Status": f'{e}'
        }), HTTPStatus.BAD_REQUEST
    finally:
        session.commit()
        session.close()

def cancel_order_view():
    session = db.session()
    try:
        order_id = request.args.get('id')
        session.query(order).filter(order.order_id == order_id).delete()
        return '1'
    except Exception as e:
        session.rollback()

        return jsonify({
            "Message": "Server Error !",
            "Status": f'{e}'
        }), HTTPStatus.BAD_REQUEST
    finally:
        session.commit()
        session.close()

def add_customer_view():
    session = db.session()
    try:
        session.add(customer("John", "1234567890", "New York"))
        session.add(customer("Doe", "0987654321", "California"))
        return '1'
    except Exception as e:
        session.rollback()
        return jsonify({
            "Message": "Server Error !",
            "Status": f'{e}'
        }), HTTPStatus.BAD_REQUEST
    finally:
        session.commit()
        session.close()

def get_all_customer_view():
    session = db.session()
    try:
        customers = session.query(customer).all()
        return jsonify({
            "Customers": [customer.customer_name for customer in customers]
        }), HTTPStatus.OK
    except Exception as e:
        session.rollback()
        return jsonify({
            "Message": "Server Error !",
            "Status": f'{e}'
        }), HTTPStatus.BAD_REQUEST
    finally:
        session.commit()
        session.close()

def add_ticket_view():
    session = db.session()
    try:
        customer_id = request.args.get('id')
        if session.query(order).filter(order.customer_id == customer_id) and session.query(order).filter(order.status == False) and customer_id is not None:
            if session.query(Ticket).filter(Ticket.food_id == 1):
                session.query(Ticket).filter(Ticket.food_id == 1).update({Ticket.quantity: Ticket.quantity + 1})
                session.query(Ticket).filter(Ticket.food_id == 1).update({Ticket.price:Ticket.price + 10.0})
                session.query(order).filter(order.customer_id == customer_id).update({order.total: order.total + 10.0})
                return '1'
            else:
                session.add(Ticket(int(customer_id), 1, 2, 20.0))
                session.query(order).filter(order.customer_id == customer_id).update({order.total: order.total + 20.0})
                return '1'
        else:
            return jsonify({
                "Message": "Order not found !"
            }), HTTPStatus.BAD_REQUEST
    except Exception as e:
        session.rollback()
        return jsonify({
            "Message": "Server Error !",
            "Status": f'{e}'
        }), HTTPStatus.BAD_REQUEST
    finally:
        session.commit()
        session.close()

def update_order_view():
    session = db.session()
    try:
        order_id = request.args.get('id')
        status = session.query(order).filter(order.order_id == order_id).first().status
        session.query(order).filter(order.order_id == order_id).update({order.status: not status})
        return '1'
    except Exception as e:
        session.rollback()
        return jsonify({
            "Message": "Server Error !",
            "Status": f'{e}'
        }), HTTPStatus.BAD_REQUEST
    finally:
        session.commit()
        session.close()

def get_order_view():
    session = db.session()
    try:
        orders = session.query(order).all()
        return jsonify({
            "Orders": [order.order_id for order in orders]
        }), HTTPStatus.OK
    except Exception as e:
        session.rollback()
        return jsonify({
            "Message": "Server Error !",
            "Status": f'{e}'
        }), HTTPStatus.BAD_REQUEST
    
    finally:
        session.commit()
        session.close()
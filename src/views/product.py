from flask import request, jsonify
from http import HTTPStatus
from src.models import *
from src.extentsion import db

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

def order_food_view():
    session = db.session()
    try:
        session.add(order(1, 1, 20))
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
from flask import request, jsonify
from http import HTTPStatus
from src.models import *
from src.extentsion import db
from src.ma_schemas import UserSchema, TicketSchema, CustomerSchema
from sqlalchemy import func
user_schema = UserSchema(many=True)
ticket_schema = TicketSchema(many=True)
customer_schema = CustomerSchema(many=True)

def add_food_view():
    session = db.session()
    try:
        name = request.get_json()['name']
        price = request.get_json()['price']
        session.add(food(name, price))
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
        session.add(order(1, 300.0, True))
        session.add(order(2, 20.0, True))
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
        name = request.get_json()['name']
        phone = request.get_json()['phone']
        address = request.get_json()['address']
        session.add(customer(name, phone, address))
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

def add_ticket_view():
    session = db.session()
    try:
        json_data = request.get_json()
        for i in json_data:
            customer_id = i['customer_id']
            food_id = i['food_id']
            quantity = i['quantity']
            price = i['price']
            session.add(Ticket(customer_id, food_id, quantity, price))
        return '1'
        # customer_id = request.args.get('id')
        # food_id = request.args.get('food_id')
        # if session.query(order).filter(order.customer_id == customer_id).first() and session.query(order).filter(order.status == False).first():
        #     if session.query(Ticket).filter(Ticket.food_id == food_id).first():
        #         session.query(Ticket).filter(Ticket.food_id == food_id).update({Ticket.quantity: Ticket.quantity + 1})
        #         session.query(Ticket).filter(Ticket.food_id == food_id).update({Ticket.price:Ticket.price + 10.0})
        #         session.query(order).filter(order.customer_id == customer_id).update({order.total: order.total + 10.0})
        #         return '1'
        #     else:
        #         session.add(Ticket(customer_id, food_id, 1, 10.0))
        #         session.query(order).filter(order.customer_id == customer_id).update({order.total: order.total + 10.0})
        #         return '1'
        # else:
        #     session.add(order(customer_id, 10.0, False))
        #     session.add(Ticket(customer_id, food_id, 1, 10.0))
        #     return '1'
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
        order_id = request.get_json()['id']
        status = request.get_json()['status']
        session.query(order).filter(order.order_id == order_id).update({order.status: status})
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

# 1
def get_customer_order_view():
    session = db.session()
    try:
        customer_id = request.args.get('id')
        orders = session.query(order).filter(order.customer_id == customer_id).all()
        return jsonify({
            "Result":[{
                "Orders": order.order_id,
                "Total": order.total,
                "Status": order.status
            }for order in orders]
            
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

# 2
# update with inner join: done
def get_ticket_view():
    session = db.session()
    try:
        Customer = customer.query.with_entities(
            customer.customer_name,
            food.food_name,
            Ticket.quantity,
            Ticket.price,
        ).join(
            order, customer.customer_id == order.customer_id
        ).join(
            Ticket, order.order_id == Ticket.order_id
        ).join(
            food, Ticket.food_id == food.food_id
        ).all()
        return user_schema.dump(Customer), HTTPStatus.OK
        # tickets = session.query(Ticket).filter(Ticket.order_id == order_id).all()
        # return jsonify({
        #     "Tickets": [{
        #         "Ticket ID": ticket.id,
        #         "Customer ID": ticket.order_id,
        #         "Food ID": ticket.food_id,
        #         "Quantity": ticket.quantity,
        #         "Price": ticket.price
        #     } for ticket in tickets]
        # }), HTTPStatus.OK
    except Exception as e:
        session.rollback()
        return jsonify({
            "Message": "Server Error !",
            "Status": f'{e}'
        }), HTTPStatus.BAD_REQUEST
    finally:
        session.commit()
        session.close()

def get_food_with_quantity_view():
    session = db.session()
    try:
        Food = food.query.with_entities(
            food.food_name,
            func.sum(order.total).label('Total_Quantity')
        ).join(
            Ticket, food.food_id == Ticket.food_id
        ).join(
            order, Ticket.order_id == order.order_id
        ).group_by(
            food.food_id
        ).having(
            func.sum(order.total) > 200
        ).all()
        return ticket_schema.dump(Food), HTTPStatus.OK
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
        Customer = customer.query.with_entities(
            customer.customer_name,
            customer.customer_phone,
            customer.customer_address
        ).join(
            order, customer.customer_id  == order.customer_id
        ).join(
            Ticket, order.order_id == Ticket.order_id
        ).group_by(
            customer.customer_id
        ).having(
            func.sum(Ticket.quantity) > 5
        ).all()
        return customer_schema.dump(Customer), HTTPStatus.OK
        
    except Exception as e:
        session.rollback()
        return jsonify({
            "Message": "Server Error !",
            "Status": f'{e}'
        }), HTTPStatus.BAD_REQUEST
    finally:
        session.commit()
        session.close()
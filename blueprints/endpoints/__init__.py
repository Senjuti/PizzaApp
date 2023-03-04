from flask import Blueprint, render_template

from models.Pizza import Pizza

blueprint = Blueprint('api', __name__, url_prefix='/')


@blueprint.route('/', methods=['GET'])
def config():
    return render_template('index.html', greeting='This is a Pizza delivery Flask app')


@blueprint.route('/order/<int:number>/<string:size>', methods=['POST'])
def order(number, size):
    pizza = Pizza(size)
    price = number * pizza.price
    return f'Placed an order for {number} Pizza(s) {pizza}. Total Price={price}. Order number'


@blueprint.route('/order/<int:number>', methods=['GET'])
def check_order_status(number):
    return f'Order number={number}'

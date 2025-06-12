from flask import Blueprint
from controllers import example_controller

calculator_bp = Blueprint('calculator', __name__)

@calculator_bp.route('/add', methods=['POST'])
def add():
    return example_controller.add()

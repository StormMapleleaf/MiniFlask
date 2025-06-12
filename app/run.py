from flask import Flask, Blueprint
from controllers import example_controller

app = Flask(__name__)

calculator_bp = Blueprint('calculator', __name__)

@calculator_bp.route('/add', methods=['POST'])
def add():
    return example_controller.add()

if __name__ == '__main__':
    app.run(debug=True,port=5176)
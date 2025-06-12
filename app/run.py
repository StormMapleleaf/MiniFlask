from flask import Flask
from controllers import example_controller

app = Flask(__name__)

# 注册/add路由，POST方法
app.add_url_rule('/add', view_func=example_controller.add, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True,port=5176)
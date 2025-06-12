from flask import Flask

def create_app():
    app = Flask(__name__)

    # 注册蓝图
    from routes.example_route import calculator_bp
    app.register_blueprint(calculator_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True,port=5176)
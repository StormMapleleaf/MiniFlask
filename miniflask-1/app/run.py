from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.example_route import calculator_bp
    app.register_blueprint(calculator_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
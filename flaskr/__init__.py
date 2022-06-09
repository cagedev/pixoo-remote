from flask import Flask

def create_app(flag):
    print(flag)
    app = Flask(__name__)

    from flaskr.routes import index
    app.register_blueprint(index)

    from flaskr.routes import test
    app.register_blueprint(test)

    from flaskr.routes import login
    app.register_blueprint(login)

    return app
from flask import Flask

def create_app(flag):
    # print(flag)
    app = Flask(__name__)

    from pxr.routes import index
    app.register_blueprint(index)

    from pxr.routes import test
    app.register_blueprint(test)

    from pxr.routes import login
    app.register_blueprint(login)

    return app
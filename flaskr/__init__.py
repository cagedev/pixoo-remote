from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/test')
    def hello():
        return 'test'

    return app
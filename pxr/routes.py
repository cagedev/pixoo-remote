from flask import current_app, Blueprint, render_template

index = Blueprint('index', __name__)


@index.route('/')
def render_index():
    return render_template('base.html', title='Pixoo-Remote')


test = Blueprint('test', __name__)


@test.route('/test1')
def render_test1():
    return 'test1a'


@test.route('/test2')
def render_test2():
    return 'test2a'


login = Blueprint('login', __name__)


@login.route('/login')
def render_login():
    return render_template('login.html', title='Pixoo-Remote')


control = Blueprint('control', __name__)


@control.route('/control')
def render_control():
    return render_template('control.html', title='Pixoo-Remote')

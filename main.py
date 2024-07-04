from flask import (Flask, make_response, redirect, render_template, request,
                   session, url_for)
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'


players = ['Patrick Mahomes', 'Travis Kelce', 'Isah Pacheco','Derrick Nnadi', 'George Karlaftis']

class LoginForm (FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip

    return response

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    username = session.get('username')
    login_form = LoginForm()
    context = {
        'user_ip':user_ip,
        'players':players,
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        return redirect(url_for('index'))
    # user_ip = request.remote_addr
    # return 'Hola, tu IP es {}'.format(user_ip)
    return render_template('hello.html',  **context)
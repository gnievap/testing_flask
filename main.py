import unittest

from flask import (flash, make_response, redirect, render_template, request,
                   session, url_for)
from flask_bootstrap import Bootstrap

from app import create_app
from app.forms import LoginForm

app = create_app()



players = ['Patrick Mahomes', 'Travis Kelce', 'Isah Pacheco','Derrick Nnadi', 'George Karlaftis']



@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

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

        flash('Nombre de usuario registrado con éxito')

        return redirect(url_for('index'))
    # user_ip = request.remote_addr
    # return 'Hola, tu IP es {}'.format(user_ip)
    return render_template('hello.html',  **context)
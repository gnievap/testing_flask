from flask import Flask, make_response, redirect, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)



players = ['Patrick Mahomes', 'Travis Kelce', 'Isah Pacheco','Derrick Nnadi', 'George Karlaftis']

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
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip':user_ip,
        'players':players,
    }

    # user_ip = request.remote_addr
    # return 'Hola, tu IP es {}'.format(user_ip)
    return render_template('hello.html',  **context)
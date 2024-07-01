from flask import Flask, make_response, redirect, render_template, request

app = Flask(__name__)

players = ['Patrick Mahomes', 'Travis Kelce', 'Isah Pacheco','Derrick Nadhi', 'George Karlaftis']

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
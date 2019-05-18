from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.config['DEBUG'] = True


# @app.before_request
# def requirements():



@app.route('/sign-up')
def signup():


    return render_template('sign-up.html')


@app.route('/sign-up', methods=['POST'])
def requirements():

    username = request.form['username']
    password = request.form['password']
    # verify = request.form['verify']
    # email = request.form['email']

    username_error = ''
    password_error = ''
    # verify_error = ''
    # email_error = ''

    if len(username) > 3 or len(username) < 20:
        username=username
        username_error=''
    else:
        username_error = 'Username must be 3-20 characters.'
        username = ''
    if not username_error:
        return redirect('/signed-in')
    else:
        return render_template('sign-up.html',
        username_error=username_error,
        username=username)



@app.route('/signed-in')
def signed_in():
    username = request.args.get('username')
    # password = request.form['password']
    # verify = request.form['verify']
    # email = request.form['email']


    return '<h1>Welcome, {0}.</h1>'.format(username)
    # return render_template('signed-in.html', name=username)


@app.route('/')
def index():
    return redirect('/sign-up')


app.run()
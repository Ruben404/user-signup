from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.config['DEBUG'] = True


# @app.before_request
# def requirements():



@app.route("/signup", methods=['POST', 'GET'])
def signup():

    return render_template('signup.html')


@app.route("/signed-in", methods=['POST', 'GET'])
def signed_in():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) == 0:
        username_error = 'field required*'
        username = ''
    else:
        pass

    if len(username) > 3 or len(username) < 20:
        pass
    else:
        username_error = 'Username must be 3-20 characters.'
        username = ''

    return render_template('signed-in.html', name=username)


@app.route("/")
def index():
    return redirect('/signup')


app.run()
from flask import Flask, render_template, request, redirect

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

    if len(username) > 3 and len(username) < 20:
        pass        
    elif len(username) == 0:
        username_error = 'Field required*'
        username = ''
        
    else:
        username_error = 'Not a valid length. (3-20)'
        username = ''

    if password == verify:
        pass
    else:
        verify_error = ' Passwords do not match.'
        password = ''
        verify = ''

    if email == '':
        pass
    elif len(email) > 3 and len(email) < 20:
        pass
    else:
        if len(email) > 0 and len(email) < 3:
            email_error = 'email length is too short.'
            email = ''
        elif len(email) >20:
            email_error = 'email is too long.'
        else:
            pass



    if not username_error and  not password_error and not verify_error and not email_error:

        return render_template('signed-in.html', name=username)
    else:
        return render_template('signup.html',
        username=username,
        password=password,
        verify=verify,
        email=email,
        username_error=username_error,
        password_error=password_error,
        verify_error=verify_error,
        email_error=email_error)


@app.route("/")
def index():
    return redirect('/signup')


app.run()
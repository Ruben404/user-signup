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

    

    return render_template('signed-in.html', name=username)


@app.route("/")
def index():
    return redirect('/signup')


app.run()
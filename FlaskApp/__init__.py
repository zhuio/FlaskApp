from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run()

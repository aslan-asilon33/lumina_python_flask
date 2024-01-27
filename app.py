from flask import Flask, render_template, redirect, url_for

# app = Flask(__name__)
app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route("/")
def index():
    # return 'Index Page <a href="' + url_for('login') + '"> go to login page</a>'
    return render_template('welcome.html')

@app.route('/login')
def login():
    # Render the HTML template
    return render_template('login/index.html')

if __name__ == "__main__":
    app.run(debug=True)

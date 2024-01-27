# routes/web.py
from flask import render_template

def init_routes(app):
    @app.route("/")
    def index():
        # return 'Index Page <a href="' + url_for('login') + '"> go to login page</a>'
        return render_template('welcome.html')

    @app.route('/login')
    def login():
        # Render the HTML template
        return render_template('login/index.html')

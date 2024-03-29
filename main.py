"""`main` is the top level module for your Flask application."""
# Note: You don't need to call app.run() when running `dev_appserver.py .` or deploying to App Engine,
# since the application is embedded within the App Engine WSGI application server.

from flask import Flask, render_template, make_response, send_from_directory
app = Flask(__name__)#, static_folder='./static', static_url_path='/static')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    print 'a'
    return render_template("index.html")

'''
@app.route('/')
def home():
    """Return a friendly HTTP greeting."""
    return render_template("index.html")
'''
if __name__ == "__main__":
    app.run(debug=True)

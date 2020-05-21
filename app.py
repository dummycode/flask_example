import os
from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'my_secret_key')


###
# Routing for your application.
###

@app.route('/')
def home():
    return jsonify({
        "app_name": "HH Test App",
        "version": "0.1.0",
    })

@app.route('/post', methods=["POST"])
def post():
    return jsonify({
        "app_name": "HH Test App",
        "version": "0.1.0",
        "request": "POST",
    })

@app.route('/post', methods=["POST"])
def post():
    return jsonify({
        "app_name": "HH Test App",
        "version": "0.1.0",
        "request": "POST",
    })

@app.route('/put', methods=["PUT"])
def put():
    return jsonify({
        "app_name": "HH Test App",
        "version": "0.1.0",
        "request": "PUT",
    })

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify("Error 404"), 404


if __name__ == '__main__':
    app.run(debug=True)

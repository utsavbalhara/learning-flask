# routes_example.py - Demonstrating different routes in Flask

from flask import Flask

app = Flask(__name__)

# Basic route returning a string
@app.route('/')
def home():

    return 'Welcome to the Flask Tutorial!'

# Route with a parameter
@app.route('/user/<username>')
def show_user(username):

    # Route that captures a username parameter
    # The parameter becomes an argument to the function

    return f'Hello, {username}!'

# Route with a typed parameter (integer)
@app.route('/post/<int:post_id>')
def show_post(post_id):

    # Route that captures a numeric post ID
    # Flask automatically converts the parameter to the specified type

    return f'Showing post with ID: {post_id}'

# Route with multiple parameters
@app.route('/product/<category>/<int:product_id>')
def product_detail(category, product_id):

# Route with multiple parameters of different types
    return f'Viewing {category} product #{product_id}'

if __name__ == '__main__':
    app.run()

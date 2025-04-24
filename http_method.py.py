# http_methods.py - Handling different HTTP methods in Flask

from flask import Flask, request

app = Flask(__name__)

# Route that handles both GET and POST methods
@app.route('/form', methods=['GET', 'POST'])
def handle_form():



if __name__ == '__main__':
    app.run(debug=True)

# request_response.py - Working with request and response objects

from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['GET', 'POST'])
def echo():
    """
    Echo back the request data based on request method
    Demonstrates accessing different request properties
    """
    if request.method == 'GET':
        # Access query parameters (from URL)
        name = request.args.get('name', 'World')
        return f'Hello, {name}!'
    elif request.method == 'POST':
        # Access form data
        if request.form:
            name = request.form.get('name', 'World')
            return f'Hello, {name}!'
        # Access JSON data
        elif request.is_json:
            data = request.get_json()
            return jsonify({"message": f"Received: {data}"})
        else:
            return "No data received"

@app.route('/custom_response')
def custom_response():
    """
    Demonstrates creating a custom response with
    status code, headers, and cookies
    """
    # Create response object
    resp = make_response("Custom response content")

    # Set status code
    resp.status_code = 200

    # Set a header
    resp.headers['Content-Type'] = 'text/plain'

    # Set a cookie
    resp.set_cookie('user_visited', 'yes')

    return resp

if __name__ == '__main__':
    app.run(debug=True)

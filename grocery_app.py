# grocery_app.py - Complete Flask application for grocery invoice generation

from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the form page
FORM_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Grocery Store Invoice Generator</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: inline-block; width: 120px; }
        input[type="text"], input[type="number"] { padding: 5px; width: 200px; }
        button { padding: 8px 15px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        .invoice { margin-top: 20px; border: 1px solid #ddd; padding: 15px; max-width: 400px; }
    </style>
</head>
<body>
    <h1>Grocery Store Invoice Generator</h1>

    <form method="POST" action="/generate-invoice">
        <div class="form-group">
            <label for="customer_name">Customer Name:</label>
            <input type="text" id="customer_name" name="customer_name" required>
        </div>

        <div class="form-group">
            <label for="item_a_cost">Cost of Item A:</label>
            <input type="number" id="item_a_cost" name="item_a_cost" min="0" step="0.01" required>
        </div>

        <div class="form-group">
            <label for="item_b_cost">Cost of Item B:</label>
            <input type="number" id="item_b_cost" name="item_b_cost" min="0" step="0.01" required>
        </div>

        <button type="submit">Generate Invoice</button>
    </form>

    {% if show_invoice %}
    <div class="invoice">
        <h2>Invoice</h2>
        <p>Customer: {{ customer_name }}</p>
        <p>The amount of item A is Rs. {{ item_a_cost }}</p>
        <p>The amount of item B is Rs. {{ item_b_cost }}</p>
        <p><strong>The total amount is Rs. {{ total_amount }}</strong></p>
    </div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    """
    Display the form for invoice generation
    This is the main entry point of the application
    """
    return render_template_string(FORM_TEMPLATE, show_invoice=False)

@app.route('/generate-invoice', methods=['POST'])
def generate_invoice():
    """
    Process form submission and generate invoice
    This handles the POST request from the form
    """
    # Extract form data
    customer_name = request.form.get('customer_name', '')

    # Get costs and convert to float
    try:
        item_a_cost = float(request.form.get('item_a_cost', 0))
        item_b_cost = float(request.form.get('item_b_cost', 0))
    except ValueError:
        return "Invalid input. Please enter valid numbers for costs."

    # Calculate total
    total_amount = item_a_cost + item_b_cost

    # Render template with invoice data
    return render_template_string(
        FORM_TEMPLATE,
        show_invoice=True,
        customer_name=customer_name,
        item_a_cost=item_a_cost,
        item_b_cost=item_b_cost,
        total_amount=total_amount
    )

if __name__ == '__main__':
    app.run(debug=True)

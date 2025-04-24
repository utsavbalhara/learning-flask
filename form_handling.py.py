# form_handling.py - Complete form handling in Flask

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Simple form displayed on GET, processed on POST
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Contact form handler:
    - GET: Display the form
    - POST: Process the submitted form
    """
    if request.method == 'POST':
        # Extract form data
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        message = request.form.get('message', '')

        # Process form data (in a real app, might save to database)
        # For this example, we'll just print it
        print(f"Received message from {name} ({email}): {message}")

        # Redirect to thank you page (prevents form resubmission)
        return redirect(url_for('thank_you'))

    # If GET request, show the form
    return '''
        <h1>Contact Us</h1>
        <form method="POST">
            <div>
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div>
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            <button type="submit">Send Message</button>
        </form>
    '''

@app.route('/thank-you')
def thank_you():
    """Thank you page after form submission"""
    return '<h1>Thank You!</h1><p>Your message has been received.</p>'

if __name__ == '__main__':
    app.run(debug=True)

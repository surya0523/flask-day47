from flask import Flask, request, redirect, url_for, render_template, flash
from flask import session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    department = request.form['department']
    source = request.args.get('source', 'unknown')

    print(f"Received from {name} ({email}) for {department}: {message} (source: {source})")

    flash(f"Thank you {name}, your message to the {department} department has been sent.")
    return redirect(url_for('thank_you'))

@app.route('/contact/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/contact/<department>')
def contact_department(department):
    return f"<h3>Welcome to the {department.capitalize()} Department Contact Page</h3>"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 1. Contact form route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        message = request.form.get('message', '').strip()

        # 4. Basic form validation
        if not name or not message:
            return "Name and message are required.", 400

        # 8. Print form data to terminal
        print(f"Contact Form Submitted: Name = {name}, Message = {message}")

        # 2 & 3. Redirect to thank you page
        return redirect(url_for('thank_you', name=name))

    return render_template('contact.html')

# 3. Thank you page
@app.route('/thankyou')
def thank_you():
    name = request.args.get('name', 'Guest')
    return render_template('thankyou.html', name=name)

# 7. Feedback form
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        rating = request.form.get('rating')
        message = request.form.get('message', '')

        print(f"Feedback: {name} rated {rating} - {message}")
        return render_template('show_data.html', data=request.form)

    return render_template('feedback.html')

# 9. Register form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        print(f"Registered: {name}, {email}")
        return render_template('show_data.html', data=request.form)

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

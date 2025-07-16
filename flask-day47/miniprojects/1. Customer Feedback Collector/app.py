from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory store for feedback (for demo purposes)
feedback_list = []

# 1. Feedback form route
@app.route('/feedback-form')
def feedback_form():
    return render_template('feedback_form.html')

# 2. Handle form POST and redirect to /thank-you
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        return "All fields are required!", 400

    # Store feedback in list
    feedback_list.append({'name': name, 'email': email, 'message': message})

    return redirect(url_for('thank_you'))

# 3. Thank you page
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

# 4. Show feedbacks (optional filter with ?user=name)
@app.route('/feedbacks')
def feedbacks():
    user = request.args.get('user')
    if user:
        filtered = [fb for fb in feedback_list if fb['name'].lower() == user.lower()]
    else:
        filtered = feedback_list
    return render_template('feedbacks.html', feedbacks=filtered, user=user)

# 5. Dynamic user route
@app.route('/user/<username>')
def user_profile(username):
    user_feedback = [fb for fb in feedback_list if fb['name'].lower() == username.lower()]
    return render_template('user.html', username=username, feedbacks=user_feedback)

if __name__ == '__main__':
    app.run(debug=True)


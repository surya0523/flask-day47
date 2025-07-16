from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# # Task 7: Print method in console for every request
# @app.before_request
# def log_method():
#     print(f"HTTP Method Used: {request.method}")

# # Task 1: Return current HTTP method
# @app.route('/method-check', methods=['GET', 'POST'])
# def method_check():
#     return f"Current HTTP method: {request.method}"

# # Task 2: Only POST allowed
# @app.route('/submit', methods=['POST'])
# def submit():
#     return "Form submitted successfully via POST"

# # Task 3: Allow both methods and return which one was used
# @app.route('/both-methods', methods=['GET', 'POST'])
# def both_methods():
#     return f"You used {request.method} method"

# Task 4: Show login form (POST method)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Task 5: Return entered username
        username = request.form.get('username')
        return f"Welcome, {username}!"
    return '''
        <h2>Login</h2>
        <form method="POST">
            Username: <input type="text" name="username" />
            <input type="submit" value="Login" />
        </form>
    '''

# # Task 6: Restrict /admin to GET
# @app.route('/admin', methods=['GET', 'POST'])
# def admin():
#     if request.method == 'POST':
#         return "POST not allowed here!", 405
#     return "Welcome to the admin panel (GET only)"

# # Task 8: Feedback form with textarea
# @app.route('/feedback', methods=['GET'])
# def feedback():
#     return '''
#         <h2>Feedback Form</h2>
#         <form action="/submit-feedback" method="POST">
#             <textarea name="comments" rows="4" cols="40" placeholder="Enter feedback..."></textarea><br>
#             <input type="submit" value="Submit Feedback" />
#         </form>
#     '''

# # Task 8 continuation: handle feedback submission
# @app.route('/submit-feedback', methods=['POST'])
# def submit_feedback():
#     feedback_text = request.form.get('comments')
#     return f"Feedback received: {feedback_text}"

# # Task 9: Button that submits a POST request
# @app.route('/post-button', methods=['GET'])
# def post_button():
#     return '''
#         <form action="/submit" method="POST">
#             <button type="submit">Submit via POST</button>
#         </form>
#     '''

# # Task 10: Form with GET vs POST method toggle
# @app.route('/choose-method', methods=['GET', 'POST'])
# def choose_method():
#     if request.method == 'POST':
#         return f"Submitted via POST: {request.form.get('data')}"
#     elif request.args.get('data'):
#         return f"Submitted via GET: {request.args.get('data')}"
#     return '''
#         <h2>Submit with GET or POST</h2>
#         <form method="GET">
#             <input type="text" name="data" placeholder="Enter something (GET)" />
#             <input type="submit" value="Submit via GET" />
#         </form>
#         <form method="POST" style="margin-top:10px;">
#             <input type="text" name="data" placeholder="Enter something (POST)" />
#             <input type="submit" value="Submit via POST" />
#         </form>
#     '''

if __name__ == '__main__':
    app.run(debug=True)

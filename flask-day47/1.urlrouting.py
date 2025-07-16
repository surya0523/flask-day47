from flask import Flask, abort

app = Flask(__name__)

# 1. Hello route
@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

# 2. Square of a number
@app.route('/square/<int:number>')
def square(number):
    return f"Square of {number} is {number ** 2}"

# 3. Greeting with name and age
@app.route('/greet/<name>/<int:age>')
def greet(name, age):
    return f"Hi {name}, you are {age} years old!"

# 4. Status update
@app.route('/status/<username>/<status>')
def status(username, status):
    return f"{username} is currently {status}"

# 5. Price with float
@app.route('/price/<float:amount>')
def price(amount):
    return f"The price is ₹{amount:.2f}"

# 6. Mini profile in HTML
@app.route('/profile/<username>')
def profile(username):
    return f"""
    <h2>User Profile</h2>
    <p>Username: <strong>{username}</strong></p>
    """

# 7. Math operations
@app.route('/math/<int:x>/<int:y>')
def math(x, y):
    return f"Sum: {x+y}, Difference: {x-y}, Product: {x*y}"

# 8. Path converter
@app.route('/file/<path:filename>')
def file(filename):
    return f"Requested file path: {filename}"

# 9. Color text in HTML
@app.route('/color/<string:color>')
def color_text(color):
    return f"<p style='color:{color};'>This is {color} text!</p>"

# 10. Language validation
@app.route('/language/<lang>')
def language(lang):
    valid_langs = ['python', 'java', 'c++', 'javascript']
    if lang.lower() in valid_langs:
        return f"{lang} is a supported language."
    else:
        return f"{lang} is not supported."

# 11. User existence check
@app.route('/user/<username>')
def user_check(username):
    users = ['surya', 'admin', 'guest']
    if username.lower() in users:
        return f"Welcome back, {username}!"
    else:
        return "User not found."

# 12. Country code lookup
@app.route('/country/<code>')
def country(code):
    countries = {
        'IN': 'India',
        'US': 'United States',
        'UK': 'United Kingdom',
        'JP': 'Japan'
    }
    return countries.get(code.upper(), "Country code not recognized.")

# 13. Debug print
@app.route('/debug/<value>')
def debug(value):
    print(f"Debug value received: {value}")
    return f"Check console for debug value: {value}"

# 14. Triple-quoted HTML
@app.route('/info/<name>/<int:age>')
def info(name, age):
    return f"""
    <html>
    <body>
        <h1>Personal Info</h1>
        <p>Name: {name}</p>
        <p>Age: {age}</p>
    </body>
    </html>
    """

# 15. Error route
@app.route('/error/<int:code>')
def error(code):
    messages = {
        404: "Page not found",
        500: "Internal server error",
        403: "Forbidden access"
    }
    return messages.get(code, "Unknown error code")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

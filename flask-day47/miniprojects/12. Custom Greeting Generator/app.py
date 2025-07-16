from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    time = request.args.get('time', 'day')
    return f"<h3>Good {time.capitalize()}, {name}!</h3>"

@app.route('/custom-greet/<name>')
def custom_greet(name):
    return f"<h3>Hello, {name.capitalize()}! Welcome to our site!</h3>"

@app.route('/greet-form')
def greet_form():
    return render_template('greet_form.html')

@app.route('/submit-greet', methods=['POST'])
def submit_greet():
    name = request.form['name']
    time = request.form['time']
    return redirect(url_for('greet_result', name=name, time=time))

@app.route('/greet-result')
def greet_result():
    name = request.args.get('name', 'Guest')
    time = request.args.get('time', 'day')
    return f"<h3>Greeting Sent: Good {time.capitalize()}, {name}!</h3>"

if __name__ == '__main__':
    app.run(debug=True)

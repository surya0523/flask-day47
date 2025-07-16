from flask import Flask, request, redirect, url_for, render_template
from datetime import datetime

app = Flask(__name__)

subscribers = []

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        month = datetime.now().strftime('%B')  # e.g. July

        subscribers.append({
            'name': name,
            'email': email,
            'month': month
        })

        return redirect(url_for('thanks', name=name))
    return render_template('subscribe.html')

@app.route('/thanks/<name>')
def thanks(name):
    return f"<h3>Thank you, {name}, for subscribing to our newsletter!</h3>"

@app.route('/subscribers')
def list_subscribers():
    month_filter = request.args.get('month')
    if month_filter:
        filtered = [s for s in subscribers if s['month'].lower() == month_filter.lower()]
    else:
        filtered = subscribers
    return render_template('subscribers.html', subscribers=filtered, month=month_filter)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

donations = []

@app.route('/donate', methods=['GET'])
def donate_form():
    return render_template('donate.html')

@app.route('/donate-confirm', methods=['POST'])
def donate_confirm():
    name = request.form['name']
    amount = float(request.form['amount'])
    purpose = request.form['purpose']

    donations.append({
        'name': name,
        'amount': amount,
        'purpose': purpose
    })

    return redirect(url_for('thank_donor', name=name))

@app.route('/thank-donor/<name>')
def thank_donor(name):
    return f"<h3>Thank you, {name}, for your generous donation!</h3>"

@app.route('/donations')
def view_donations():
    purpose = request.args.get('purpose')
    if purpose:
        filtered = [d for d in donations if d['purpose'].lower() == purpose.lower()]
    else:
        filtered = donations
    return render_template('donations.html', donations=filtered, purpose=purpose)

if __name__ == '__main__':
    app.run(debug=True)

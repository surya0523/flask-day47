from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# In-memory storage of RSVPs (in production, use a database)
rsvp_list = []

# 1. /rsvp - GET form for RSVP
@app.route('/rsvp', methods=['GET'])
def rsvp_form():
    return render_template('rsvp_form.html')

# 2. Handle POST submission and redirect to /thank-you/<name>
@app.route('/rsvp-confirm', methods=['POST'])
def rsvp_confirm():
    name = request.form.get('name')
    email = request.form.get('email')
    attending = request.form.get('attending')

    if not name or not email or not attending:
        return "All fields are required", 400

    rsvp_list.append({
        'name': name,
        'email': email,
        'attending': attending.lower()
    })

    return redirect(url_for('thank_you', name=name))

# 3. Dynamic thank-you page for each guest
@app.route('/thank-you/<name>')
def thank_you(name):
    return render_template('thank_you.html', name=name)

# 4. View all guests with optional attending filter
@app.route('/guests')
def guests():
    attending_filter = request.args.get('attending')
    if attending_filter:
        filtered = [g for g in rsvp_list if g['attending'] == attending_filter.lower()]
    else:
        filtered = rsvp_list
    return render_template('guests.html', guests=filtered, attending=attending_filter)
    
if __name__ == '__main__':
    app.run(debug=True)

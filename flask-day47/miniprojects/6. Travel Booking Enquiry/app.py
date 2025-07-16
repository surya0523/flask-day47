from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# Dummy deal data
travel_deals = {
    "paris": ["Eiffel Tower Tour", "Seine Cruise", "Disneyland Package"],
    "tokyo": ["Mount Fuji Day Trip", "Tokyo Disneyland", "Sushi Workshop"],
    "newyork": ["Statue of Liberty", "Broadway Show", "Central Park Tour"]
}

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        destination = request.form['destination']
        travel_date = request.form['travel_date']
        print(f"Booking received: {name} - {destination} - {travel_date}")
        return redirect(url_for('confirm_booking', name=name))
    return render_template('booking.html')

@app.route('/booking/confirm/<name>')
def confirm_booking(name):
    return f"<h3>Thank you {name}, your travel booking enquiry has been submitted!</h3>"

@app.route('/deals')
def deals():
    dest = request.args.get('destination')
    deals = travel_deals.get(dest.lower(), []) if dest else []
    return render_template('deals.html', destination=dest, deals=deals)

if __name__ == '__main__':
    app.run(debug=True)

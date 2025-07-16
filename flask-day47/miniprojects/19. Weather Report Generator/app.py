from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# Dummy weather data for demo
weather_data = {
    "new york": {"metric": {"temp": 22, "desc": "Cloudy"}, "imperial": {"temp": 72, "desc": "Cloudy"}},
    "london": {"metric": {"temp": 18, "desc": "Rainy"}, "imperial": {"temp": 64, "desc": "Rainy"}},
    "paris": {"metric": {"temp": 20, "desc": "Sunny"}, "imperial": {"temp": 68, "desc": "Sunny"}},
}

@app.route('/weather', methods=['GET'])
def weather_form():
    return render_template('weather_form.html')

@app.route('/weather-result', methods=['POST'])
def weather_result():
    city = request.form['city'].strip().lower()
    return redirect(url_for('weather_report', city=city))

@app.route('/weather/<city>')
def weather_report(city):
    unit = request.args.get('unit', 'metric').lower()
    city_lower = city.lower()
    if city_lower in weather_data:
        data = weather_data[city_lower].get(unit, weather_data[city_lower]['metric'])
        return render_template('weather_report.html', city=city.capitalize(), temp=data['temp'], desc=data['desc'], unit=unit)
    else:
        return f"<h3>No weather data available for {city.capitalize()}.</h3>"

if __name__ == '__main__':
    app.run(debug=True)

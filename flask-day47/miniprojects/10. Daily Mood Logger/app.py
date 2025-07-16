from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# In-memory mood logs
mood_logs = []

@app.route('/log-mood', methods=['GET'])
def log_mood():
    return render_template('log_mood.html')

@app.route('/mood-result', methods=['POST'])
def mood_result():
    name = request.form['name']
    mood = request.form['mood']
    reason = request.form['reason']
    
    entry = {
        'name': name,
        'mood': mood.lower(),
        'reason': reason
    }
    mood_logs.append(entry)

    return redirect(url_for('thank_you', name=name))

@app.route('/thank-you/<name>')
def thank_you(name):
    return f"<h3>Thank you, {name}. Your mood has been logged.</h3>"

@app.route('/logs')
def mood_logs_view():
    mood_filter = request.args.get('mood')
    if mood_filter:
        filtered = [entry for entry in mood_logs if entry['mood'] == mood_filter.lower()]
    else:
        filtered = mood_logs
    return render_template('mood_logs.html', entries=filtered, filter=mood_filter)

if __name__ == '__main__':
    app.run(debug=True)

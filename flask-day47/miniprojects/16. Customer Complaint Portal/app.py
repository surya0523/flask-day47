from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

complaints = []

@app.route('/complaint', methods=['GET'])
def complaint_form():
    return render_template('complaint_form.html')

@app.route('/complaint-submit', methods=['POST'])
def complaint_submit():
    name = request.form['name']
    issue = request.form['issue']
    urgency = request.form['urgency'].lower()

    complaints.append({
        'name': name,
        'issue': issue,
        'urgency': urgency
    })

    return redirect(url_for('complaint_status', name=name))

@app.route('/complaint-status/<name>')
def complaint_status(name):
    user_complaints = [c for c in complaints if c['name'].lower() == name.lower()]
    if user_complaints:
        html = f"<h3>Complaints for {name}:</h3><ul>"
        for c in user_complaints:
            html += f"<li>Issue: {c['issue']} - Urgency: {c['urgency'].capitalize()}</li>"
        html += "</ul>"
        return html
    return f"<h3>No complaints found for {name}.</h3>"

@app.route('/complaints')
def complaints_list():
    urgency_filter = request.args.get('urgency')
    if urgency_filter:
        filtered = [c for c in complaints if c['urgency'] == urgency_filter.lower()]
    else:
        filtered = complaints
    return render_template('complaints.html', complaints=filtered, urgency=urgency_filter)

if __name__ == '__main__':
    app.run(debug=True)

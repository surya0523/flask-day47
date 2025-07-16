from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory bug list
bug_reports = []
bug_id_counter = 1

@app.route('/report', methods=['GET'])
def report_form():
    return render_template('report.html')

@app.route('/submit-report', methods=['POST'])
def submit_report():
    global bug_id_counter
    title = request.form['title']
    description = request.form['description']
    priority = request.form['priority']
    
    bug = {
        'id': bug_id_counter,
        'title': title,
        'description': description,
        'priority': priority
    }
    bug_reports.append(bug)
    bug_id_counter += 1

    return redirect(url_for('report_confirm'))

@app.route('/report-confirm')
def report_confirm():
    return "<h3>Thank you! Your bug report has been submitted.</h3>"

@app.route('/bugs')
def view_bugs():
    priority_filter = request.args.get('priority')
    if priority_filter:
        filtered = [b for b in bug_reports if b['priority'].lower() == priority_filter.lower()]
    else:
        filtered = bug_reports
    return render_template('bugs.html', bugs=filtered, priority=priority_filter)

@app.route('/bug/<int:id>')
def bug_detail(id):
    bug = next((b for b in bug_reports if b['id'] == id), None)
    if bug:
        return render_template('bug_detail.html', bug=bug)
    return "<h3>Bug not found.</h3>", 404

if __name__ == '__main__':
    app.run(debug=True)

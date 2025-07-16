from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory store for applications (use SQLite in production)
applications = []

# 1. Show job application form
@app.route('/apply')
def apply():
    return render_template('apply.html')

# 2. Handle form submission and redirect to status
@app.route('/submit-application', methods=['POST'])
def submit_application():
    name = request.form.get('name')
    email = request.form.get('email')
    position = request.form.get('position')

    if not name or not email or not position:
        return "All fields are required.", 400

    # Save application
    applications.append({
        'name': name,
        'email': email,
        'position': position
    })

    return redirect(url_for('application_status'))

# 3. Application status confirmation
@app.route('/application-status')
def application_status():
    return render_template('status.html')

# 4. Filter applications by position
@app.route('/applications')
def view_applications():
    position = request.args.get('position')
    if position:
        filtered = [app for app in applications if app['position'].lower() == position.lower()]
    else:
        filtered = applications
    return render_template('applications.html', applications=filtered, position=position)

# 5. Dynamic route for applicant
@app.route('/applicant/<name>')
def applicant_detail(name):
    applicant_data = [app for app in applications if app['name'].lower() == name.lower()]
    return render_template('applicant.html', name=name, applications=applicant_data)

if __name__ == '__main__':
    app.run(debug=True)

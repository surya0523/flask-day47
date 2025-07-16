from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

courses_data = [
    {"code": "CS101", "name": "Intro to Computer Science", "dept": "CS"},
    {"code": "CS201", "name": "Data Structures", "dept": "CS"},
    {"code": "EE101", "name": "Circuits", "dept": "EE"},
    {"code": "ME101", "name": "Thermodynamics", "dept": "ME"},
]

@app.route('/courses')
def course_list():
    dept = request.args.get('dept')
    if dept:
        filtered = [c for c in courses_data if c["dept"].lower() == dept.lower()]
    else:
        filtered = courses_data
    return render_template('courses.html', courses=filtered, dept=dept)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        student = request.form['student']
        course = request.form['course']
        print(f"{student} registered for {course}")
        return redirect(url_for('confirm', name=student))
    return render_template('register.html', courses=courses_data)

@app.route('/confirm-registration/<name>')
def confirm(name):
    return f"<h3>Thank you {name}, your registration has been received.</h3>"

if __name__ == '__main__':
    app.run(debug=True)

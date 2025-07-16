from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

certificates = []

@app.route('/quiz-form', methods=['GET', 'POST'])
def quiz_form():
    if request.method == 'POST':
        name = request.form['name']
        score = int(request.form['score'])
        certificates.append({'name': name, 'score': score})
        return redirect(url_for('certificate', name=name, score=score))
    return render_template('quiz_form.html')

@app.route('/certificate/<name>/<int:score>')
def certificate(name, score):
    return render_template('certificate.html', name=name, score=score)

@app.route('/certificates')
def certificates_list():
    score_filter = request.args.get('score')
    if score_filter:
        filtered = [c for c in certificates if c['score'] == int(score_filter)]
    else:
        filtered = certificates
    return render_template('certificates.html', certificates=filtered, score_filter=score_filter)

if __name__ == '__main__':
    app.run(debug=True)

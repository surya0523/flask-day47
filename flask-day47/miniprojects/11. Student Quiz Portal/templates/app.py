from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory quiz results
quiz_results = []

# Answer key
correct_answers = {
    "q1": "B",
    "q2": "C",
    "q3": "A"
}

@app.route('/quiz', methods=['GET'])
def quiz():
    return render_template('quiz.html')

@app.route('/quiz-result', methods=['POST'])
def quiz_result():
    name = request.form['name']
    score = 0
    answers = {}

    for q in ['q1', 'q2', 'q3']:
        answers[q] = request.form.get(q)
        if answers[q] == correct_answers[q]:
            score += 1

    quiz_results.append({
        'name': name,
        'answers': answers,
        'score': score
    })

    return redirect(url_for('quiz_summary', name=name))

@app.route('/quiz-summary/<name>')
def quiz_summary(name):
    result = next((r for r in quiz_results if r['name'] == name), None)
    if result:
        return render_template('quiz_summary.html', result=result)
    return f"<h3>No quiz data found for {name}</h3>"

@app.route('/leaderboard')
def leaderboard():
    score_filter = request.args.get('score')
    if score_filter:
        filtered = [r for r in quiz_results if str(r['score']) == score_filter]
    else:
        filtered = quiz_results
    return render_template('leaderboard.html', results=filtered, score_filter=score_filter)

if __name__ == '__main__':
    app.run(debug=True)

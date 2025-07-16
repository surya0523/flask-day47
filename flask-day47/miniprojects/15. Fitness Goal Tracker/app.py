from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

fitness_goals = []

@app.route('/goal', methods=['GET'])
def goal_form():
    return render_template('goal_form.html')

@app.route('/goal-submit', methods=['POST'])
def goal_submit():
    name = request.form['name']
    goal = request.form['goal'].lower()

    fitness_goals.append({
        'name': name,
        'goal': goal
    })
    return redirect(url_for('goal_status', name=name))

@app.route('/goal-status/<name>')
def goal_status(name):
    user_goal = next((g for g in fitness_goals if g['name'].lower() == name.lower()), None)
    if user_goal:
        return f"<h3>{user_goal['name']}, your fitness goal is: {user_goal['goal'].capitalize()}</h3>"
    else:
        return f"<h3>No goal found for {name}.</h3>"

@app.route('/goals')
def goals_list():
    goal_type = request.args.get('type')
    if goal_type:
        filtered = [g for g in fitness_goals if goal_type.lower() in g['goal']]
    else:
        filtered = fitness_goals
    return render_template('goals.html', goals=filtered, goal_type=goal_type)

if __name__ == '__main__':
    app.run(debug=True)

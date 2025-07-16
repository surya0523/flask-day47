from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

votes = {}

@app.route('/poll')
def poll():
    return render_template('poll.html')  # Load from templates folder

@app.route('/vote', methods=['POST'])
def vote():
    name = request.form['name']
    option = request.form['option']
    votes[name] = option
    return redirect(url_for('result', option=option))

@app.route('/result')
def result():
    selected_option = request.args.get('option')
    count = sum(1 for v in votes.values() if v == selected_option)
    return f"<h3>Total votes for option {selected_option}: {count}</h3>"

@app.route('/voter/<name>')
def voter(name):
    vote = votes.get(name, 'No vote found')
    return f"<h3>{name} voted for: {vote}</h3>"

if __name__ == '__main__':
    app.run(debug=True)

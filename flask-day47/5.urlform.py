from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

# Simulated login status
is_logged_in = False

# 1. Redirect from /start to /home
@app.route('/start')
def start():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return "<h2>Welcome to the Home Page!</h2>"

# 2. Dashboard that redirects to /login if not logged in
@app.route('/dashboard')
def dashboard():
    if not is_logged_in:
        return redirect(url_for('login'))
    return "<h2>Welcome to your Dashboard!</h2>"

@app.route('/login')
def login():
    return "<h2>Please log in first.</h2>"

# 3. Dynamic URL building in HTML (profile page)
@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", username=username)

# 4. Page with HTML links generated via url_for
@app.route('/links')
def links():
    home_url = url_for('home')
    profile_url = url_for('profile', username='mahesh')
    dashboard_url = url_for('dashboard')

    return render_template("links.html", home_url=home_url, profile_url=profile_url, dashboard_url=dashboard_url)

# 5. Form submission that redirects to /thankyou
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return redirect(url_for('thankyou'))
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            <button type="submit">Submit</button>
        </form>
    '''

@app.route('/thankyou')
def thankyou():
    return "<h2>Thank you! Your form has been submitted.</h2>"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request , render_template

app = Flask(__name__)

# Task 1: /search?keyword=flask
@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    return f"Search keyword: {keyword}" if keyword else "No keyword provided."

# Task 2: /filter?type=shirt&color=blue&size=M
@app.route('/filter')
def filter_items():
    item_type = request.args.get('type')
    color = request.args.get('color')
    size = request.args.get('size')
    return f"Filtering: Type={item_type}, Color={color}, Size={size}"

# Task 3: Return “No keyword found” if missing
@app.route('/safe-search')
def safe_search():
    if 'keyword' in request.args:
        return f"Keyword: {request.args['keyword']}"
    return "No keyword found."

# Task 4: Loop through all query parameters and return in list
@app.route('/params-list')
def params_list():
    if not request.args:
        return "No query parameters passed."
    items = "".join(f"<li>{key} = {value}</li>" for key, value in request.args.items())
    return f"<h3>Query Parameters</h3><ul>{items}</ul>"

# Task 5: /greet?name=John
@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    return f"Hello, {name}!"

# Task 6: /profile?mode=admin (optional)
@app.route('/profile')
def profile():
    mode = request.args.get('mode', 'user')
    return f"Profile page in {mode} mode."

# Task 7: Show how many query parameters were passed
@app.route('/count-params')
def count_params():
    count = len(request.args)
    return f"Number of query parameters: {count}"

# Task 8: Format query params into HTML table
@app.route('/show-table')
def show_table():
    if not request.args:
        return "No data to show."
    table = "<table border=1><tr><th>Key</th><th>Value</th></tr>"
    for key, value in request.args.items():
        table += f"<tr><td>{key}</td><td>{value}</td></tr>"
    table += "</table>"
    return table

# Task 9: /toggle?debug=true
@app.route('/toggle')
def toggle():
    debug = request.args.get('debug')
    if debug == 'true':
        return "Debug mode is ON"
    return "Debug mode is OFF"

# Task 10: /display/<section>?lang=english
@app.route('/display/<section>')
def display(section):
    lang = request.args.get('lang', 'en')
    return f"Section: {section}<br>Language: {lang}"

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def home():
    return render_template('query.html')



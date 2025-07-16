from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

ratings = []

# Sample movie info
movies = {
    "Inception": {
        "director": "Christopher Nolan",
        "year": 2010,
        "genre": "Sci-Fi/Thriller",
        "desc": "A thief who steals corporate secrets through dream-sharing technology."
    },
    "Titanic": {
        "director": "James Cameron",
        "year": 1997,
        "genre": "Romance/Drama",
        "desc": "A love story aboard the ill-fated RMS Titanic."
    },
}

@app.route('/rate', methods=['GET'])
def rate_form():
    return render_template('rate_form.html')

@app.route('/submit-rating', methods=['POST'])
def submit_rating():
    name = request.form['name']
    movie = request.form['movie'].strip()
    rating = int(request.form['rating'])

    ratings.append({
        'name': name,
        'movie': movie,
        'rating': rating
    })

    return redirect(url_for('thank_you', name=name))

@app.route('/thank-you/<name>')
def thank_you(name):
    return f"<h3>Thank you, {name}, for your rating!</h3>"

@app.route('/ratings')
def ratings_list():
    movie_filter = request.args.get('movie')
    if movie_filter:
        filtered = [r for r in ratings if r['movie'].lower() == movie_filter.lower()]
    else:
        filtered = ratings
    return render_template('ratings.html', ratings=filtered, movie_filter=movie_filter)

@app.route('/movie/<title>')
def movie_info(title):
    movie = movies.get(title)
    if movie:
        return render_template('movie_info.html', title=title, movie=movie)
    else:
        return f"<h3>No information found for movie: {title}</h3>", 404

if __name__ == '__main__':
    app.run(debug=True)

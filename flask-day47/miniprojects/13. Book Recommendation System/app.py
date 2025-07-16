from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Sample book data
books = [
    {"title": "Dune", "genre": "sci-fi", "author": "Frank Herbert", "desc": "Epic sci-fi adventure on desert planet."},
    {"title": "Neuromancer", "genre": "sci-fi", "author": "William Gibson", "desc": "Cyberpunk classic about AI and hackers."},
    {"title": "Pride and Prejudice", "genre": "romance", "author": "Jane Austen", "desc": "Classic love story in English countryside."},
    {"title": "The Notebook", "genre": "romance", "author": "Nicholas Sparks", "desc": "Heartfelt tale of enduring love."},
]

@app.route('/recommend', methods=['GET'])
def recommend():
    return render_template('recommend.html')

@app.route('/show-recommendation', methods=['POST'])
def show_recommendation():
    user = request.form['user']
    genre = request.form['genre']
    # Filter books by genre
    recs = [b for b in books if b['genre'] == genre]
    return render_template('show_recommendation.html', user=user, books=recs, genre=genre)

@app.route('/thanks/<user>')
def thanks(user):
    return f"<h3>Thanks for your interest, {user}!</h3>"

@app.route('/books')
def books_list():
    genre = request.args.get('genre')
    if genre:
        filtered = [b for b in books if b['genre'] == genre]
    else:
        filtered = books
    return render_template('books.html', books=filtered, genre=genre)

@app.route('/book/<title>')
def book_detail(title):
    book = next((b for b in books if b['title'].lower() == title.lower()), None)
    if book:
        return render_template('book_detail.html', book=book)
    return "<h3>Book not found.</h3>", 404

if __name__ == '__main__':
    app.run(debug=True)

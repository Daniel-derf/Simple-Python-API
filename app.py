from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'O Senhor dos Anéis',
        'author': "J.R.R. Tolkien"
    },
    {
        'id': 2,
        'title': 'O Senhor dos Anéis 2',
        'author': "J.R.R. Tolkien"
    },
    {
        'id': 3,
        'title': 'O Senhor dos Anéis 3',
        'author': "J.R.R. Tolkien"
    },
]

@app.route('/books')
def get_books():
    return jsonify(books)


app.run(port=5000, host='localhost', debug=True)
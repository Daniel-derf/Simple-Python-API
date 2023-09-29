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

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)


@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_by_id(id):
    edited_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(edited_book)
            return jsonify(books[index])


@app.route('/books', methods=['POST'])
def create_new_book():
    new_book = request.get_json()
    books.append(new_book)

    return jsonify(books)
    

app.run(port=5000, host='localhost', debug=True)
from flask import Flask, request, jsonify


app = Flask(__name__)

books_list=[
     {
         'id':0,
         "author":"chinua achebe",
         "language":"english",
         "title":"things fall apart",
     },
     {
         'id': 1,
         "author": "hans christian andersen",
         "language": "danish",
         "title": "fairy tales",
     },
     {
         'id': 2,
         "author": "samuel beckett",
         "language": "french,english",
         "title": "molloy,malone dies,the unnamable,the triology",
     },
     {
         'id': 6,
         "author": "jorge luis borges",
         "language": "spanish",
         "title": "ficciones",
     },
     {
         'id': 3,
         "author": "giovanni boccaccio",
         "language": "italian",
         "title": "the decameron",
     },
     {
         'id': 5,
         "author": "emily bront",
         "language": "english",
         "title": "wuthering heights",
     },
 ]

@app.route('/books',methods=["GET","POST"])
def books():
    if request.method == "GET":
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            'Nothing Found',404

    if request.method == "POST":
        author = request.form.get('author')
        language = request.form.get('language')
        title = request.form.get('title')
        id = books_list[-1]['id'] + 1

        new_object = {"id":id,
                      "author": author,
                      "language":language,
                      "title":title,
                      }

        books_list.append(new_object)
        return jsonify(books_list),201


@app.route('/book/<int:id>',methods=["GET","PUT","DELETE"])
def single_book(id):
    if request.method == "GET":
        for book in books_list:
            if book["id"] == id:
                return jsonify(book)
            pass
    
    if request.method == "PUT":
        for book in books_list:
            if book["id"] == id:
                updated_book_data = {
                    "id":id,
                    "author": request.form.get("author"),
                    "language": request.form.get("language"),
                    "title":request.form.get("title")
                    }
                return jsonify(updated_book_data)
    
    if request.method == "DELETE":
        for index, book in enumerate(books_list):
            if book["id"] == id:
                books_list.pop(index)
                return jsonify(books_list)

if __name__ == "__main__":
    app.run()
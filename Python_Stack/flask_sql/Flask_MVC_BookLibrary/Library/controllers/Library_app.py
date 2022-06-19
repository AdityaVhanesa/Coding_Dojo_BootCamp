from flask import render_template, redirect, request

from Library import app
from Library.models.authors import Author


@app.route("/")
def home():
    return redirect("/authors")


@app.route("/authors")
def authorView():
    authorsList = Author.getAll()
    return render_template('author.html', authors=authorsList)


@app.route("/author_create", methods=["POST"])
def createAuthor():
    data = {
        "name": request.form.get("author_name")
    }
    Author.save(data)
    return redirect("/authors")


@app.route("/authors/<int:author_id>")
def authorDetailView(author_id):
    authorDetails = Author.getAllBooks({"id": author_id})
    print(authorDetails.books)
    return redirect("/")

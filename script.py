from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/start")
def start():
    return "I got it"

@app.route("/book/<path:book_title>")
def book(book_title):
    return f"Eu vou buscar um livro! com o nome de: { book_title }  "


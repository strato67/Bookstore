from flask import Blueprint,render_template
from flask_login import login_required, current_user
from .models import Book

views = Blueprint('views',__name__)

@views.route('/')

def home():
    books= Book.query.all()
    return render_template("index.html",user=current_user,books=books)

@views.route("book_info/<int:book_id>")
def book_info(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_info.html', title=book.title, book=book, user=current_user)

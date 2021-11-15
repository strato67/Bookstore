from flask import Blueprint,render_template
from flask_login import login_required, current_user
from .models import Book

views = Blueprint('views',__name__)

@views.route('/')

def home():
    books= Book.query.all()
    return render_template("index.html",user=current_user,books=books)
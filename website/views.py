import json
from flask import Blueprint,render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .models import User,Book, Cart, Genre,Order,OrderBook,Review
from .api import infoQuery
from datetime import date

import json

views = Blueprint('views',__name__)

@views.route('/')

def home():
    booksJOINgenre =  db.session.query(Book,Genre).select_from(Book).join(Genre).all()
    
    return render_template("index.html",user=current_user,combine=booksJOINgenre)

# book info rediect 
@views.route("book_info/<int:book_id>", methods=['GET','POST'])
def book_info(book_id):
    book = Book.query.get_or_404(book_id)
    bookinfoQuery = json.loads(infoQuery.info(book.title))
    
    commentlist = Review.query.filter(Review.bookid == book_id).all()
    if request.method == 'POST':
        comment = request.form.get('comment')
        if len(comment) < 1:
            flash('Comment is too short' ,category='error')
        else:
            newComment = Review(data=comment, date = date.today(),user_id=current_user.id, bookid=book_id)
            db.session.add(newComment)
            db.session.commit()
            flash('Comment added.', category='success')

    return render_template('book_info.html', title=book.title, book=book, user=current_user, info = bookinfoQuery["description"], commentList = commentlist)


#######################
# cart redirect
@views.route("/cart")
def cart():
    carts=Cart.query.filter_by(user_id=current_user.id).all()
    sum=0
    for cart in carts:
        sum=sum+cart.cartbook.price
    return render_template('cart.html', title="cart",carts=carts,total=sum,user=current_user)   

# Addbooks to cart
@views.route("/addcart/<int:book_id>")
def addcart(book_id):
    if current_user.is_authenticated:
        book = Book.query.get_or_404(book_id)
        cart=Cart(user_id=current_user.id,book_id=book_id)
        db.session.add(cart)
        db.session.commit()
        flash('Book added successfully', 'success')
        return redirect(url_for('views.cart'))
    else:
        flash('Login to add this book to your cart.', 'error')
        return redirect(url_for('auth.login'))

# Delete books from cart
@views.route("/cart/<int:cart_id>/delete_cart", methods=['POST'])
@login_required
def delete_cart(cart_id):
    if current_user.is_authenticated:
        cart = Cart.query.get_or_404(cart_id)
        db.session.delete(cart)
        db.session.commit()
        flash('Book  has been deleted from Cart!', 'success')
        return redirect(url_for('views.cart'))

# Checkout Cart
@views.route("/checkout")
def checkout():
    carts=Cart.query.filter_by(user_id=current_user.id).all()
    c=Cart.query.filter_by(user_id=current_user.id).first()
    sum=0
    for cart in carts:
        sum=sum+cart.cartbook.price
    return render_template('checkout.html', title="checkout",carts=carts,total=sum, user=current_user) 


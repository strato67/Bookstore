from flask import Blueprint,render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import User,Book, Cart, Genre,Order,OrderBook

views = Blueprint('views',__name__)

@views.route('/')

def home():
    books= Book.query.all()
    #genre = Book.query.filter_by(title="The Catcher in the Rye").all()
    #genre = Genre.query.all()
    genre =  db.session.query(Genre.id,Genre.genre_name).select_from(Book).join(Genre, Genre.id == Book.genre_id).all()
    print(genre)
    return render_template("index.html",user=current_user,books=books,genres=genre)


# book info rediect 
@views.route("book_info/<int:book_id>")
def book_info(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_info.html', title=book.title, book=book, user=current_user)


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
    if (c.reader.address is None) and (c.reader.state is None) and (c.reader.pincode is None):
        flash('Add Address to Order Book', 'danger')
        return redirect(url_for('account'))
    return render_template('checkout.html', title="checkout",carts=carts,total=sum) 


from flask import Blueprint,render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
        
    return render_template("login.html")

@auth.route('/signup',methods=['GET','POST'])
def signup():

    if request.method=='POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        password1 = request.form.get('confirmpassword')
        address = request.form.get('address')
        phone = request.form.get('phone')
        
        if password != password1:
            flash('Passwords do not match',category='error')
        else:
            new_user = User(email=email, first_name= first_name,last_name = last_name, address = address, phone = phone, password=generate_password_hash(
            password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))


    return render_template("signup.html")
from os import error
from flask import Blueprint,render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
        
    return render_template("login.html")

@auth.route('/signup',methods=['GET','POST'])
def signup():

    if request.method=='POST':
        firstname = request.form.get('first_name')
        lastname = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        password1 = request.form.get('confirmpassword')
        address = request.form.get('address')
        phone = request.form.get('phone')
        
        if password != password1:
            flash('Passwords do not match',category='error')
        else:
            flash('Hello',category='success')


    return render_template("signup.html")
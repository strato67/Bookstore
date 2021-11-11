from logging import debug
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../Bookstore/bookstoreDB.db'
app.config['SECRET_KEY'] = 'password'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    return render_template("login.html")


@app.route('/signup', methods=["POST", "GET"])
def signup():
    return render_template("signup.html")




if __name__ == "__main__":
    app.run(debug==True)
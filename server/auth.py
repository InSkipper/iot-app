from . import db
from .models import User

from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again.")
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.devices'))


@auth.route("/signup", methods=['GET'])
def signup():
    return render_template('signup.html')


@auth.route("/signup", methods=['POST'])
def signup_post():
    email = request.form.get("email")
    user_login = request.form.get("login")
    password = request.form.get("password")
    password_conf = request.form.get("password_conf")

    if password != password_conf:
        flash('Please confirm your password')
        return redirect(url_for("auth.signup"))

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email already exist')
        return redirect(url_for("auth.signup"))

    new_user = User(email=email, login=user_login, password=generate_password_hash(password, 'sha256'))
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user, remember=True)
    return redirect(url_for("main.devices"))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

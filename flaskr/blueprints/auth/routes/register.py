from flask import render_template, redirect, url_for, flash, request
from flaskr.blueprints.auth import auth
from flaskr.models.user import User
from flaskr import db
from flask_wtf.csrf import generate_csrf
import logging

logger = logging.getLogger(__name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    csrf_token = generate_csrf()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        logger.info(f"Attempting to register user: {username}")

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            logger.error("Passwords do not match.")
            return redirect(url_for('auth.register'))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user is None:
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            logger.info(f"User {username} registered successfully.")
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Username already exists.', 'danger')
            logger.error(f"Username {username} already exists.")

    return render_template('register.html', csrf_token=csrf_token)

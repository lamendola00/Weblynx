from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user
from flaskr.blueprints.auth import auth
from flaskr.models.user import User
from flask_wtf.csrf import generate_csrf
import logging

logger = logging.getLogger(__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    csrf_token = generate_csrf()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        logger.info(f"Attempting login for user: {username}")

        user = User.query.filter_by(username=username).first()

        if user:
            if user.check_password(password):
                login_user(user)
                logger.info(f"User {username} logged in successfully.")
                flash('Login successful!', 'success')
                next_page = request.args.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect(url_for('link.show_all'))
            else:
                flash('Incorrect password.', 'danger')
                logger.warning(f"Failed login attempt for user {username}: incorrect password.")
        else:
            flash('Username does not exist.', 'danger')
            logger.warning(f"Failed login attempt for non-existing user: {username}")

    return render_template('login.html', csrf_token=csrf_token)

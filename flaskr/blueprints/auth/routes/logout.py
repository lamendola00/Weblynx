from flask import redirect, url_for, flash
from flask_login import logout_user
from flaskr.blueprints.auth import auth

@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.choose'))

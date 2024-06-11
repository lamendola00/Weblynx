from flask import render_template, redirect, url_for, request, flash, session
from flask_login import current_user, login_required
from flaskr.blueprints.auth import auth
from flaskr import db

@auth.route('/user_settings', methods=['GET', 'POST'])
@login_required
def user_settings():
    print(session)
    if request.method == 'POST':
        # Ottieni i nuovi dati dal form
        new_username = request.form.get('username')
        new_password = request.form.get('password')

        # Aggiorna i dati dell'utente
        if new_username:
            current_user.username = new_username
        if new_password:
            current_user.set_password(new_password)  # Assicurati che questo metodo esista nel modello User

        # Salva le modifiche
        db.session.commit()
        flash('User settings updated successfully!', 'success')
        return redirect(url_for('auth.user_settings'))

    return render_template('user_settings.html', user=current_user)

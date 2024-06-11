from flask import render_template
from flaskr.blueprints.auth import auth

@auth.route('/choose', methods=['GET'])
def choose():
    return render_template('choose.html')

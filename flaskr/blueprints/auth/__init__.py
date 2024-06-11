from flask import Blueprint

auth = Blueprint(
    'auth',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/auth'
)

# Inizializzazione del login_manager
from flask_login import LoginManager
login_manager = LoginManager()

def init_login_manager(app):
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        from flaskr.models.user import User
        return User.query.get(int(user_id))

# Importa le rotte del blueprint auth
from .routes import login, register, choose, user_settings, logout

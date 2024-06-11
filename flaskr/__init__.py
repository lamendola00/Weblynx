from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import logging
from flaskr.config import Config
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, current_user

# Inizializza le estensioni
db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Rotta per la pagina di login

# Configura il logging
logging.basicConfig(
    filename='weblynx.log', 
    format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(filename)s -> %(funcName)s:%(lineno)d - %(message)s',
    level=logging.INFO, 
    datefmt='%Y-%m-%d %H:%M:%S'
)

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['STATIC_FOLDER'] = 'static'
    app.config.from_object(Config)

    # Inizializza le estensioni
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)  # Inizializza Flask-Login

    @app.after_request
    def set_security_headers(response):
        # Prevents clickjacking
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        
        # Enforces HTTPS by redirecting HTTP requests
        response.headers['Strict-Transport-Security'] = "max-age=63072000; includeSubdomains; preload"
        
        # Prevents MIME type sniffing
        response.headers['X-Content-Type-Options'] = 'nosniff'
        
        # Controls the information sent in the Referer header
        response.headers['Referrer-Policy'] = 'strict-origin'
        
        # Sets policies for loading resources from different origins
        response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
        response.headers['Cross-Origin-Resource-Policy'] = 'same-origin'
        
        # XSS Protection
        response.headers['X-XSS-Protection'] = "1; mode=block"

        # Content Security Policy
        response.headers['Content-Security-Policy'] = (
            "default-src 'self'; "
            "img-src 'self' data:; "
            "script-src 'self' 'unsafe-inline'; "
            "style-src 'self' 'unsafe-inline'; "
            "font-src 'self';"
        )
        return response

    from flaskr.blueprints.link import link
    from flaskr.blueprints.auth import auth, init_login_manager

    app.register_blueprint(link)
    app.register_blueprint(auth)

    # Configura il user_loader dopo l'inizializzazione dell'app
    init_login_manager(app)

    with app.app_context():
        # Importa tutti i modelli prima di chiamare create_all
        from flaskr.models.user import User
        from flaskr.models.link import Link
        from flaskr.models.tag import Tag
        from flaskr.models.linktag import LinkTag
        db.create_all()  # Crea tutte le tabelle se non esistono

    @app.route('/', methods=['GET'])
    def index():
        if current_user.is_authenticated:
            return redirect(url_for('link.show_all'))  # Redirige alla pagina principale per utenti autenticati
        return redirect(url_for('auth.choose'))  # Redirige alla pagina di scelta login/registrazione

    return app

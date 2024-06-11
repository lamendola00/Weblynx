from flask import Blueprint


link = Blueprint(
    'link',
    __name__,
    template_folder='templates/link',
    static_folder='static',
    url_prefix='/link')

from flaskr.blueprints.link.routes import *
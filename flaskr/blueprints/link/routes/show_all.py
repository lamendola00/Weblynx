from flask import render_template, request, redirect, url_for, session
from flask_login import login_required
from flaskr.models.link import Link
from flaskr.models.tag import Tag
from flaskr.blueprints.link import link

@link.route('/')
@login_required  # Protegge la rotta, richiede login
def show_all():
    links = Link.query.all()
    tags = Tag.query.all()
    #print(session)
    return render_template('index.html', links=links, tags=tags)

@link.route('/filter')
@login_required  # Protegge la rotta, richiede login
def filter_by_tag():
    tag_id = request.args.get('tag_id')
    if tag_id:
        links = Link.query.join(Link.tags).filter(Tag.id == tag_id).all()
        tags = Tag.query.all()
        return render_template('index.html', links=links, tags=tags)
    else:
        return redirect(url_for('link.show_all'))

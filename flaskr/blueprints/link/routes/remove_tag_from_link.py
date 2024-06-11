from flask import redirect, url_for, flash
from flaskr.models.link import Link
from flaskr.models.tag import Tag
from flaskr import db
from flaskr.blueprints.link import link

@link.route('/remove_tag/<int:link_id>/<int:tag_id>', methods=['POST'])
def remove_tag_from_link(link_id, tag_id):
    link = Link.query.get_or_404(link_id)
    tag = Tag.query.get_or_404(tag_id)

    if tag in link.tags:
        link.tags.remove(tag)
        db.session.commit()
        flash('Tag rimosso con successo dal link!', 'success')
    else:
        flash('Il tag non è associato al link.', 'error')

    return redirect(url_for('link.detail_link', link_id=link_id))

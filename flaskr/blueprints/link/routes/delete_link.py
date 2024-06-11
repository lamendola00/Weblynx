from flask import render_template, redirect, request, url_for, flash
from flaskr.models.link import Link
from flaskr.models.tag import Tag
from flaskr.models.linktag import LinkTag
from flaskr.blueprints.link import link
from flaskr import db
from flask_wtf.csrf import generate_csrf

@link.route('/delete_link', methods=['GET', 'POST'])
def delete_link():
    links = Link.query.all()
    
    if request.method == 'POST':
        if 'cancel' in request.form:
            return redirect(url_for('link.show_all'))

        link_id = request.form.get('link_id')
        
        if not link_id:
            flash('No link selected for deletion.', 'warning')
            return redirect(url_for('link.delete_link'))

        link_to_delete = Link.query.get(link_id)

        if not link_to_delete:
            flash('Link not found.', 'danger')
            return redirect(url_for('link.delete_link'))

        try:
            # Remove associations between link and tags
            LinkTag.query.filter_by(link_id=link_id).delete()
            db.session.commit()
            
            # Now delete the link
            db.session.delete(link_to_delete)
            db.session.commit()
            flash('Link deleted successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error deleting link: {e}', 'danger')
        return redirect(url_for('link.show_all'))

    csrf_token = generate_csrf()  # Genera correttamente il token CSRF
    return render_template('delete_link.html', links=links, tags=Tag.query.all(), csrf_token=csrf_token)

@link.route('/delete_tag', methods=['GET', 'POST'])
def delete_tag():
    tags = Tag.query.all()
    
    if request.method == 'POST':
        if 'cancel' in request.form:
            return redirect(url_for('link.show_all'))

        tag_id = request.form.get('tag_id')

        if not tag_id:
            flash('No tag selected for deletion.', 'warning')
            return redirect(url_for('link.delete_tag'))

        tag_to_delete = Tag.query.get(tag_id)

        if not tag_to_delete:
            flash('Tag not found.', 'danger')
            return redirect(url_for('link.delete_tag'))

        try:
            # Remove associations between tag and links
            LinkTag.query.filter_by(tag_id=tag_id).delete()
            db.session.commit()

            # Now delete the tag
            db.session.delete(tag_to_delete)
            db.session.commit()
            flash('Tag deleted successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error deleting tag: {e}', 'danger')
        return redirect(url_for('link.show_all'))

    csrf_token = generate_csrf()  # Genera correttamente il token CSRF
    return render_template('delete_link.html', links=Link.query.all(), tags=tags, csrf_token=csrf_token)

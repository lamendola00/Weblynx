from flask import render_template, redirect, request, url_for, flash, jsonify
from flask_login import login_required, current_user
from flaskr.models.link import Link
from flaskr.models.tag import Tag
from flaskr.blueprints.link import link
from flaskr import db
import base64
from PIL import Image
from io import BytesIO
import concurrent.futures
from flask_wtf.csrf import generate_csrf
from datetime import datetime

def resize_and_encode_image(image):
    img_resized = image.copy()
    img_resized.thumbnail((200, 200), Image.ANTIALIAS)
    buffer_resized = BytesIO()
    img_resized.save(buffer_resized, format="JPEG")
    image_data = base64.b64encode(buffer_resized.getvalue()).decode('utf-8')
    return image_data

@link.route('/detail/<int:link_id>', methods=['GET', 'POST'])
@login_required  # Protegge la rotta, richiede login
def detail_link(link_id):
    link = Link.query.get_or_404(link_id)
    tags = Tag.query.all()
    csrf_token = generate_csrf()  # Genera il token CSRF
    if request.method == 'POST':
        # Aggiornamento dei campi URL e descrizione
        link.url = request.form['url']
        link.description = request.form['description']
        link.modified_by = current_user.id  # Imposta l'utente che modifica con il suo ID
        link.modified_at = datetime.utcnow()  # Imposta la data di modifica

        # Gestione dell'immagine
        new_image = request.files.get('image_original')
        if new_image:
            img_original = Image.open(new_image)
            img_original = img_original.convert("RGB")

            buffer_original = BytesIO()
            img_original.save(buffer_original, format="JPEG")
            new_image_original_data = base64.b64encode(buffer_original.getvalue()).decode('utf-8')
            link.image_original = new_image_original_data

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(resize_and_encode_image, img_original)
                new_image_resized_data = future.result()

            link.image_resized = new_image_resized_data

        # Gestione dei nuovi tag
        new_tags = request.form.get('new_tags')
        if new_tags:
            new_tags = new_tags.split(',')
            for new_tag_name in new_tags:
                new_tag_name = new_tag_name.strip()
                if new_tag_name:
                    existing_tag = Tag.query.filter_by(name=new_tag_name).first()
                    if existing_tag:
                        if existing_tag not in link.tags:
                            link.tags.append(existing_tag)
                    else:
                        new_tag = Tag(name=new_tag_name)
                        db.session.add(new_tag)
                        link.tags.append(new_tag)

        db.session.commit()
        flash('Link updated successfully!', 'success')
        return redirect(url_for('link.show_all'))

    return render_template('detail_link.html', link=link, tags=tags, csrf_token=csrf_token)

@link.route('/add_tag/<int:link_id>', methods=['POST'])
def add_tag(link_id):
    link = Link.query.get_or_404(link_id)
    tag_id = request.form.get('tag_id')
    new_tag_name = request.form.get('new_tag')
    if tag_id:
        try:
            tag_id = int(tag_id)
            tag = Tag.query.get(tag_id)
            if tag and tag not in link.tags:
                link.tags.append(tag)
                db.session.commit()
                return jsonify({'success': True, 'tag': {'id': tag.id, 'name': tag.name}})
            else:
                return jsonify({'success': False, 'message': 'Tag already exists or not found.'})
        except ValueError:
            return jsonify({'success': False, 'message': 'Invalid tag ID.'})
    elif new_tag_name:
        existing_tag = Tag.query.filter_by(name=new_tag_name).first()
        if existing_tag:
            if existing_tag not in link.tags:
                link.tags.append(existing_tag)
                db.session.commit()
                return jsonify({'success': True, 'tag': {'id': existing_tag.id, 'name': existing_tag.name}})
            else:
                return jsonify({'success': False, 'message': 'Tag already exists.'})
        else:
            new_tag = Tag(name=new_tag_name)
            db.session.add(new_tag)
            link.tags.append(new_tag)
            db.session.commit()
            return jsonify({'success': True, 'tag': {'id': new_tag.id, 'name': new_tag.name}})
    else:
        return jsonify({'success': False, 'message': 'No tag selected.'})

@link.route('/remove_tag/<int:link_id>', methods=['POST'])
def remove_tag(link_id):
    link = Link.query.get_or_404(link_id)
    tag_id = request.form.get('tag_id')
    if tag_id:
        try:
            tag_id = int(tag_id)
            tag = Tag.query.get(tag_id)
            if tag and tag in link.tags:
                link.tags.remove(tag)
                db.session.commit()
                return jsonify({'success': True})
            else:
                return jsonify({'success': False, 'message': 'Tag not found or not associated with this link.'})
        except ValueError:
            return jsonify({'success': False, 'message': 'Invalid tag ID.'})
    else:
        return jsonify({'success': False, 'message': 'Tag ID not provided.'})

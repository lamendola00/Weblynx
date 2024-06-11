from flask import render_template, redirect, request, url_for, flash
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

@link.route('/add_link', methods=['GET', 'POST'])
@login_required  # Protegge la rotta, richiede login
def add_link():
    if request.method == 'POST':
        url = request.form['url']
        description = request.form['description']
        tag_ids = request.form.getlist('tag_ids[]')
        new_tags = request.form.getlist('new_tags[]')
        
        # Creazione del nuovo link
        link = Link(
            url=url,
            description=description,
            created_by=current_user.id,  # ID dell'utente loggato
            created_at=datetime.utcnow()
        )
        
        # Aggiunta dei tag esistenti
        for tag_id in tag_ids:
            if tag_id != 'new':
                tag = Tag.query.get(tag_id)
                if tag:
                    link.tags.append(tag)
        
        # Creazione e aggiunta di nuovi tag
        for tag_name in new_tags:
            if tag_name:
                new_tag = Tag(name=tag_name)
                db.session.add(new_tag)
                link.tags.append(new_tag)
        
        # Gestione dell'immagine
        new_image = request.files.get('image')
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

        db.session.add(link)
        db.session.commit()
        flash('Link added successfully!', 'success')
        return redirect(url_for('link.show_all')) 
    
    tags = Tag.query.all()
    csrf_token = generate_csrf()  # Genera il token CSRF
    return render_template('add_link.html', tags=tags, csrf_token=csrf_token)

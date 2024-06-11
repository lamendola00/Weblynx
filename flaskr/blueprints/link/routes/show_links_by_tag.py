from flask import render_template, request, redirect, url_for
from flaskr.models.link import Link
from flaskr.models.tag import Tag
from flaskr.blueprints.link import link

@link.route('/show_links_by_tag', methods=['GET'])
def show_links_by_tag():
    tags = Tag.query.all()
    selected_tag_id = request.args.get('tag_id')
    
    if selected_tag_id:
        if selected_tag_id == "":
            links = Link.query.all()
        else:
            selected_tag = Tag.query.get(selected_tag_id)
            if selected_tag:
                links = selected_tag.links
            else:
                links = []
    else:
        links = Link.query.all()

    return render_template('index.html', links=links, tags=tags)

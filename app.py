from flaskr import create_app

app= create_app()


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()  # Solo se il database non è già stato creato
        app.run(debug=True, port=5000)

from flask import Flask
from models.database import init_db
import models

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.secret_key = 'very_secret_key'
    init_db(app)

    return app

app = create_app()
import view

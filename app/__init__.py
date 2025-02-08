from flask import Flask
from config.database import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.settings.Config')

    # Inicializar la base de datos
    db.init_app(app)

    # Configurar Flask-Migrate
    migrate = Migrate(app, db)

    return app

# Exportar la aplicación Flask
app = create_app()
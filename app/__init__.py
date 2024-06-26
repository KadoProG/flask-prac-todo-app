from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_assets import Environment, Bundle

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Flask-Assetsの設定
    assets = Environment(app)
    scss = Bundle('src/scss/styles.scss', filters='libsass', output='dist/css/styles.css')
    assets.register('scss_all', scss)
    scss.build()

    with app.app_context():
        from app import models
        from app.routes.api import api_bp
        from app.routes.main import main_bp
        app.register_blueprint(main_bp)
        app.register_blueprint(api_bp, url_prefix='/api')
        
        db.create_all()

    return app

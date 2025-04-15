from flask import Flask
from pathlib import Path
from flask_bootstrap import Bootstrap5

from config import config

templates_dir = Path(__file__).resolve().parent / "templates"
bootstrap = Bootstrap5()

def create_app():
    app = Flask(__name__, template_folder=templates_dir)

    app.config.from_object(config)
    bootstrap.init_app(app)

    with app.app_context():
        from flaskTemplate.routes import routes_bp
        app.register_blueprint(routes_bp, url_prefix='/')


    return app


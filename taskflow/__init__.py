from flask import Flask
from config import Config
from taskflow.models import db

def create_app(config_class=Config):
    """Application factory for TaskFlow."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    from taskflow.routes import main_bp
    app.register_blueprint(main_bp)

    # Inject current datetime to all Jinja templates
    from datetime import datetime
    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}

    # Create database tables within the app context
    with app.app_context():
        db.create_all()

    return app

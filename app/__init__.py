import uuid

from flask import Flask
from flask_security import SQLAlchemyUserDatastore, Security, hash_password

from app.models import Role, User, db


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY="dev-secret-key-change-in-production",
        SECURITY_PASSWORD_SALT="dev-salt-change-in-production",
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SECURITY_REGISTERABLE=True,
    )
    if config:
        app.config.update(config)

    db.init_app(app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, user_datastore)

    from app.routes import bp

    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()
        if not user_datastore.find_user(email="admin@example.com"):
            user_datastore.create_user(
                email="admin@example.com",
                password=hash_password("ChangeMe123!"),
                fs_uniquifier=str(uuid.uuid4()),
            )
            db.session.commit()

    return app

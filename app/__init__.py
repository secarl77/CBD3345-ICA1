
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tenacity import retry, stop_after_attempt, wait_fixed

db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)
#     app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@db:5432/postgres"
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#
#     db.init_app(app)
#
#     from .routes import bp
#     app.register_blueprint(bp)
#
#     # These lines create users table
#     #with app.app_context():
#     #    db.create_all()
#
#     return app



@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def try_db_init(app):
    with app.app_context():
        db.create_all()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@db:5432/postgres"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .routes import bp
    app.register_blueprint(bp)

    # Retry if fail
    try_db_init(app)

    return app

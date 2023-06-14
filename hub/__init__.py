from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'W&mm{m4DW+p7CV7Z'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///modules.sqlite'
    # "postgresql://user1:123123123@rc1a-d9c2wi1g9xdvsb8z.mdb.yandexcloud.net:6432/db1"

    db.init_app(app)

    from . import models

    with app.app_context():
        db.create_all()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

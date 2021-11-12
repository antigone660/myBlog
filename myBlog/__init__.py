from logging import basicConfig
from flask import render_template,Flask
import click

import os

from myBlog.setting import BaseConfig
from myBlog.blueprints.admin import admin_bp
from myBlog.blueprints.blog import blog_bp
from myBlog.extensions import bootstrap,db
from myBlog.modles import User

def create_app():
    app = Flask("myBlog")
    app.config.from_object(BaseConfig)
    # app.secret_key = os.getenv("SECRET_KEY")
    register_blueprints(app=app)
    register_extensions(app)
    register_commands(app)
    return app



def register_blueprints(app:Flask):
    app.register_blueprint(blueprint=blog_bp)
    app.register_blueprint(admin_bp)

def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)


def register_commands(app:Flask):
    @app.cli.command()
    def initDB():
        db.create_all()
        click.echo("success")
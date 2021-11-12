from flask import render_template,Flask

import os

from myBlog.blueprints.admin import admin_bp
from myBlog.blueprints.blog import blog_bp
from myBlog.extensions import bootstrap

def create_app():
    app = Flask("myBlog")
    app.secret_key = os.getenv("SECRET_KEY")
    register_blueprints(app=app)
    register_extensions(app)
    return app



def register_blueprints(app:Flask):
    app.register_blueprint(blueprint=blog_bp)
    app.register_blueprint(admin_bp)

def register_extensions(app):
    bootstrap.init_app(app)

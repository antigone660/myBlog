from flask import Blueprint,render_template

blog_bp = Blueprint('blog',__name__)

@blog_bp.route('/',methods=["GET"])
def index():
    return 'hi'


from operator import pos
import re
from flask import Blueprint,render_template,url_for
from myBlog.modles import Post,Comment
blog_bp = Blueprint('blog',__name__)

@blog_bp.route('/',methods=["GET"])
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("blog/index.html",posts=posts)

@blog_bp.route('/post/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter(Comment.post_id==post_id)
    return render_template("blog/post.html",post=post,comments=comments)



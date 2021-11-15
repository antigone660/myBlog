from operator import pos
import re
from flask import Blueprint,render_template,url_for,flash
from wtforms.validators import Email
from myBlog.extensions import db
from myBlog.modles import Post,Comment
from myBlog.forms import CommentForm
blog_bp = Blueprint('blog',__name__)

@blog_bp.route('/',methods=["GET"])
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("blog/index.html",posts=posts)

@blog_bp.route('/post/<int:post_id>',methods=["GET","POST"])
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter(Comment.post_id==post_id)
    form = CommentForm()
    if form.validate_on_submit():
        author=form.author.data
        email=form.email.data
        body=form.body.data
        comment=Comment(
            author=author,
            email=email,
            body=body,
            post=post
        )
        db.session.add(comment)
        db.session.commit()
        flash(" u publish a comment")
    return render_template("blog/post.html",post=post,comments=comments,form=form)



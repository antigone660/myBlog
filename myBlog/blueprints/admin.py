from flask import Blueprint,render_template,url_for,flash
from werkzeug.utils import redirect

from myBlog.extensions import db
from myBlog.modles import User
from myBlog.forms import registerForm
admin_bp = Blueprint('admin',__name__)

@admin_bp.route('/register',methods=['GET','POST'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        flash('register successfully')
        return redirect(url_for("blog.index"))
    # flash("do u seek for me ?")
    return render_template('admin/register.html',form=form)

@admin_bp.route('/init')
def init():
    db.create_all()
    return "init"

@admin_bp.route("/show")
def show():
    res = User.query.first()
    
    return res.username

from flask import Blueprint,render_template,url_for,flash
from werkzeug.utils import redirect

from myBlog.forms import registerForm

admin_bp = Blueprint('admin',__name__)

@admin_bp.route('/register',methods=['GET','POST'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        flash('register successfully')
        return redirect(url_for("blog.index"))
    flash("do u seek for me ?")
    return render_template('admin/register.html',form=form)
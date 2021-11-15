import random

from flask import Blueprint,render_template,url_for,flash
from werkzeug.utils import redirect
from faker import Faker

from myBlog.extensions import db
from myBlog.modles import User,Admin,Category,Comment,Post,Link
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

@admin_bp.route('/log')
def log():
    pass

@admin_bp.route('/publish')
def publish():
    pass


@admin_bp.route('/init')
def init():
    admin = Admin(
        username='admin',
        password='123456',
        about='这个人很懒，什么也没有留下。'
    )
    db.drop_all()
    db.create_all()
    db.session.add(admin)
    db.session.commit()
    flash("init!")
    return redirect(url_for("blog.index"))

@admin_bp.route("/show")
def show():
    res = User.query.first()
    
    return res.username

@admin_bp.route("/fake")
def fake_all():
    fake_categories()
    fake_posts()
    fake_comments()
    flash("fake messages are generated!")
    return redirect(url_for("blog.index"))

fake = Faker()
def fake_categories(count=10):
    category=Category(name="Default")
    db.session.add(category)
    for i in range(count):
        category = Category(name=fake.word())
        db.session.add(category)
        try:
            db.session.commit()
        except:
            db.session.rollback()

def fake_posts(count=20):
    for i in range(count):
        post = Post(
            title=fake.text(50),
            body=fake.text(2000),
            category=Category.query.get(random.randint(1, Category.query.count())),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(post)
    db.session.commit()

def fake_comments(count=500):
    for i in range(count):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            # site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            # reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

    salt = int(count * 0.1)
    for i in range(salt):
        # unreviewed comments
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=False,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

        # from admin
        comment = Comment(
            author='Mima Kirigoe',
            email='mima@example.com',
            site='example.com',
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            from_admin=True,
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.commit()

    # replies
    for i in range(salt):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            replied=Comment.query.get(random.randint(1, Comment.query.count())),
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.commit()


def fake_links():
    twitter = Link(name='Twitter', url='#')
    facebook = Link(name='Facebook', url='#')
    linkedin = Link(name='LinkedIn', url='#')
    google = Link(name='Google+', url='#')
    db.session.add_all([twitter, facebook, linkedin, google])
    db.session.commit()

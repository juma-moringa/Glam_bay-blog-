from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# user class
class User(UserMixin,db.Model):

    '''
    User class to define user Objects
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

# blog class
class Blog(db.Model):
    '''
    Blog class to define blog Objects
    '''
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    content = db.Column(db.Text(),nullable=False)
    blog_by = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    comment = db.relationship('Comment', backref='blog', lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_user_blogs(cls,id):
        posts = Blog.query.filter_by(user_id = id).order_by(Blog.posted.desc()).all()
        return posts

    @classmethod
    def get_all_blogs(cls):
        return Blog.query.order_by(Blog.posted).all()


        # return blogs
    # def __repr__(self):
    #     return f'Blog {self.title}'
        
# Quotes class
class Quote:
    """
    Quotes is a  class for quotes  from API given
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote        

# subscribers class
class Subscriber(db.Model):
    '''
    Subscribers class to define subscriber Objects
    '''


    __tablename__='subscribers'


    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'

# comments class
class Comment(db.Model):
    '''
    Comments class to define comments Objects
    '''

    __tablename__='comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    def get_comment(id):
        comment = Comment.query.all(id=id)
        return comment


    def __repr__(self):
        return f'Comment {self.comment}'

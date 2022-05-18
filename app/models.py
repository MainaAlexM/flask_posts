from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Category(db.Model):
    '''
    Category class define category per pitch
    '''
    __tablename__ = 'categories'

    # add columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    Category =[
        1,
        "Love",
        "I love Myself"
    ]
    # save
    def save_category(self):
        '''
        The Function saves a category
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        '''
        The Query Function returns all data from categories
        '''
        categories = Category.query.all()
        return categories

#pitches
class Pitch(db.Model):

    """
    Lists pitches in each category
    """
    all_pitches = []

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String)
    date_posted = db.Column(db.DateTime,default=datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer,db.ForeignKey("categories.id"))
    comment = db.relationship("Comments", backref="Pitch", lazy = "dynamic")



    def save_pitch(self):
        '''
        Function to Save Pitches
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    # display pitches
    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.order_by(Pitch.date_posted.desc()).filter_by(category_id=id).all()
        return pitches



#Users
class User(UserMixin,db.Model):
    '''
    User class that helps create new Users
    '''
    __tablename__ = 'users'

    # add column
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True,index=True)
    password_hash=db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship("Pitch", backref="user", lazy = "dynamic")
    comment = db.relationship("Comments", backref="user", lazy = "dynamic")

    # securing our passwords
    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return f'User {self.username}'

#Comments
class Comments(db.Model):
    '''
    Comment class which allows users create new comments.
    '''
    __tablename__ = 'comment'

    # add columns
    id = db.Column(db. Integer,primary_key = True)
    comment_section_id = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_comment(self):
        '''
        Saving comments per pitch
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self,id):
        comment = Comments.query.order_by(Comments.date_posted.desc()).filter_by(pitches_id=id).all()
        return comment

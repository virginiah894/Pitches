from .import db,login_manager

# class to provide common user interface for all users

from flask_login import UserMixin
# function that takes password and generate a password hardh annd the later function  checks to confirm if the passwords match
from werkzeug.security import generate_password_hash, check_password_hash
# class for defining tthe users in the database
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    # table head
    __tablename__ = 'users'
    # table content

    id = db.Column(db.Integer, primary_key=True)
# adds a username which takes a maximum of 200 characters
    username = db.Column(db.String(200), index=True,nullable= False)
    email = db.Column(db.String(200), unique=True, index=True)
    # add columns for the bio and the  profile photo
    bio = db.Column(db.String(200))
    profile_pic_path = db.Column(db.String(255))
    password_secure = db.Column(db.String(200),nullable = False)
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')

    

    @property
    # decorater with a  class which cannot be read
    def password(self):
        raise AttributeError('you cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)
        # method to confirm password entered and compare if they are similar

    def verify_password(self, password):
        return check_password_hash(self.password_secure, password)

    def __repr__(self):
          # function that returns  a printed representattion of the table object
        return f'User{self.username}'

        # class that defines the roles of the users in the database
    def __repr__(self):
        return f'User{self.name}'


class Comment(db.Model):

    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
  


    def save_comments(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by().all()
        return comments


class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    
    
    author = db.Column(db.String(100))
    content = db.Column(db.String)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.relationship('Comment', backref='pitch', lazy='dynamic')
    example_id = db.Column(db.Integer,db.ForeignKey('examples.id'))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by().all()
        return pitches
        
class Example(db.Model):
    
    __tablename__= 'examples'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), index = True)
    pitches = db.relationship('Pitch', backref = 'examples', lazy = "dynamic")  
    
    @classmethod
    def get_types(cls):
        examples = Example.query.all()
        return examples

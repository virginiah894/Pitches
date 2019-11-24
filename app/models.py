from .import db
from . import login_manager
# class to provide common user interface for all users 

from flask_login import UserMixin
# function that takes password and generate a password hardh annd the later function  checks to confirm if the passwords match
from werkzeug.security import generate_password_hash,check_password_hash
# class for defining tthe users in the database



@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin,db.Model):
  # table head
  __tablename__ = 'users'
  # table content
  
  id = db.Column(db.Integer,primary_key = True)
# adds a username which takes a maximum of 200 characters
  username = db.Column(db.String(200),index = True)
  email =db.Column(db.String(200),unique = True,index = True)
  role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
  # add columns for the bio and the  profile photo
  bio = db.Column(db.String(200))
  profile_pic_path = db.Column(db.String())
  password_secure = db.Column(db.String(200))
  
  
  
  
  
  pass_secure =db.Column(db.String(200))
  @property
    # decorater with a  class which cannot be read
  def password(self):
    raise AttributeError ('you cannot read the password attribute')
  @password.setter
  def password(self,password):
    self.pass_secure = generate_password_hash(password)
      # method to confirm password entered and compare if they are similar
  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)
  def __repr__(self):
      # function that returns  a printed representattion of the table object
    return f'User{self.username}'

# class that defines the roles of the users in the database
class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer,primary_key = True)
  name = db.Column(db.String(200))
  users = db.relationship('User',backref = 'role',lazy="dynamic")
def __repr__(self):
  return f'User{self.name}'
  


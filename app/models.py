from .import db
# function that takes password and generate a password hardh annd the later function  checks to confirm if the passwords match
from werkzeug.security import generate_password_hash,check_password_hash
# class for defining tthe users in the database
class User(db.Model):
  # table head
  __tablename__ = 'users'
  # table content
  
  id = db.Column(db.Integer,primary_key = True)
# adds a username which takes a maximum of 200 characters
  username = db.Column(db.String(200))
  role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
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
  


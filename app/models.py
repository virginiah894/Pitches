from .import db
# class for defining tthe users in the database
class User(db.Model):
  # table head
  __tablename__ = 'users'
  # table content
  id = db.Column(db.Integer,primary_key = True)
# adds a username which takes a maximum of 200 characters
  username = db.Column(db.String(200))
  role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

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
  


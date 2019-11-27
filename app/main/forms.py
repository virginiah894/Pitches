from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
  title = StringField('Comment title',validators=[Required()])
  comment = TextAreaField('Pitch Comment', validators=[Required()])
  submit = SubmitField('Submit')

class UpdatePitch(FlaskForm):
    title = StringField(' Title', validators = [Required()])
    pitch = TextAreaField('Add a pitch', validators = [Required()])
    # author = TextAreaField('Add an author',validators= [Required])
    # category =TextAreaField('Add a category',validators= [Required])
    submit = SubmitField('Submit')



# category = db.Column(db.String(100))
    # author = db.Column(db.String(100))
    # content = db.Column(db.String)
    # upvote = db.Column(db.Integer)
    # downvote = db.Column(db.Integer)
    # date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    # users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # comment 
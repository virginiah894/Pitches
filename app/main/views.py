from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort
from ..models import User
@main.route('/')
def index():
  @login_required

  return render_template('index.html')
@main.route('/user/<usname>')
def profile(usname):
    user = User.query.filter_by(username = usname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

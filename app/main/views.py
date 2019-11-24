from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort
from ..models import User
from ..import db,photos
from .forms import UpdateProfile
@main.route('/')
def index():


    return render_template('index.html')

@main.route('/user/<usname>/update',methods = ['GET','POST'])
@login_required
def update_profile(usname):
    user = User.query.filter_by(username = usname).first()

    if user is None:
        abort(404)
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',usname=user.username))

    return render_template('profile/update.html',form =form)
    
@main.route('/user/<usname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = usname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',usname=usname))

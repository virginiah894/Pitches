from flask_login import login_required,current_user
from flask import render_template ,request,redirect,url_for,abort
from ..models import User,Comment
from ..import db,photos
from .forms import UpdateProfile
from .import main
# import markdown2




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
def update_pic(usname):
    user = User.query.filter_by(username = usname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',usname=usname))
@main.route('/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    pitch = Pitches.query.filter_by(id =pitch_id).first()
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        # new comment instance
        new_comment = Comment(pitch =pitch_id,pitch_comment=comment,user=current_user)
        # save comment
        new_comment.save_comment()
        return redirect(url_for('.comment',id = pitch_id ))

    
    return render_template('newcomment.html',form=form,user=user,pitch = pitch)

@main.route('/comment/<int:id>')
def single_comment(id):
    comment = Comment.query.get(id)
    if comment is None:
        abort(404)
    format_comment = markdown2.markdown(comment.pitch_comment,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('comment.html',comment = comment,format_comment=format_comment)
@main.route('/everything')
def everything():
    # comment = Comment.query.all()
    everything = Pitch.query.all()
    return render_template('everything.html',everything = everything,comment=comment)

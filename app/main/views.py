from flask_login import login_required,current_user
from flask import render_template ,request,redirect,url_for,abort
from ..models import User,Comment,Pitch,Example
from ..import db,photos
from .forms import UpdateProfile,UpdatePitch,CommentForm
from . import main
# import markdown2

@main.route('/')
def index():
    title = 'Welcome to Pitches World'
    categories = Example.get_types()
    
    # examples = Example.get_types()
    return render_template('index.html',title = title, categories=categories )


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
# @main.route('/everything')
# def everything():
#     # comment = Comment.query.all()
#     everything = Pitch.query.all()
#     return render_template('everything.html',everything = everything,comment=comment)
@main.route('/user/pitches/<int:id>')
def everything(id):
    
    users = User.query.get(id)
    title = f'{users.username} pitches'
    pitches = Pitch.get_pitches_user(users.id)
    
    return render_template('everything.html',title=title,pitches=pitches)
@main.route('/example/<int:id>')
def pitch_example(id):
    '''
    A view function that will return the pitches on a specific example of pitch
    '''

    examples= Example.query.get(id)
    title = f'{examples.name} pitches'
    pitches = Pitch.get_pitches(examples.id)

    
    return render_template('examples.html', title=title, types=types, pitches=pitches)
@main.route('/category/pitch/new/<int:id>', methods=["GET", "POST"])
def create_pitch(id):
    '''
    using a form to create a new pitch function
    '''

    form =UpdatePitch
    examples = Example.query.filter_by(id=id).first()
    if form.validate_on_submit():
        pitch = form.pitch.data
        title = form.title.data

        new_pitch = Pitch(examples_id=examples.id, title=title, pitch=pitch, user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('.pitch_example', id=types.id))

    title = f'{examples.name} pitches'
    return render_template('new_pitch.html', title=title, UpdatePitch_form=form,examples=examples)

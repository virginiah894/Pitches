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

        return redirect(url_for('main.profile',usname=user.username))

    return render_template('/profile/update.html',form =form)
    
@main.route('/user/<usname>/update/pic',methods= ['GET','POST'])
@login_required
def update_pic(usname):
    user = User.query.filter_by(username = usname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.update_profile',usname=usname))
@main.route('/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    pitch = Pitch.query.filter_by(id = id).first()
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        # new comment instance
        new_comment = Comment(pitch_id = pitch.id,comment=comment,user=current_user)
        # save comment
        new_comment.save_comments()
        return redirect(url_for('.comment',id = pitch.id ))

    
    return render_template('newcomment.html',form=form,user=current_user,pitch = pitch)

@main.route('/comment/<int:id>')
def comment(id):

    pitch = Pitch.query.get(id)
    comment = Comment.get_comments(pitch.id)
    title = f'{pitch.title} comments'
    
    print(comment)
    return render_template('comment.html', title=title, pitch=pitch, comment = comment)




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
    
    return render_template('examples.html', title=title,pitches=pitches,example=examples)

@main.route('/example/pitch/new/<int:id>', methods=["GET", "POST"])
def create_pitch(id):
    '''
    using a form to create a new pitch function
    '''

    form =UpdatePitch()
    examples = Example.query.filter_by(id=id).first()
    if form.validate_on_submit():
        pitch = form.pitch.data
        title = form.title.data

        new_pitch = Pitch(example_id=examples.id, title=title, content=pitch, user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('.pitch_example', id=examples.id))

    title = f'{examples.name} pitches'
    return render_template('new_pitch.html', title=title, UpdatePitch_form=form,examples=examples)


@main.route('/user/<usname>')
def profile(usname):
    user = User.query.filter_by(username = usname).first()
    example = Example.query.all()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user,example = example)

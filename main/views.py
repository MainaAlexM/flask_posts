from application import main
from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from ..application.models import User,Pitch,Comment
from datetime import datetime
from ..application import db,photos
from .forms import UpdateProfile,PitchForm,CommentForm

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Top-Pitches'

    # Getting reviews by category
    Business_piches = Pitch.get_pitches('Business')
    Team_piches = Pitch.get_pitches('Team')
    Love_pitches = Pitch.get_pitches('Love')


    return render_template('index.html',title = title, Business = Business_piches, Team = Team_piches, Love = Love_pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches_count = Pitch.count_pitches(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitches = pitches_count,date = user_joined)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form = form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.text.data
        category = pitch_form.category.data

        # Updating a pitch instance
        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,user=current_user,likes=0,dislikes=0)

        # Saving a pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'Post a New pitch'
    return render_template('new_pitch.html',title = title,pitch_form=pitch_form )

@main.route('/pitches/business_pitches')
def Business_pitches():

    pitches = Pitch.get_pitches('Business')

    return render_template("business_pitches.html", pitches = pitches)

@main.route('/pitches/team_pitches')
def Team_pitches():

    pitches = Pitch.get_pitches('Team')

    return render_template("team_pitches.html", pitches = pitches)

@main.route('/pitches/love_pitches')
def Love_pitches():

    pitches = Pitch.get_pitches('Love')

    return render_template("love_pitches.html", pitches = pitches)

@main.route('/pitch/<int:id>', methods = ['GET','POST'])
def pitch(id):
    pitch = Pitch.get_pitch(id)
    posted_date = pitch.posted.strftime('%b %d, %Y')

    if request.args.get("like"):
        pitch.likes = pitch.likes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    elif request.args.get("dislike"):
        pitch.dislikes = pitch.dislikes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comment(comment = comment,user = current_user,pitch_id = pitch)

        new_comment.save_comment()


    comments = Comment.get_comments(pitch)

    return render_template("pitch.html", pitch = pitch, comment_form = comment_form, comments = comments, date = posted_date)

@main.route('/user/<uname>/pitches')
def user_pitches(uname):
    user = User.query.filter_by(username=uname).first()
    pitches = Pitch.query.filter_by(user_id = user.id).all()
    pitches_count = Pitch.count_pitches(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')

    return render_template("profile/pitches.html", user=user,pitches=pitches,pitches_count=pitches_count,date = user_joined)
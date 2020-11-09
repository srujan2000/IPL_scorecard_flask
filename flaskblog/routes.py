from flaskblog import app,db
from flask import render_template,request, redirect, url_for,flash,abort
from flaskblog.forms import LoginForm,MatchForm
from flaskblog.models import Post,User
from flask_login import current_user,login_user,logout_user,login_required
import os

# posts= [{
#     'Title': 'Match 1',
#     'Date': '19 Sept 2020',
#     'Teams' : 'CSK vs MI',
#     'firstinnings': 'MI - 162/9',
#     'secondinnings': 'CSK - 163/5',
#     'Result': 'CSK Won By 5 Wickets ',
#     'MOM': 'Ambati Rayudu'
#     },
#     {
#     'Title': 'Match 2',
#     'Date': '20 Sept 2020',
#     'Teams' : 'DC vs KXIP',
#     'firstinnings': 'MI - 156/9',
#     'secondinnings': 'CSK - 156 /5',
#     'Result': 'DC Won By 10 Wickets(SUPER OVER)',
#     'MOM': 'Kagiso Rabada'
#     }
# ]

@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all()
    return render_template('home.html',posts=posts)

@app.route("/login",methods=['GET','POST'])
def login():

     if current_user.is_authenticated:
        return redirect(url_for('home'))

     form = LoginForm()
     
     if form.validate_on_submit():
        

        user = User.query.filter_by(email = form.email.data).first()

        if user and (user.password == form.password.data) :
             login_user(user)
             flash('Login Successful','success')
             return redirect(url_for('home'))
        else:
            flash('Wrong Credentials','danger')
            return redirect(url_for('login'))

             
     return render_template('login.html', form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/post",methods = ['GET','POST'])
@login_required
def post():
    form = MatchForm()

    if form.validate_on_submit():

        id = ((form.Title.data).split())[1]
        post = Post(id= id,match=form.Title.data,teams= form.Teams.data,date=form.Date.data,venue=form.Venue.data,firstinnings=form.First.data,secondinnings=form.Second.data,result=form.Result.data,mom=form.MOM.data,user_id = 1)
        db.session.add(post)
        db.session.commit()
        flash('New Post was created','success')
        return redirect(url_for('home'))

    return render_template('post.html',form=form)

@app.route("/post/<int:post_id>")
def check_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('check_post.html',post=post)


@app.route("/post/<int:post_id>/update",methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)

    form = MatchForm()

    if form.validate_on_submit():
         post.match = form.Title.data
         post.date = form.Date.data
         post.venue = form.Venue.data
         post.teams = form.Teams.data
         post.firstinnings = form.First.data
         post.secondinnings = form.Second.data
         post.result = form.Result.data
         post.mom = form.MOM.data
         db.session.commit()
         flash('Your Post Has been Updated','success')
         return redirect(url_for('home'))


    elif request.method == 'GET':
        form.Title.data = post.match
        form.Date.data = post.date
        form.Venue.data = post.venue
        form.Teams.data = post.teams
        form.First.data = post.firstinnings
        form.Second.data = post.secondinnings
        form.Result.data = post.result
        form.MOM.data = post.mom

    return render_template('post.html',form=form)


@app.route("/post/<int:post_id>/delete",methods=['GET','POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    db.session.delete(post)
    db.session.commit()
    flash('Your Post Has been Updated','success')
    return redirect(url_for('home'))








from flaskblog import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50),nullable=False,unique=True)
    password = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return f"Post('{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match = db.Column(db.String(50),unique=True,nullable=False)
    teams = db.Column(db.String(50), nullable = False)
    date = db.Column(db.String(40),nullable = False)
    venue = db.Column(db.String(20),nullable = False)
    firstinnings = db.Column(db.String(40), nullable = False)
    secondinnings = db.Column(db.String(40), nullable = False)
    result = db.Column(db.String(40), nullable = False)
    mom = db.Column(db.String(40), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.match}','{self.teams},'{self.venue}')"
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField , SubmitField
from wtforms.validators import DataRequired , Length , Email , ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class MatchForm(FlaskForm):
    Title = StringField('Title(Match No)', validators=[DataRequired()])
    Date = StringField('Date(DD Month(sept) YY)', validators=[DataRequired()])
    Venue = StringField('Venue', validators=[DataRequired()])
    Teams = StringField('Teams(T1 vs T2)', validators=[DataRequired()])
    First = StringField('First Innings(score/wickets)', validators=[DataRequired()])
    Second = StringField('Second Innings(score/wickets)', validators=[DataRequired()])
    Result =  StringField('Result(Team won by runs/wickets)', validators=[DataRequired()])
    MOM = StringField('Man of the Match(Player Name)', validators=[DataRequired()])
    Submit = SubmitField('Submit')


    
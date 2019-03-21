from  flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@host/database'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask-user:Redhat2019**@165.227.177.17/flask-user'
app.config['SECRET_KEY'] = 'mylittlewinky_77>hallaluya'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)



class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = StringField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

@app.route('/')
def index():
    return "Hello World"

@app.route("/signup", methods=['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1> New User Has been created! </h1>'
    return render_template('signup.html', form=form)

if __name__ == "__main__":
    app.run(port=80, host='0.0.0.0')

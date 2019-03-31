from  flask import Flask, render_template, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

########################MYSQL#######################

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@host/database'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask-user:Redhat2019**@165.227.177.17/flask-user'
app.config['SECRET_KEY'] = 'mylittlewinky_77>hallaluya'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

########################USERS CLASS#######################

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

########################LOGIN_MANAGEW#######################

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


########################LOGIN CLASS#######################

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

########################REGISTAR CLASS#####################

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = StringField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


########################HOME PAGE#######################

@app.route('/')
def index():
    return render_template('index.html')

########################HEALTHY#######################

@app.route('/healthy', methods=['GET'])
def healthy():
    return jsonify({'message': 'ok'})

########################SIGNUP#######################

@app.route("/signup", methods=['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1> New User Has been created! </h1>'
    return render_template('signup.html', form=form)


########################LOGOIN#######################

@app.route('/login', methods=['GET', 'POST'] )
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                return redirect(url_for('dashboard'))
        return 'Invalid username or password'

    return render_template('dashboard.html', form=form)
    #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'


########################DASHBOARD#######################

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

########################LOGOUT#######################

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_all('index'))

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')

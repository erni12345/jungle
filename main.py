from flask import Flask, redirect, url_for, render_template, request, session, g, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from home_page_logic import *
from search_logic import *
from account_page_logic import *
from upload_logic import *
from sign_up_logic import creat_account

app = Flask(__name__)
app.config['SECRET_KEY'] = 'joe momma'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/Jungle.db'
app.config['UPLOAD_FOLDER'] = "/static/"
app.config['MAX_CONTENT_PATH'] = 10^20

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

        

class Login(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


@login_manager.user_loader
def load_user(user_id):
    return Login.query.get(int(user_id))




@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        return render_template('index.html')


@app.route('/newpost/', methods=['GET', 'POST'])
@login_required
def create_post():
    account = getAccount(current_user.id)
    return render_template("newpost.html", user = account)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    
    result = request.form
    email = result["email"]
    password = result["password"]

    if request.method == "POST":

        user = Login.query.filter_by(email = str(email)).first()

        if user:
            if user.password == str(password):
                login_user(user) #add remember me
                return redirect(url_for('home'))


        return render_template('index.html')

    return render_template('index.html')



@app.route('/signup/', methods=['GET', 'POST'])
def signup():

 
    result = request.form
    email = result["email"]
    password1 = result["pass1"]
    password2 = result["pass2"]
    name = result["name"]
    last_name = result["last_name"]
    age = result["age"]
    username = result["user_name"]
    bio = result["age"]
    

    if request.method == "POST" and password1 == password2:

        new_user = Login(email = email, password = password2)

        db.session.add(new_user)
        db.session.commit()

        creat_account(new_user.id, name, last_name, age, username, bio)
        
        return render_template("index.html")


    return render_template('index.html')

@app.route('/logout/')
@login_required
def logout():

    logout_user()

    return redirect(url_for('index'))


@app.route('/profile/')
@login_required
def profile():


    posts = get_user_posts(current_user.id)
    account = getAccount(current_user.id)
    return render_template("profile.html", posts = posts, user = account)


@app.route('/home/')
@login_required
def home():
    if current_user.is_authenticated:
        posts = get_posts(current_user.id)
        for x in posts:
            user = getAccount(x["id"])
            x["user"] = user
        return render_template('home.html', user_id = current_user.id, posts=posts)
    else:
        return redirect(url_for('index'))


@app.route('/search/', methods = ["POST", "GET"])
@login_required
def search():
    if current_user.is_authenticated:
        result = request.form
        search = result["search"]
        results = user_search(search)
        return render_template("search.html", results = results)
    else:
        return redirect(url_for('index'))


@app.route("/follow/", methods = ["POST", "GET"])
def follow():
    if current_user.is_authenticated:
        result = request.form
        idFollow = result["id"]
        follow_account(current_user.id, idFollow)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

    
@app.route('/uploader/', methods = ['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        title = request.form["title"]
        descp = request.form["Description"]
        f.save("static/"+f.filename)
        upload_post(current_user.id, title, descp, str(f.filename) )
        return redirect(url_for("home"))
    else:
        return redirect(url_for("index"))



@app.route('/view_account/', methods = ['GET', 'POST'])
@login_required
def view_account():

    user_id = request.form["id"]
    posts = get_user_posts(user_id)
    account = getAccount(user_id)
    return render_template("profile.html", posts = posts, user = account)


app.secret_key = 'joeMomma'


app.run(debug=True)


from flask import Flask, render_template, url_for, flash, redirect #載入flask
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm,LoginForm

app = Flask(__name__) #建立 Application 物件

app.config['SECRET_KEY'] ='df1e8f2d5e6b36ab313ac14506482327'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    account = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    sername = db.Column(db.String(20), unique=True, nullable=False)

posts = [
    {
        'author':'penny',
        'title':'blog post 1',
        'content':'first post content',
        'date_posted':'april 20,2024'
    },
    {
        'author':'didi',
        'title':'blog post 2',
        'content':'second post content',
        'date_posted':'april 28,2024'
    }
]

@app.route('/')
@app.route('/home')
def home(): #用來回應網站首頁連線的函式
    return render_template('home.html',posts=posts) #回傳網站首頁的內容 
    #posts:資料匯到home.html

@app.route('/about')
def about(): #用來回應網站首頁連線的函式
    return render_template('about.html',title = 'About') #title有About

@app.route('/register', methods=['GET','POST'])
def register(): 
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title = 'Register', form=form) 

@app.route('/login')
def login(): 
    form = LoginForm()
    return render_template('login.html',title = 'login', form=form) 

if __name__ == '__main__':
    app.run(debug = True)#啟動網站伺服器
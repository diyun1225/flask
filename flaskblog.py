from flask import Flask, render_template, url_for, flash, redirect,send_from_directory, request #載入flask
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm,LoginForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__) #建立 Application 物件

app.config['SECRET_KEY'] ='df1e8f2d5e6b36ab313ac14506482327'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_account.db'
db = SQLAlchemy(app)

   
class users(db.Model):
    __tablename__ = 'users'  # 指定表名
    account = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    change_password = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.name}>'


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

UPLOAD_FOLDER = 'C:\\Users\\USER\\Documents\\GitHub\\flask\\file'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/push', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 
                                   filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

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
    with app.app_context():
        db.create_all()
        users = users.query.all()
        for user in users:
            print(user.name)  # 使用定义的字段名

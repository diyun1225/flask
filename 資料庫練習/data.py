from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
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


@app.route('/')
@app.route('/home')
def home(): #用來回應網站首頁連線的函式
    return render_template('home.html') #回傳網站首頁的內容 
    #posts:資料匯到home.html

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        users = users.query.all()
        for user in users:
            print(user.name)  # 使用定义的字段名

    app.run(debug=True)

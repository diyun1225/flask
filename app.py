from flask import Flask, render_template #載入flask
app = Flask(__name__) #建立 Application 物件


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

@app.route('/about')
def about(): #用來回應網站首頁連線的函式
    return render_template('about.html') #回傳網站首頁的內容

if __name__ == '__main__':
    app.run(debug = True)#啟動網站伺服器
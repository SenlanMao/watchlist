from flask import Flask,render_template,request
app = Flask(__name__)

name = 'Grey Li'
movies = [
{'title': 'My Neighbor Totoro', 'year': '1988'},
{'title': 'Dead Poets Society', 'year': '1989'},
{'title': 'A Perfect World', 'year': '1993'},
{'title': 'Leon', 'year': '1994'},
{'title': 'Mahjong', 'year': '1996'},
{'title': 'Swallowtail Butterfly', 'year': '1996'},
{'title': 'King of Comedy', 'year': '1999'},
{'title': 'Devils on the Doorstep', 'year': '1999'},
{'title': 'WALL-E', 'year': '2008'},
{'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
def hello_world():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/index')
def index():
    return render_template('index.html',name=name,movies=movies)   #会自动找templates文件夹里面的index.html,并不需要一个绝对路径

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080)
import sqlite3

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index')
def index():
    score = []
    num = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()
    return render_template("index.html",score=score,num=num)
@app.route('/')
def home():
    return index()
@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie.html",movies=datalist)


if __name__ == '__main__':
    app.run()

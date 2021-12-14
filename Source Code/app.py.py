import os
import random
from flask import Flask,session,url_for,redirect,render_template,request
from database import db_connect, user_reg,viewpost1,analysis1,analysis2,post_add
from database import ins_profile,viewusrpst,comment_add,admin_loginact,ins_loginact 

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def FUN_root():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/user")
def user():
       return render_template("user.html")

@app.route("/userreg")
def userreg():
    return render_template("userreg.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/uvc")
def uvc():
    username = session['username']
    data = viewusrpst(username)
    return render_template("uvc.html",comm = data)

@app.route("/analysis")
def analysis():
    username = session['username']
    data = analysis1()
    data3 = analysis2()
    data1 = viewpost1(username)
    return render_template("analysis.html",ana = data, p1=data1,ana1=data3)

@app.route("/vp")
def vp():
    username = session['username']
    data1 = viewpost1(username)
    return render_template("vp.html", p1=reversed(data1))

@app.route("/userhome")
def userhome():
    return render_template("userhome.html")

@app.route("/viewusers")
def viewusers():
    data = ins_profile()
    return render_template("viewusers.html",ins = data)

@app.route("/adminhome")
def adminhome():
    return render_template("adminhome.html")

@app.route("/aact",methods = ['GET','POST'])
def aact():
    if request.method == 'POST':
        post=request.form['post']
        print(post)
        data = vaact(post)
        print("....................................")
        print(data)
        return render_template("analysis.html",add1 = data)

@app.route("/vp",methods = ['GET','POST'])
def pact():
    if request.method == 'POST':  
      status = comment_add(request.form['comment'],request.form['post'])
      print(request.form['comment'],request.form['post'])
      username = session['username']
      data1 = viewpost1(username)
      print(status)
      print(type(data1))
      dat=reversed(data1)
      if status == 1:
        return render_template("vp.html", p1=reversed(data1))
      else:
        return render_template("vp.html", p1=reversed(data1))    

@app.route("/insreg", methods = ['GET','POST'])
def insreg():
   if request.method == 'POST':    
      
      status = user_reg(request.form['uname'],request.form['mail'],request.form['password'],request.form['gender'],request.form['dob'],request.form['mobile'],request.form['address'])
      
      if status == 1:
       return render_template("user.html",m1="sucess")
      else:
       return render_template("userreg.html",m1="failed")

@app.route("/postact", methods = ['GET','POST'])
def postact():
   if request.method == 'POST':    
      
      status = post_add(request.form['uname'],request.form['post'])
      
      if status == 1:
       return render_template("post.html",m1="sucess")
      else:
       return render_template("post.html",m1="failed")

@app.route("/adminlogact", methods=['GET', 'POST'])       
def adminlogact():
    if request.method == 'POST':
        status = admin_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("adminhome.html", m1="sucess")
        else:
            return render_template("admin.html", m1="Login Failed")

@app.route("/inslogin", methods=['GET', 'POST'])       
def inslogin():
    if request.method == 'POST':
        status = ins_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("userhome.html", m1="sucess")
        else:
            return render_template("user.html", m1="Login Failed")

   
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000,use_reloader=False)

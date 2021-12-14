import MySQLdb
from flask import session
from clas_new import* 

def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",passwd="root", db="project")
    c = _conn.cursor()

    return c, _conn
def user_reg(uname,mail,password,gender,dob,mobile,address):
    try:
        c, conn = db_connect()
        print(uname,mail,password,gender,dob,mobile,address)
        id="0"
        
        j = c.execute("insert into user (id,name, password, mail,gender,dob,mobile,address) values ('"+id +
                      "','"+uname+"','"+password+"','"+mail+"','"+gender+"','"+dob+"','"+mobile+"','"+address+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

def post_add(uname,post):
    try:
        c, conn = db_connect()
        print(uname,post)
        id="0"
        comment1='pending'
        type1=prediction_result(post)
        print("*********************************************")
        print(type1)
        j = c.execute("insert into post (name, post, comment,type) values ('"+uname+"','"+post+"','"+comment1+"','"+type1+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

def comment_add(comment,post):
    try:
        c, conn = db_connect()
        j = c.execute("update post set comment='"+comment+"' where post='"+post+"' ")
        conn.commit()
        conn.close()
        return j
    except Exception as e:
        print(e)
        return(str(e))


def ins_profile():
    c, conn = db_connect()
    c.execute("select * from user")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def viewpost1(username):
    c, conn = db_connect()
    c.execute("select * from post")
    result = c.fetchall()
    conn.close()
    print("result")
    return result



def viewusrpst(username):
    c, conn = db_connect()
    c.execute("select * from post where name='"+username+"' ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def analysis1():
    c, conn = db_connect()
    c.execute("select count(type) from post where type='Emergency'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def analysis2():
    c, conn = db_connect()
    c.execute("select count(type) from post where type='Feedback'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

              
def admin_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from admin where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))


def ins_loginact(username, password):
    try:
        c, conn = db_connect()
        
        j = c.execute("select * from user where name='" +
                      username+"' and password='"+password+"' "  )                  
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    print(db_connect())

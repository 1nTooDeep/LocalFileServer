from flask import (
    Blueprint,render_template,request,make_response,Response,redirect
)

users={'root':'password'}
login=Blueprint('login',__name__,url_prefix='/login')
bp=login
@bp.route('/')
def f():
    return render_template("login.html")

@bp.route('/check',methods=['POST'])
def checklogin():
    print('checking...')
    user=request.form.get('user')
    passwd=request.form.get('password')
    print(user,passwd)
    if users.get(user)==passwd:
        res=make_response(redirect('/'),)
        res.set_cookie('user',str(user),max_age=3600)
        return res
    return make_response("wrong password",200)
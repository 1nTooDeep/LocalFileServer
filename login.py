from flask import (
    Blueprint
)

login=Blueprint('login',__name__,url_prefix='/login')
bp=login
@bp.route('/')
def f():
    return "login"
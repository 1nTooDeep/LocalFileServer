from flask import (
    Blueprint,send_from_directory,make_response,url_for,request
)
import os
from app import DIRECTORY_PATH

download=Blueprint('download',__name__,url_prefix='/dowload')
bp=download
@bp.route('/<string:filename>',methods=['OPTIONS','GET','POST'])
def file_content(filename):
    print(filename in os.listdir(DIRECTORY_PATH))
    if filename in os.listdir(DIRECTORY_PATH):
        return make_response(send_from_directory(DIRECTORY_PATH, filename),200)
    else:
        return make_response('error',200)

from flask import (
    Blueprint,request
)
from get_file import DIRECTORY_PATH
bp=Blueprint('upload',__name__,url_prefix='/upload')

@bp.route('/file',methods=['GET','POST','OPTION'])
def upload():
    print(f"in uploadfile.")
    file=request.files.get('file')
    file.save(DIRECTORY_PATH+f"/{file.filename}")
    return "save success."
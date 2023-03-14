from flask import (
    render_template, send_from_directory, request, redirect,
    url_for, flash, sessions, session,make_response,Flask

)
from flask_cors import CORS
import os
import time
import logging
from get_file import get_files_data,DIRECTORY_PATH

app = Flask(__name__)
app.secret_key = 'askydiqyddiudhiudiwuhdhdyjqoijd'
log = logging.Logger('flasklog')
app.logger.addHandler(log)


@app.route("/",methods=['POST','GET'])
def index():
    # if session.get('user') == None:
        # return render_template('login.html')
    files = get_files_data()
    return render_template("index.html", files=files)


@app.route("/filedetail")
def filedetail():
    return get_files_data()


@app.route('/args')
def args():
    return request.get_data()



if __name__ == '__main__':
    # 在局域网上开启端口
    cors = CORS(app, resources=r'/*')
    from login import login
    from download import download
    from upload import bp as upload
    app.register_blueprint(login,url_prefix='/login')
    app.register_blueprint(download,url_prefix='/download')
    app.register_blueprint(upload,url_prefix='/upload')
    app.run(port="5000", debug=True,host="::")
    

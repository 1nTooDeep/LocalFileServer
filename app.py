from flask import Flask
from flask import (
    render_template, send_from_directory, request, redirect,
    url_for, flash, sessions, session,make_response

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
    if session.get('user') == None:
        return render_template('login.html')
    files = get_files_data()
    return render_template("index.html", files=files)

@app.route("/download/<filename>", methods=['GET', 'POST'])
def file_content(filename):
    if filename in os.path.listdir(DIRECTORY_PATH):
        return send_from_directory(DIRECTORY_PATH, filename)
    else:
        return make_response('error',200)


@app.route("/filedetail")
def filedetail():
    return get_files_data()


@app.route('/args')
def args():
    return request.get_data()


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    # 在局域网上开启端口
    cors = CORS(app, resources=r'/*')
    app.run(port="8000", debug=True,host="0.0.0.0")

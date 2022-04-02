from flask import Flask, render_template, request, flash, redirect,\
 url_for, flash, make_response, session

from config import Config
import datetime

app = Flask(__name__)
app.secret_key = 'super secret key'
app.permanent_session_lifetime = datetime.timedelta(days=365)

@app.route('/')

def index():
    if 'username' in session:
        username = session['username']
    else:
        username = False
    return render_template('index.html', username = username)

@app.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        session['username'] = request.form['username']
        redirect(url_for('index'))

@app.route('/queue',methods=['POST'])
def queue():
    if request.method == 'POST':
        redirect(url_for(index))





if __name__ == '__main__':
     app.run(port=8080)

from flask import Flask, render_template, request, flash, redirect,\
 url_for, flash, make_response, session
from flask import Response
from flask import Flask
from flask import render_template
import sched, time
import threading
import argparse
import datetime
import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from apscheduler.schedulers.background import BackgroundScheduler
from flask_socketio import SocketIO, emit

outputFrame = None
lock = threading.Lock()
# vs = VideoStream(src=0).start()

from database import init_db

init_db()

from database import db_session
from models import User, Queue
# sqlalchemy config
engine = create_engine('sqlite:///:memory:', echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()
app = Flask(__name__)
app.secret_key = 'super secret key'
app.permanent_session_lifetime = datetime.timedelta(days=365)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

@app.route('/')

def index():
    if 'username' in session:
        username = session['username']
    else:
        username = False
    return render_template('index.html', username = username)

@app.route('/login', methods=['GET', 'POST', 'DESTROY']) 
def login():
    username = request.form.get('username')
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        p = User.query.filter_by(username=username).first()
        print(p)
        password = request.form.get('password')
        if p and (p.password == request.form.get('password')):
            flash('Successful Login')
            return redirect(url_for('index'))
        elif p:
            flash('Username Already Exists')
            render_template('login.html')
        else:
            db_session.add(User(username=username,password=request.form.get('password')))
            db_session.commit()
            session['username'] = username
            flash('User Registered')
            return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))

@app.route('/queue', methods=["POST"])
def queue():
    p = User.query.filter_by(username=session['username']).first()
    if p:
        q = Queue.query.filter_by(id=p.id).first()
    else:
        print("no p added")
        return redirect(url_for('index'))
    print(request.form.get("link"))
    if not q:
        l = request.form.get("link").replace("watch?v=","/embed/")
        db_session.add(Queue(p.id, l))
        db_session.commit()
        flash('Added to queue')
    else:
        flash('Already in queue')
    return redirect(url_for('index'))

# socketio = SocketIO(app)
    # import sched, time
import time

# @socketio.on('connect')
# @celery.task()
def change_link():
    q = Queue.query.first()
    if q:
        db_session.delete(q)
        db_session.commit()
        with app.test_request_context('/'):
            socketio.emit('change', {'link': q.video, 'user': q.id})
            print(q.video)
    else:
        with app.test_request_context('/'):
            socketio.emit('change', {'link': 'https://www.youtube.com/embed/5qap5aO4i9A', 'user': None})
            print('Nothing')
    # sc.enter(2, 1, change_link, (sc,))


@app.before_first_request
def thread_start():
    # t = threading.Thread(target = change_link)
    # t.daemon = True
    # t.start()
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(change_link,'interval',minutes=1)
    sched.start()

if __name__ == '__main__':
     '''
     ap = argparse.ArgumentParser()
     ap.add_argument("-i", "--ip", type=str, required=False, help="ip address of the device")
     ap.add_argument("-o", "--port", type=int, required=False, help="ephemeral port number of the server (1024 to 65535)")
     ap.add_argument("-f", "--frame-count", type=int, default=32, help="# of frames used to construct the background model")
     args = vars(ap.parse_args())
     '''
     # s = sched.scheduler(time.time, time.sleep)
     # s.enter(60, 1, change_link, (s,))
     # s.run()

     # t1 = threading.Thread(target=detect_motion)
     # t1.daemon = True
     # t1.start()

     # sched = BackgroundScheduler(daemon=True)
     # sched.add_job(change_link,'interval',minutes=1)
     # sched.start()

     socketio.run(app)
     # app.run(threaded=True)
     # change_link()

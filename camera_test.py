    # -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:14:23 2022

@author: Will
"""

from flask import Flask, render_template, request
from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
import threading
import argparse
import datetime
import imutils
import time
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', text='')

@app.route('/stream')
def stream():
    return render_template('stream.html', text='')

@app.route('/viewer')
def viewer():
    return render_template('viewer.html', src='https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1')

if __name__ == '__main__':
     app.run()

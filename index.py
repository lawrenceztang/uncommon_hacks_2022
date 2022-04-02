from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# sqlalchemy config
engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    return render_template('index.html', text='')

if __name__ == '__main__':
     app.run(port=8080)

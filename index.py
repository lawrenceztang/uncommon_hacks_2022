from flask import Flask, render_template, request
import audd_test

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', text='')

@app.route('/rr_check', methods=["POST"])
def rr_check():
    url = request.form['url']
    is_rr = audd_test.url_to_audio(url)
    if is_rr:
        return render_template('index.html', text='You would have been Rick Rolled. It\'s OK. We saved you. You\'re welcome.')
    else:
        return render_template('index.html', text='You lucked out this time.')
if __name__ == '__main__':
     app.run(port=8080)

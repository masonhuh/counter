from flask import Flask, render_template, session, redirect, request
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'seeeeeccretkey'

@app.route('/')
def index():
    if 'clicks' not in session:
        session['clicks'] = 0
    if 'counter' not in session:
        session['counter'] = 0
    if 'tracker' not in session:
        session['tracker'] = []
    return render_template("index.html", act=session['tracker'], len_act=len(session['tracker']))

@app.route('/process_clicks', methods=["POST"])
def clicks():
    x = request.form['which_form']
    time_string = datetime.now()
    time_string = time.strftime('%m/%d/%Y %H:%M:%S')
    if x == 'refresh' and session['counter'] < 15 and session['clicks'] < 500:
        session['x'] = x
        new_value = 1
        session['clicks'] += 1
        session['tracker'].append([new_value, x, time_string])
    elif x == 'reset' or session['counter'] >= 15 or session['clicks'] > 500:
        session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
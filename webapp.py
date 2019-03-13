from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask import render_template
from flask_mail import Mail, Message

import csv
import pprint
import os

app = Flask(__name__)

app.debug = True #Change this to False for production
app.secret_key = os.environ['SECRET_KEY'] #used to sign session cookies


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mehufarm@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

@app.route('/')
def Page1():
    return render_template('Page1.html')

@app.route('/Page2')
def Page2():
    return render_template('Page2.html')
@app.route('/Page3')
def Page3():
    return render_template('Page3.html')
@app.route('/Page4')
def Page4():
    return render_template('Page4.html')

@app.route('/next1',methods=["POST","GET"])
def rendernext1():
    return render_template('Page2.html')

@app.route('/next2',methods=["POST","GET"])
def rendernext2():
    print(request.form)
    if request.form["data"] == 'mrs.adams':
        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    session["data1"]=request.form["data"]
    return render_template('Page3.html')

@app.route('/next3',methods=["POST","GET"])
def rendernext3():
    print(request.form)
    session["data2"]=request.form["data"]
    return render_template('Page4.html')


@app.route('/finish',methods=["POST","GET"])
def renderfinish():

    messg = session['data1'] + ',' + session['data2'] + ',' + str(request.form['data'])
    msg = Message('User Dats', sender = 'mehufarm@gmail.com', recipients = ['mehufarm@gmail.com'])
    msg.attach("data.csv", "data/csv" , messg )

    mail.send(msg)
    return render_template('Page1.html' , sent="Your survey is complete and your awnsers are sent.")


@app.route('/home',methods=["POST","GET"])
def renderhome():
    return render_template('Page1.html')

if __name__ == '__main__':
    app.run()

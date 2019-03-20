from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask import render_template
from flask_mail import Mail, Message
from time import localtime, strftime
from werkzeug.utils import secure_filename
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
app.config['UPLOAD_FOLDER']='/Users/P3/Desktop'
mail=Mail(app)

@app.route('/')
def Page1():
    print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))
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
@app.route('/Page5')
def Page5():
    return render_template('Page5.html')

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

@app.route('/next4',methods=["POST","GET"])
def rendernext4():
    print(request.form)
    session["data3"]=request.form["data"]
    return render_template('Page5.html')

@app.route('/next5',methods=["POST","GET"])
def rendernext5():
    print(request.form)
    session["data4"]=request.form["data"]
    return render_template('Page6.html')

@app.route('/finish',methods=["POST","GET"])
def renderfinish():
    file=request.files['data']
    #bytefile=os.fsencode(file)
    #bytefile=open(file, "rb").read()
    # print(type(file))
    # file.save(app.config['UPLOAD_FOLDER'], "tmp.png")
    messg = 'Name: ' + session['data1'] + ',' + 'Smash Main: '+ session['data2'] + ',' +"Name: "+ session["data3"] + ',' + "Name: "+ session["data4"] + ','+'Time; '+ (strftime("%d %b %Y %H:%M:%S", localtime()))
    msg = Message('User Dats', sender = 'mehufarm@gmail.com', recipients = ['mehufarm@gmail.com'])
    msg.attach("data.csv", "text/csv" , messg )

    msg.attach("image.png", "image/png", file.read())
    mail.send(msg)
    return render_template('Page1.html' , sent="Your survey is complete and your awnsers are sent.")


@app.route('/home',methods=["POST","GET"])
def renderhome():
    return render_template('Page1.html')

if __name__ == '__main__':
    app.run()

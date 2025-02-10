import smtplib
from flask import Flask, render_template, request, url_for, flash, jsonify
import os
from dotenv import load_dotenv
from werkzeug.utils import redirect

# from flask_bootstrap import Bootstrap5
load_dotenv()
app=Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
EMAIL=os.environ.get('EMAIL')
PASSWORD=os.environ.get('PASSWORD')


# Bootstrap5(app)
def send_email(name,email,message):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=email,to_addrs='nazanhaciyeva99@gmail.com',
                            msg=f'Subject:Someone want to reach out you by Portfolio\n\n Name: {name}\n'
                                f' Email: {email}\n Message:{message}')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact',methods=['POST','GET'])
def send_message():
    if request.method=='POST':
        name=request.form.get("name")
        email=request.form.get("email")
        message=request.form.get('message')
        send_email(name=name,email=email,message=message)

        return 'Message sent succesfully. Thanks!'




if __name__=="__main__":
    app.run(debug=False)
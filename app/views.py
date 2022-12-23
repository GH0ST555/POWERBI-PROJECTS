#all the routes for my website go here

#import relevant modules
import os
from app import app
from flask import render_template, flash,redirect,request, make_response,json,url_for
from flask_login import LoginManager,login_required,logout_user,login_user,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message


#it is a sample view to test a sample JSON File with flask. as i am not very familiar with JSON i am trying an example

@app.route('/')
def test_load():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "adress.json")
    data = json.load(open(json_url))
    return render_template('homepage.html', data=data)
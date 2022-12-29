#all the routes for my website go here

#import relevant modules
import os
from app import app
from flask import render_template, flash,redirect,request, make_response,json,url_for
from flask_login import LoginManager,login_required,logout_user,login_user,current_user
from flask_mail import Mail, Message
from .forms import NewRec


#it is a sample view to test a sample JSON File with flask. as i am not very familiar with JSON i am trying an example

@app.route('/', methods=['GET','POST'])
def load_all():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "adress.json")
    data = json.load(open(json_url))
    return render_template('viewall.html', data=data)


@app.route('/create_user', methods=['GET','POST'])
def create_record():
    form = NewRec()
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "adress.json")
    data = json.load(open(json_url))
    if form.validate_on_submit():
        for row in data:
            nid=row['id']
        newid = int(nid) + 1
        nid = str(newid)
        dictionary = {
        "id": nid,
        "first_name":form.fname.data,
        "last_name": form.lname.data,
        "phone":str(form.pno.data),
        "email":form.email.data
        }
        # Serializing json

        with open("app/static/adress.json", "r+") as f:
            data1=json.load(f)
        data1.append(dictionary)
            

        # Writing to our flat file, we append the new data from our form.
        with open("app/static/adress.json", "w") as outfile:
            json.dump(data1, outfile, indent=4,  separators=(',',': '))
            return redirect('/')
            
    return render_template('create.html', form=form)

@app.route('/delete/<id>', methods=['GET','POST'])
def delete_record(id):
    # SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    # json_url = os.path.join(SITE_ROOT, "static", "adress.json")
    # datas = json.load(open(json_url))
    with open("app/static/adress.json", "r+") as f:
        data1=json.load(f)
    # Iterate through the objects in the JSON and pop (remove)                      
    # the obj once we find it.                                                      
    for i in range(len(data1)):
        if data1[i]["id"] == id:
            data1.pop(i)
            break
    with open("app/static/adress.json", "w") as outfile:
        json.dump(data1, outfile, indent=4,  separators=(',',': '))            
    return redirect('/')   

    


@app.route('/view/<id>', methods=['GET','POST'])
def load_record(id):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "adress.json")
    datas = json.load(open(json_url))
    for row in datas:
        if row['id'] == id:
            p_row = row
    return render_template('userpage.html', data=p_row)
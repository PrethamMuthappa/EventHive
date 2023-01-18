from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///eventhive.db" #previous db name was todo.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class user(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    last_name=db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phonenumber = db.Column(db.Integer,nullable=False)
    date_of_birth = db.Column(db.Integer, nullable=False)
    passes = db.Column(db.String(100), nullable=False)
    seat = db.Column(db.String(100), nullable=False)
    events = db.Column(db.String(100), nullable=False)
   
   
    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}- {self.last_name}- {self.email} -{self.phonenumber} - {self.date_of_birth} -{self.passes} -{self.seat}-{self.events}"

@app.route('/')
def landingpage():
    return render_template('index.html')


@app.route('/tickets')
def tickets():
    return render_template('tickets.html')

@app.route('/events')
def allevents():
    return render_template('event.html')   

@app.route('/myshows')
def myshows():
    return render_template('myshows.html')     

   
@app.route('/form', methods=['GET', 'POST'])
def registration_Page():
    if request.method=='POST':
        name = request.form['name']
        last_name=request.form['last_name']
        email = request.form['email']
        phonenumber = request.form['phonenumber']
        date_of_birth = request.form['date_of_birth']
        passes=request.form['passes']
        seat=request.form['seat']
        events = request.form['events']
        eventhive = user(name=name,last_name=last_name, email=email,phonenumber=phonenumber,date_of_birth=date_of_birth,passes=passes,seat=seat, events=events)
        db.session.add(eventhive)
        db.session.commit()
        
    allevent = user.query.all()
    
    return render_template('form.html', allevent=allevent)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        name = request.form['name']
        last_name=request.form['last_name']
        email = request.form['email']
        phonenumber= request.form['phonenumber']
        date_of_birth=request.form['date_of_birth']
        passes=request.form['passes']
        seat=request.form['seat']
        events = request.form['events']
        eventhive = user.query.filter_by(sno=sno).first()
        eventhive.name = name
        eventhive.last_name = last_name
        eventhive.email =email
        eventhive.phonenumber = phonenumber
        eventhive.date_of_birth=date_of_birth
        eventhive.passes=passes
        eventhive.seat=seat
        eventhive.events = events
        
        db.session.add(eventhive)
        db.session.commit()
        return redirect("/")
        
    eventhive = user.query.filter_by(sno=sno).first()
    return render_template('update.html', eventhive=eventhive)


@app.route('/delete/<int:sno>')
def delete(sno):
    eventhive = user.query.filter_by(sno=sno).first()
    db.session.delete(eventhive)
    db.session.commit()
    return redirect("/table")
    

@app.route('/table')
def products():
    allevent = user.query.all()
    print(allevent)
    return render_template('table.html', allevent=allevent)

######################################### CUSTOM BOOKING SECTION #################################### 

class custom(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    cusname=db.Column(db.String(100),nullable=False)
    cusemail=db.Column(db.String(100),nullable=False)
    cusphone=db.Column(db.Integer,nullable=False)
    cus=db.Column(db.String(300),nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno}-{self.cusname} - {self.cusemail} -{self.cusphone}-{self.cus} "


@app.route('/customs',methods=['GET','POST'])
def custombookings():
    if request.method=='POST':
        cusname=request.form['cusname']
        cusemail=request.form['cusemail']
        cusphone=request.form['cusphone']
        cus=request.form['cus']
        eventhive=custom(cusname=cusname,cusemail=cusemail,cusphone=cusphone,cus=cus)
        db.session.add(eventhive)
        db.session.commit()

    allcustom=custom.query.all()
    return render_template('customs.html',allcustom=allcustom)

@app.route('/custable')
def customtables():
    allcustom=custom.query.all()
    print(allcustom)
    return render_template('customtable.html',allcustom=allcustom)       

@app.route('/cusupdate/<int:sno>', methods=['GET', 'POST'])
def cusupdate(sno):
    if request.method=='POST':
        cusname = request.form['cusname']
        cusemail = request.form['cusemail']
        cusphone= request.form['cusphone']
        cus=request.form['cus']
        eventhive = custom.query.filter_by(sno=sno).first()
        eventhive.cusname=cusname
        eventhive.cusemail=cusemail
        eventhive.cusphone=cusphone
        eventhive.cus=cus

        db.session.add(eventhive)
        db.session.commit()
        return redirect("/")
        
    eventhive = custom.query.filter_by(sno=sno).first()
    return render_template('cusupdate.html', eventhive=eventhive)

@app.route('/cusdelete/<int:sno>')
def cusdelete(sno):
    eventhive = custom.query.filter_by(sno=sno).first()
    db.session.delete(eventhive)
    db.session.commit()
    return redirect("/custable")


######################################### FEED BACK ################################################

class feedback(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    feedname=db.Column(db.String(50),nullable=False)
    food=db.Column(db.String(50),nullable=False)
    saftey=db.Column(db.String(50),nullable=False)
    parking=db.Column(db.String(50),nullable=False)
    visibility=db.Column(db.String(50),nullable=False)

    def __repr__(self) -> str:
        return f" {self.sno} - {self.feedname} - {self.food} - {self.saftey} -{self.parking} -{self.visibility} "


@app.route('/feedform', methods=['GET','POST'])
def feeddata():
    if request.method=='POST':
        feedname=request.form['feedname']
        food=request.form['food']
        saftey=request.form['saftey']
        parking=request.form['parking']
        visibility=request.form['visibility']

        eventhive=feedback(feedname=feedname,food=food,saftey=saftey,parking=parking,visibility=visibility)
        db.session.add(eventhive)
        db.session.commit()

    allfeed=feedback.query.all()
    return render_template('feedpage.html',allfeed=allfeed)

@app.route('/feedtable')
def newfeedtable():
    allfeed=feedback.query.all()
    print(allfeed)
    return render_template('feedtable.html',allfeed=allfeed)

@app.route('/feedupdate/<int:sno>',methods=['GET','POST'])
def upfeed(sno):
    if request.method=='POST':
        feedname=request.form['feedname']
        food=request.form['food']
        saftey=request.form['saftey']
        parking=request.form['parking']
        visibility=request.form['visibility']
        eventhive=feedback.query.filter_by(sno=sno).first()
        eventhive.feedname=feedname
        eventhive.food=food
        eventhive.saftey=saftey
        eventhive.parking=parking
        eventhive.visibility=visibility

        db.session.add(eventhive)
        db.session.commit()
        return redirect("/")

    eventhive=feedback.query.filter_by(sno=sno).first()
    return render_template('feedupdates.html',eventhive=eventhive)


@app.route('/feeddelete/<int:sno>')
def feeddelete(sno):
    eventhive = feedback.query.filter_by(sno=sno).first()
    db.session.delete(eventhive)
    db.session.commit()
    return redirect("/feedtable")

############################################## BILLING ##################################################################

class payment(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    cardno=db.Column(db.Integer,nullable=False)
    date=db.Column(db.String(20),nullable=False)
    cvv=db.Column(db.Integer,nullable=False)
    cname=db.Column(db.String(20),nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno}-{self.cardno} - {self.date} - {self.cvv} -{self.cname}"



@app.route('/billform',methods=['GET','POST'])
def bii():
    if request.method=='POST':

        cardno=request.form['cardno']
        date=request.form['date']
        cvv=request.form['cvv']
        cname=request.form['cname']

        eventhive=payment(cardno=cardno,date=date,cvv=cvv,cname=cname)
        db.session.add(eventhive)
        db.session.commit()
    allbill=payment.query.all()
    return render_template('billingform.html',allbill=allbill)    


@app.route('/tablebill')
def newbilltable():
    allbill=payment.query.all()
    print(allbill)
    return render_template('billtable.html',allbill=allbill)
    
########################################### admin ####################################################

class admin(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),nullable=False)
    password=db.Column(db.Integer,nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.username} - {self.password}"


@app.route('/adminmain',methods=['GET','POST'])
def adminlogin():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']

        eventhive=admin(username=username,password=password)
        db.session.add(eventhive)
        db.session.commit()

    alladmin=admin.query.all()
    
    
    return render_template('adminnew.html',alladmin=alladmin)
    
    

@app.route('/admintable')
def addtable():
    alladmin=admin.query.all()
    print(alladmin)
    return render_template('admintable.html',alladmin=alladmin)    



if __name__ == "__main__":
    app.run(debug=True, port=8000)
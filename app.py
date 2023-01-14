from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///eventhive.db" #previous db name was todo.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Event(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    last_name=db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(500), nullable=False)
    phonenumber = db.Column(db.Integer,nullable=False)
    date_of_birth = db.Column(db.Integer, nullable=False)
    passes = db.Column(db.String(500), nullable=False)
    seat = db.Column(db.String(500), nullable=False)
    events = db.Column(db.String(500), nullable=False)
   
   

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
        eventhive = Event(name=name,last_name=last_name, email=email,phonenumber=phonenumber,date_of_birth=date_of_birth,passes=passes,seat=seat, events=events)
        db.session.add(eventhive)
        db.session.commit()
        
    allevent = Event.query.all()
    
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
        eventhive = Event.query.filter_by(sno=sno).first()
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
        
    eventhive = Event.query.filter_by(sno=sno).first()
    return render_template('update.html', eventhive=eventhive)


@app.route('/delete/<int:sno>')
def delete(sno):
    eventhive = Event.query.filter_by(sno=sno).first()
    db.session.delete(eventhive)
    db.session.commit()
    return redirect("/table")



    

@app.route('/table')
def products():
    allevent = Event.query.all()
    print(allevent)
    return render_template('table.html', allevent=allevent)    

if __name__ == "__main__":
    app.run(debug=True, port=8000)
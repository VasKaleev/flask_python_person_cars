from flask import Flask, request, redirect, render_template
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
from project.forms import ProfileFormPerson, ProfileFormCar
from config import Config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)
db = SQLAlchemy(app)

class Persons(db.Model):
    __tablename__ = 'Persons'
    Id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String)
    Age = db.Column(db.Integer)

class Cars(db.Model):
    __tablename__ = 'Cars'
    Id = db.Column(db.Integer, primary_key = True)
    Brand = db.Column(db.String)
    Model = db.Column(db.String)
    PersonId = db.Column(db.Integer, db.ForeignKey('Persons.Id'))

@app.route('/')
def home():
    tables = {'persons': Persons.query.all(), 'cars': Cars.query.all()}
    return render_template('home.html', tables = tables)

@app.route('/add/person', methods = ['GET','POST'])
def add_person():
    name = ''
    age = ''
    form = ProfileFormPerson()
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        print(name)
        print(age)
        person = Persons(Name = name, Age = age)
        db.session.add(person)
        db.session.commit()
        return redirect('/')
    return render_template(
           'person.html',
           form=form,
           name = name,
           age = age)

@app.route('/delete/person/<int:id>', methods = ['GET','POST'])
def delete_person(id):
    cars = Cars.query.filter_by(PersonId=id)
    for car in cars:
        db.session.delete(car)
    person = Persons.query.get(id)
    db.session.delete(person)
    db.session.commit() 
    #person = Persons.query.get(id)
    #db.session.delete(person)
    #db.session.commit()
    return redirect('/')
    

@app.route('/add/car', methods = ['GET','POST'])
def add_car():
    brand = ''
    model = ''
    person_id=''
    form = ProfileFormCar()
    if form.validate_on_submit():
        brand  = form.brand.data
        model = form.model.data
        person_id = form.av.data
        print(brand)
        print(model)
        print(person_id)
        car = Cars(Brand = brand, Model = model, PersonId = person_id)
        db.session.add(car)
        db.session.commit()
        return redirect('/')
    return render_template(
           'car.html',
           form=form,
           brand = brand,
           model = model,
           person_id = person_id
           )

@app.route('/delete/car/<int:id>', methods = ['GET','POST'])
def delete_car(id):
    car = Cars.query.get(id)
    db.session.delete(car)
    db.session.commit()
    return redirect('/')
app.run(debug="True")

from flask import Flask, render_template
from mongoengine import *


app = Flask(__name__)

connect('web3Project')

class User(Document):
    email = StringField()
    first_name = StringField()
    last_name = StringField()

class countrydetails(Document):
    country = StringField()
    population = StringField()
    
   
@app.route('/testinspiration')
def testinspiration():
    return 'This is inspiration page!'
	
	#returns a template
@app.route('/')
@app.route("/index")
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/user')
def home():
    User(email="adhis7@student.op.ac.nz", first_name="Suresh123", last_name="Adkikari").save()
    return render_template("index.html")

@app.route('/country')
def country():
    countrydetails(country="New Zealand", population="48,000,00").save()
    return render_template("index.html")

# @app.route('/countryloop')
# def countrylist():
#     countries("New Zealand", "Austrila", "Maldives").save()
#     for country in countries: 
#     return render_template("index.html")

	
@app.route("/listUserTest")
def listUserTest():
    return User.objects.to_json()

@app.route("/inspiration")
def inspiration():
    return render_template("inspiration.html")

	

if __name__ =="__main__":
    app.run(host='0.0.0.0', port=80)
    
    


 
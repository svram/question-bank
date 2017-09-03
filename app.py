from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, jsonify, session
from werkzeug import secure_filename
import os
import random

#UNCOMMENT IN PRODUCTION SERVER
#from flask_heroku import Heroku


# create the application object
app = Flask(__name__)
app.config.from_object('_config')

#UNCOMMENT IN PRODUCTION SERVER
#heroku = Heroku(app)

db = SQLAlchemy(app)

class Card(db.Model):

	#__tablename__ = 'cards'

	qid = db.Column('id',db.Integer, primary_key=True)
	typeq = db.Column('type',db.Integer)
	front = db.Column('front',db.String())
	back = db.Column('back',db.String())
	known = db.Column('known',db.Boolean)

	def __init__(self, qid, typeq, front, back, known):
		self.qid = qid
		self.typeq = typeq
		self.front = front
		self.back = back
		self.known = known

	def __repr__(self):
		return "Question {0}".format(self.front)


#####-ROUTING-#####
###################

@app.route('/')
def index():
	random_card = Card.query.filter_by(qid=random.randint(1, 1793)).first()
	return render_template('index.html')
	

@app.route('/random')
def random_question():
	random_card = Card.query.filter_by(qid=random.randint(1, 1793)).first()
	return jsonify([random_card.front, random_card.back]);

if __name__ == '__main__':
	app.run(debug=True)



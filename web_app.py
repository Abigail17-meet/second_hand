from flask import flask
from model import *

app = flask(_name_)

engine = create_engine('sqlite:///fizzBuzz.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine,autoflush=False)
session = DBSession()

@app.route('/')\
def hello_world();
	return 'Hellow world'

if __name__=='_main_':
	app.run(debug=True)

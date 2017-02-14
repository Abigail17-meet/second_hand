
from flask import Flask, url_for, flash, render_template, redirect, request, g, send_from_directory
from flask import session as login_session
from model import *
from werkzeug.utils import secure_filename
import locale, os

app = Flask(__name__)
app.secret_key = "mu_secret_key"


engine = create_engine('sqlite:///Second_hand.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine, autoflush=False)

session = DBSession()





@app.route('/')
@app.route('/homepage')
def homepage():
	items = session.query(Item).all()
	return render_template('homepage.html', items=items)


@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		if email is None or password is None:
			flash('Missing Arguments')
			return redirect(url_for('login'))
		if verify_password(email, password):
			customer = session.query(Customer).filter_by(email=email).one()
			flash('Login Successful, welcome, %s' % customer.name)
			login_session['name'] = customer.name
			login_session['email'] = customer.email
			login_session['id'] = customer.id
			return redirect(url_for('inventory'))
		else:
			# incorrect username/password
			flash('Incorrect username/password combination')
			return redirect(url_for('login'))

@app.route('/newCustomer', methods = ['GET','POST'])
def newCustomer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        customer = Customer(name=name,email=email,address=address )
        customer.hash_password(password)
        session.commit()
        if name is None or email is None or password is None or 'file' not in request.files:
            flash("Your form is missing arguments")
            return redirect(url_for('newCustomer'))
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('newCustomer'))
        if session.query(Customer).filter_by(email = email).first() is not None:
            flash("A user with this email address already exists")
            return redirect(url_for('newCustomer'))
        if file and allowed_file(file.filename):
            customer = Customer(name = name, email=email, address = address)
            customer.hash_password(password)
            session.add(customer)
            session.commit()
            filename = str(customer.id) + "_" + secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            customer.set_photo(filename)
            session.add(customer)
            shoppingCart = ShoppingCart(customer=customer)
            session.add(shoppingCart)
            session.commit()
            flash("User Created Successfully!")
            return redirect(url_for('inventory'))
        else:
        	flash("Please upload either a .jpg, .jpeg, .png, or .gif file.")
        	return redirect(url_for('newCustomer'))
    else:
        return render_template('homepage.html')

def verify_password(email, password):
	customer = session.query(Customer).filter_by(email=email).first()
	if not customer or not customer.verify_password(password):
		return False
	g.customer = customer
	return True

if __name__ == '__main__':
	print("In Here!")
	app.run(debug=True)

#@app.route('/')\
#def hello_world();
#	return 'Hellow world'

if __name__=='_main_':
	app.run(debug=True)


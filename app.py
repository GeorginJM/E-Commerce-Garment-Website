from flask import Flask, render_template, request,redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
app.secret_key = 'your-secret-key'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index1():
    return render_template('index1.html', login_error='')

@app.route('/purchase')
def purchase():
    return render_template('purchase.html')

@app.route('/custom')
def custom():
    return render_template('custom.html')

@app.route('/custom1')
def custom1():
    return render_template('custom1.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('index1.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sproduct')
def sproduct():
    return render_template('sproduct.html')

@app.route('/sproduct1')
def sproduct1():
    return render_template('sproduct1.html')

@app.route('/sproduct2')
def sproduct2():
    return render_template('sproduct2.html')

@app.route('/sproduct3')
def sproduct3():
    return render_template('sproduct3.html')

@app.route('/sproduct4')
def sproduct4():
    return render_template('sproduct4.html')

@app.route('/sproduct5')
def sproduct5():
    return render_template('sproduct5.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['login-username']
    password = request.form['login-password']

    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        # Login validation succeeded
        return render_template('index.html')
    else:
        # Login validation failed
        return render_template('index1.html', login_error='Invalid login credentials', signup_error='')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['signup-username']
    password = request.form['signup-password']

    user = User.query.filter_by(username=username).first()

    if user:
        # User with the same username already exists
        return render_template('index1.html', login_error='', signup_error='Username already taken')

    # Create a new user record
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    # Signup validation succeeded
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

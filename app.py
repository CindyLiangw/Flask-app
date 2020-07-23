from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a747c18413804fd39619a626bfdc0d4a'

posts = [
    {
        'author' : 'Harry Potter',
        'title' : 'Me and the Dark Lord',
        'content' : 'First post content',
        'date_posted' : 'April 20, 2020'
    },
    {
        'author' : 'Barty Crouch.Jr',
        'title' : 'How to brew the polyjuice',
        'content' : 'Second post content',
        'date_posted' : 'April 20, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Welcome~!')

@app.route('/about')
def about():
    return render_template('about.html', title='About Cindy')
    
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

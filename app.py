from flask import Flask, send_from_directory
from flask import render_template, url_for, redirect
from flask import request
from flask_cors import CORS
from models import create_post, get_posts
from forms import RegistrationForm, LoginForm
from flask import flash


app = Flask(__name__)

CORS(app)

app.config['SECRET_KEY'] = 'b5e1e67009bc5fe76b54aa79d0ad9b5f'

@app.route('/')
@app.route('/home/', methods=['GET', 'POST'])
def home():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)

    posts = get_posts()

    return render_template('home.html', posts=posts)

@app.route('/register/', methods = ["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)


@app.route('/login/', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You are logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Unsuccessful Login Attempt. Please Check Username and Password', 'danger')
    return render_template('login.html', title = 'Login', form=form)





if __name__ == '__main__':
    app.run(debug=True)

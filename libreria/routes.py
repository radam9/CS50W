from flask import render_template, request, url_for, flash, redirect, session
from libreria import app, db, bcrypt
#import forms from forms.py in root
from libreria.forms import RegForm, LoginForm, ReviewForm, SearchForm
from libreria.models import User, Book, Review
from flask_login import login_user, current_user, logout_user, login_required
import json


@app.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.ultimateuser(username=form.username.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main'))
        else:
            flash('Invalid credentials! if your not a user please Sign Up first.')
    return render_template('index.html', title='Book Reviews', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = RegForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_pw)
        #combine the .create and .search in the user class
        user.create()
        user.search()
        flash(f'{form.username.data}, your account has been created!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Sign Up', form=form)

@app.route("/main")
@login_required
def main():
    return render_template('main.html', title='Book Reviews')

@app.route("/book", methods=['GET', 'POST'])
@login_required
def book():
    form = ReviewForm()
    if form.validate_on_submit():
        flash('Your review has been submitted!', 'success')
        review = Review.create(review=form.review.data, rating=form.rating.data, bookid=900, userid=current_user.id)
        return redirect(url_for('main'))
    return render_template('book.html', title='Book Title', form=form)

@app.route("/reviews")
@login_required
def reviews():
    reviews = Review.revsearchuid(current_user.id)
    return render_template('reviews.html', title='My Reviews', reviews=reviews)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
    # I need to redirect the user from the logout.html to login.html
    # return render_template('logout.html', title='Logging Out')

@app.route("/search", methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    if form.validate_on_submit():
        if form.type.data == 'title':
            session['books'] = Book.searchtitle(title=form.search.data)
        elif form.type.data == 'isbn':
            session['books'] = Book.searchisbn(isbn=form.search.data)
        elif form.type.data == 'author':
            session['books'] = Book.searchauthor(author=form.search.data)
        return redirect(url_for('results'))

    return render_template('temp.html', title='Book Search Results', form=form)

@app.route("/results")
@login_required
def results():
    sbooks = session['books']
    temp = list()
    for b in sbooks:
        temp.append(json.loads(b))
    books = list()
    for t in temp:
        books.append(Book(t[0], t[1], t[2], t[3], t[4]))
    return render_template('search.html', title='Book Search Results', books=books)

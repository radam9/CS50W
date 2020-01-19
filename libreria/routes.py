from flask import render_template, request, url_for, flash, redirect, session, abort, jsonify
from libreria import app, db, bcrypt
#import forms from forms.py in root
from libreria.forms import RegForm, LoginForm, ReviewForm, SearchForm
from libreria.models import User, Book, Review
#importing the goodreads funtion to get review count and average rating
from libreria.funcs import goodreads
from flask_login import login_user, current_user, logout_user, login_required
import json


@app.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('search'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.ultimateuser(username=form.username.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('search'))
        else:
            flash('Invalid credentials! if your not a user please Sign Up first.')
    return render_template('login.html', title='Book Reviews', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('search'))
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


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/search", methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    session['searchresult'] = form.search.data
    if form.validate_on_submit():
        if form.type.data == 'title':
            session['books'] = Book.bsearchtitle(title=form.search.data)
        elif form.type.data == 'isbn':
            session['books'] = Book.bsearchisbn(isbn=form.search.data)
        elif form.type.data == 'author':
            session['books'] = Book.bsearchauthor(author=form.search.data)
        return redirect(url_for('results'))
    return render_template('search.html', title='Search for books', form=form)

@app.route("/results")
@login_required
def results():
    sbooks = session['books']
    searchresult = session['searchresult']
    temp = list()
    for b in sbooks:
        temp.append(json.loads(b))
    books = list()
    for t in temp:
        books.append(Book(t[0], t[1], t[2], t[3], t[4]))
    return render_template('results.html', title='Book search results', books=books, searchresult=searchresult)

@app.route("/book/<int:bookid>", methods=['GET', 'POST'])
@login_required
def book(bookid):
    session['book'] = Book.bsearchid(bookid)
    if session['book'] == None:
        abort(404)
    else:
        temp = json.loads(session['book'])
        book = Book(temp[0], temp[1], temp[2], temp[3], temp[4])

    ureview = Review.revsearch(current_user.id, bookid)
    form = ReviewForm()
    if form.validate_on_submit():
        if ureview == None:
            review = Review.create(review=form.review.data, rating=form.rating.data, bookid=book.id, userid=current_user.id)
            session['revmsg'] = 1#value used to notify the review submit page that a review hasn't been submitted for this book by the user.
            return redirect(url_for('revsubmit'))
        else:
            session['revmsg'] = 0#value used to notify the review submit page that a review has been submitted for this book by the user.
            return redirect(url_for('revsubmit'))

    breview, count = Review.revsearchbid(bookid)
    total = 0
    if count == 0:
        avgrating = 0
    elif count == 1:
        avgrating = breview[0].rating
    else:
        for b in breview:
            total += b.rating
        avgrating = total/count
        avgrating = round(avgrating,2)

    goodread = goodreads(book.isbn)
    gcount = goodread[0]
    grating = goodread[1]
    return render_template('book.html', title='Book Title', form=form, book=book, ureview=ureview, count=count, avgrating=avgrating, grating=grating, gcount=gcount)

@app.route("/reviews")
@login_required
def reviews():
    revs = Review.revsearchuid(current_user.id)
    books = list()
    for r in revs:
        book = json.loads(Book.bsearchid(r.bookid))
        books.append(Book(book[0], book[1], book[2], book[3], book[4]))
    return render_template('reviews.html', title='My Reviews', reviews=zip(books,revs))

@app.route("/review_submit")
@login_required
def revsubmit():
    temp = json.loads(session['book'])
    book = Book(temp[0], temp[1], temp[2], temp[3], temp[4])
    return render_template('message.html', title='Review submission', message=session['revmsg'], book=book)

@app.route("/api/<isbn>")
@login_required
def api(isbn):
    b = Book.bsisbn(isbn)
    if b == None:
        abort(404, description="Book not found")
    else:
        temp = json.loads(b)
        book = Book(temp[0], temp[1], temp[2], temp[3], temp[4])
    brev, count = Review.revsearchbid(book.id)
    if count == 0:
        rating = 0
    else:
        rating = float(brev[0].rating)

    r = {}
    r['title'] = book.title
    r['author'] = book.author
    r['year'] = book.year
    r['isbn'] = book.isbn
    r['review_count'] = count
    r['average_rating'] = rating
    jr = jsonify(r)

    return jr, 200

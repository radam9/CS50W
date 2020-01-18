from libreria import db, login_manager
from flask_login import UserMixin
import json


@login_manager.user_loader
def load_user(user_id):
    return User.ultimateid(id=user_id)

class User(UserMixin):

    def __init__(self, username, password=None, id=None):
        self.username = username
        self.password = password
        self.id = id

    def create(self):
        db.session.execute("INSERT INTO users (username, password) VALUES (:username, :password)", {"username": self.username, "password": self.password})
        db.session.commit()


    def search(self):
        response = db.session.execute("SELECT id,username,password FROM users WHERE username = :username", {"username":self.username}).fetchone()
        if response != None:
            self.id = response[0]
            self.password = response[2]
        return response

    @classmethod
    def ultimateid(cls, id):
        response = db.session.execute("SELECT * FROM users WHERE id = :id", {"id":id}).fetchone()
        return cls(response[1], response[2], response[0])

    @classmethod
    def ultimateuser(cls, username):
        response = db.session.execute("SELECT id,username,password FROM users WHERE username = :username", {"username":username}).fetchone()
        if response == None:
            return None
        else:
            return cls(response[1], response[2], response[0])

    def __str__(self):
        return f'The user: {self.username}, has an ID: {self.id}'


class Book():

    def __init__(self, id, isbn, title, author, year):
        self.id = id
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    @staticmethod
    def bsearchisbn(isbn):
        response = db.session.execute("SELECT * FROM books WHERE isbn LIKE :isbn", {"isbn": "%" + isbn + "%"}).fetchall()
        books=list()
        if response != None:
            for r in response:
                books.append(json.dumps(tuple(r)))
            return books
        else:
            return None

    @staticmethod
    def bsearchtitle(title):
        response = db.session.execute("SELECT * FROM books WHERE title LIKE :title", {"title": "%" + title + "%"}).fetchall()
        books=list()
        if response != None:
            for r in response:
                books.append(json.dumps(tuple(r)))
            return books
        else:
            return None

    @staticmethod
    def bsearchauthor(author):
        response = db.session.execute("SELECT * FROM books WHERE author LIKE :author", {"author": "%" + author + "%"}).fetchall()
        books=list()
        if response != None:
            for r in response:
                books.append(json.dumps(tuple(r)))
            return books
        else:
            return None

    @staticmethod
    def bsearchid(id):
        r = db.session.execute("SELECT * FROM books WHERE id = :id", {"id":id}).fetchone()
        if r != None:
            return json.dumps(tuple(r))
        else:
            return None

    @staticmethod
    def bsisbn(isbn):
        r = db.session.execute("SELECT * FROM books WHERE isbn = :isbn", {"isbn":isbn}).fetchone()
        if r != None:
            return json.dumps(tuple(r))
        else:
            return None

    def updaterating(self,rating):
        '''
        update the rating through the review class, and it should get the avg ratings for a single book after each rating update and send that information over to "book.rating"
        '''
        pass

class Review():

    def __init__(self, id, review, rating, bookid, userid):
        self.id = id
        self.review = review
        self.rating = rating
        self.bookid = bookid
        self.userid = userid

    @classmethod
    def create(cls, review, rating, bookid, userid):
        db.session.execute("INSERT INTO reviews (review, rating, books_id, users_id) VALUES (:review, :rating, :bookid, :userid)", {"review":review, "rating":rating, "bookid":bookid, "userid":userid})
        db.session.commit()
        r = db.session.execute("SELECT id FROM reviews WHERE books_id = :bookid AND users_id = :userid", {"bookid":bookid, "userid":userid}).fetchone()
        return cls(r[0], review, rating, bookid, userid)

    @staticmethod
    def revsearchuid(userid):
        response = db.session.execute("SELECT * FROM reviews WHERE users_id = :userid", {"userid": userid}).fetchall()
        reviews = list()
        if response != None:
            for r in response:
                reviews.append(Review(r[0], r[1], r[2], r[3], r[4]))
            return reviews
        else:
            return None

    @staticmethod
    def revsearchbid(bookid):
        response = db.session.execute("SELECT * FROM reviews WHERE books_id = :bookid", {"bookid": bookid}).fetchall()
        reviews = list()
        count = 0
        if response != None:
            for r in response:
                count += 1
                reviews.append(Review(r[0], r[1], r[2], r[3], r[4]))
            return reviews, count
        else:
            return None

    @staticmethod
    def revsearch(userid, bookid):
        r = db.session.execute("SELECT * FROM reviews WHERE users_id = :userid AND books_id = :bookid", {"userid": userid, "bookid": bookid}).fetchone()
        if r != None:
            return Review(r[0], r[1], r[2], r[3], r[4])
        else:
            return None

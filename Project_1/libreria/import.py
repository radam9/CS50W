import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://oijlbnofzvlluw:b06ac42f7be0fc4c1427c3c010323d6034387520cca39fdca8f9a7400ac3cdb9@ec2-54-247-72-30.eu-west-1.compute.amazonaws.com:5432/deuk0ndr5rg90v')
db = scoped_session(sessionmaker(bind=engine))


def main():
    #Creating the books table with colums; id, isbn, title, author, year.
    db.execute("CREATE TABLE books(id SERIAL PRIMARY KEY, isbn VARCHAR NOT NULL, title VARCHAR NOT NULL, author VARCHAR NOT NULL, year INTEGER NOT NULL)")
    #Creating the users table with colums; id, username, password.
    db.execute("CREATE TABLE users(id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, password VARCHAR NOT NULL)")
    #Creating the reviews table with columns, id, review, rating, book id, user id
    db.execute("CREATE TABLE reviews(id SERIAL PRIMARY KEY, review VARCHAR NOT NULL, rating DECIMAL DEFAULT '0', books_id INTEGER REFERENCES books NOT NULL, users_id INTEGER REFERENCES users NOT NULL)")

    f = open("books.csv", mode="r")
    r = csv.reader(f)
    next(r, None)
    #reading the books.csv rows 1 at a time and inserting them into the books table
    for isbn, title, author, year in r:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn":isbn, "title":title, "author":author, "year":year})
    db.commit()

if __name__ == "__main__":
    main()

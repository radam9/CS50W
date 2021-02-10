import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///books.db')
db = scoped_session(sessionmaker(bind=engine))


def main():
    #Creating the books table with colums; id, isbn, title, author, year.
    db.execute("create table books (id integer primary key autoincrement not null, isbn varchar not null, title varchar not null, author varchar not null, year int not null)")
    #Creating the users table with colums; id, username, password.
    db.execute("create table users (id integer primary key autoincrement not null, username varchar not null, password varchar not null)")
    #Creating the reviews table with columns, id, review, rating, book id, user id
    db.execute("create table reviews (id integer primary key autoincrement not null, review varchar not null, rating decimal default '0', books_id int not null, users_id int not null, foreign key (books_id) references books, foreign key (users_id) references users)")

    with open("books.csv", mode="r") as f:
        r = csv.reader(f)
        next(r, None)
        #reading the books.csv rows 1 at a time and inserting them into the books table
        for isbn, title, author, year in r:
            db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                        {"isbn":isbn, "title":title, "author":author, "year":year})
    db.commit()

if __name__ == "__main__":
    main()

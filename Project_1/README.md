# Project 1

CS50W - Web Programming with Python and JavaScript

This is project1's repo.
It contains the code and files for project1, which is a website based project to practice the basics of Python, Flask and SQL.
The application is packaged and is launched using  ``` run.py``` in the main directory.
### The project directory looks as follows:
```bash
───Project1
   └───libreria
       ├───static
       │   ├───images
       │   └───styles
       └───templates
```

####	The ``Project1`` folder contains the following files:

- README.md  

- requirements.txt > contains the required python packages for this project.

- resources.txt > contains the sources of images and other resources using for the website.

- run.py > main app launching file.

#### The ``libreria`` folder contains:

-  _ _init__.py > main application initialization file, contains the app.config parameters as well as db initialization.

- books.csv > provided csv with list of books and info.

- errors.py > The errorhandler for the 404 page.

- form.py > The Flask-WTForms code to get the user input from various pages.
- funcs.py > Goodreads api function to get book ratings count and average rating.
- import.py > Initializes the database by creating 3 tables: books, users and reviews. It also imports the contents of ``books.csv`` into the database books table.
- models.py > The User, Book and Review classes as well as relevant methods.
- routes.py > The Flask app routes.

#### The ``static`` folder contains:
- ``images`` folder that contains images used in the webpage.
- ``styles`` folder that contains all the css for the webpage.
#### The ``templates`` folder contains all relavent html files.


### Project1 requirements check list:

- [x] **Login page:** login functionality, existing user in db check and correct password check.
- [x] **Register page:** register functionality, existing username check and required input check.
- [x] **Logout:** Logout button on the navigation bar, logs out the user and redirects to the Login page.
- [x] **Import:** ``import.py`` Create database tables and import ``books.csv`` to the database.
- [x] **Search:** Once the user is logged in, the are redirected to a search page where they can search for books by title, author or isbn (part of title/author/isbn also works). After the search, the user is redirected to a results page showing the results of his or her search or a message showing "No Results".
- [x] **Book Page:** Clicking on a book from either "results page" or "my reviews page" will redirect the user to a page containing the book details and user reviews.
- [x] **Review Submission:** On the book page the user can submit a review with score 1 to 5 and a text component. The user can't submit a review to the same book twice.
- [x] **Goodreads Review Data:** On the book page, the goodreads review count and average rating are included using goodreads api.
- [x] **API Access:** If the user makes a GET request to ``/api/<isbn>`` they are given a JSON response with the book info, they are given a 404 error if the isbn is not found.

- [x] SQLAlchemy ORM not used.

- [x] Python packages used to run the application included in ``requirements.txt``.
- [x] ``README.md`` file containing
  - [x] project description
  - [x] contents of each file
  - [x] (optional) any aditional info

# CS50W - Web Programming with Python and JavaScript

This Repository contains the content [Lectures, Notes, Source Code, Projects] for the course CS50W - Web Programming with Python and JavaScript.

There was a lot to learn from the course:
- HTML
- CSS (Bootstrap)
- Python (Flask, Django, VirtualEnvironments, Packaging)
- Testing (Pytest, Unittest, Mock, Django Test)
- SQL (ORM, Migrations, SQLite3, Postgresql)
- Javascript (AJAX, handlebars, amcharts)
- Templates (Mustache, Jinja2)
- CI/CD (TravisCI, Git, Github, Github Actions, Heroku, Docker)
- Security (SQL Injection, API Keys and Authentication, Cross-Site Scripting, CSRF, Environmental Variables)

The course included 5 projects in total, they are all currntly hosted on [Heroku](https://www.heroku.com).

- [**Project_0:**](Project_0) 
  - Description: Simple static website that is mobile responsive.
  - Tech: CSS, HTML, Bootstrap
  
- [**Project_1:**](Project_1)
  - Description: Book library built using Flask, it allows users to, comment, rate and review books. It has an API for requesting book information using the `ISBN`. It fetches the current ratings from [goodreads' API](https://www.goodreads.com) and the book cover from [openlibrary](https://openlibrary.org/)
  - Tech: Flask, SQLite3, SQLAlchemy, requests, Bootstrap, BCrypt
  - Link: [libreria-a.herokuapp.com](https://libreria-a.herokuapp.com)
  
- [**Project_2:**](Project_2)
  - Description: Flask and SocketIO chat app. It allows the user to create new chat rooms and chat with users.
  - Tech: Flask, SocketIO, Javascript, Handlebars
  - Link: [flack-a.herokuapp.com](https://flack-a.herokuapp.com)
  
- [**Project_3:**](Project_3)
  - Descroption: Django webapp to handle a pizza store's online orders. It allows users to add items to a cart, place orders and track the status of their order.
  - Tech: Django, SQLite3, Javascript, Ajax, Bootstrap
  - Link: [pizza-a.herokuapp.com](https://pizza-a.herokuapp.com)
  
- [**Final_Project:**](Final_project)
  - Description: A Django webapp for drama series analytics. It allows the user to build a database of dramas they have watched from [MyDramaList](https://www.mydramalist.com), fetch the drama information from [MyDramaList](https://www.mydramalist.com) when adding it to the database. Using the users data, the main page shows a set of graphs and charts (using [javascript amcharts](https://www.amcharts.com)) giving insight to the users drama trends, preferences and style. It also allows the user to download his drama list as a `CSV` or `XLSX` file.
  - Tech: Django, Django REST Framework, SQLite3, Javascript, Ajax, Webscrapping (BeautifulSoup4), AMCharts, Bootstrap
  - Link: [dramas.herokuapp.com](https://dramas.herokuapp.com)

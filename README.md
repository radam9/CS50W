# Final Project
CS50W - Web Programming with Python and JavaScript

This is final-project's repo.

It contains the code and files for final-project, which is a website based project to practice what was learned in the CS50W course.

## Description:
The project ``Dramas`` is an analytical website, it has a list of dramas and its relevant info [rating, watch date, airing year, no. of episodes, duration of episodes, broadcasting station, and if the drama is a favorite].
The website consists of three pages ``Dashboard``, ``Drama List`` and ``Add Drama``.
The ``Dashboard`` is a page containing graphs and charts showing statistics related to the list of dramas in the database.
The ``Drama List`` is a page that shows the list of dramas in the database and allows the user to search through the dramas using filters as well and saving the results as a file [CSV or XLSX].
The ``Add Drama`` page allows you to add a drama to the database, you can enter a URL in the form that will enable the form to fetch relevant information from [MDL](www.mydramalist.com) and use it to fill the form.

------------

## Features:
- Accounts are issued by the administration, its not open for anyone to register.
- All website routes (API and Normal) require authentication (login).

------------

## This project was built with:
1. Python:
	- [Django](https://pypi.org/project/Django/ "Django")
	- [Django Rest Framework](https://pypi.org/project/djangorestframework/ "Django Rest Framework")
	-  [Django-filter](https://pypi.org/project/django-filter/ "Django-filter")
	- 	[Django-crispy-forms](https://pypi.org/project/django-crispy-forms/ "Django-crispy-forms")
	- 	[openpyxl](https://pypi.org/project/openpyxl/ "openpyxl")
	- 	[requests](https://pypi.org/project/requests/ "requests")
	- 	[beautifulsoup4](https://pypi.org/project/beautifulsoup4/ "beautifulsoup4")

2. JavaScript:
	- [amCharts 4](https://www.amcharts.com/ "amCharts 4")

3. Others:
	- [Alex Brush Google Font](https://fonts.google.com/specimen/Alex+Brush "Alex Brush Google Font")
	- [Bootstrap 4](https://getbootstrap.com/ "Bootstrap 4")
	- [Logo Maker](https://hatchful.shopify.com/)
------------


## Folders & Files structure:

```
Final-Project                                   # Project's main folder
|
|   .gitignore
|   db.sqlite3
|   manage.py
|   README.md
|   requirements.txt
|   
+---dramas
|       asgi.py
|       settings.py
|       urls.py
|       wsgi.py
|       __init__.py
|       
+---mydramas
|   |   admin.py
|   |   apps.py
|   |   filters.py                      # django-filter classes
|   |   forms.py
|   |   models.py
|   |   serializers.py                  # djangorestframework model serializers
|   |   tests.py
|   |   urls.py
|   |   views.py
|   |   __init__.py
|   |   
|   +---static
|   |   +---css                         # The template styling files
|   |   |       base.css
|   |   |       dashboard.css
|   |   |       dramalist.css
|   |   |       login.css
|   |   |       newdrama.css
|   |   |       
|   |   +---images                      # Folder containing logo images
|   |   |       logo.png
|   |   |       logo_transparent.png
|   |   |       
|   |   \---js
|   |           dashboard.js            # The JS file for the dashboard.html view
|   |           newdrama.js             # The JS file for the newdrama.html view
|   |           
|   \---templates
|       \---mydramas                    # The templates for the project
|               base.html
|               dashboard.html
|               dramalist.html
|               login.html
|               logout.html
|               navbar.html
|               newdrama.html
|               
\---myscripts                           # Folder containing helper files
        MDL.py                          # Import .xlsx to db, helper function to fetch info from www.mydramalist.com
        myinfo.xlsx                     # List of Drams and info to populate the database
```

------------


## Final Project requirements:
- [x] Your web application must be sufficiently distinct from the other projects in this course, and more complex than those.
- [x] Your web application must utilize at least two of Python, JavaScript, and SQL. Used:
	- [x] Python [Django, Django Rest Framework, Django-filter]
	- [x] Javascript [amCharts 4]
	- [x] SQL [SQLite3]
- [x] Your web application must be mobile-responsive.
- [x] In `README.md`, include a short writeup describing your project, what’s contained in each file you created or modified, and (optionally) any other additional information the staff should know about your project.
- [x] If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to `requirements.txt`

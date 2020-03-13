
# Project 3

  

CS50W - Web Programming with Python and JavaScript

  

This is project3's repo.

It contains the code and files for project3, which is a website based project to practice Django and Relational Database Design


### The project directory looks as follows:

```bash

───Project3

+---orders
|   +---migrations
|   +---static
|   |   +---css
|   |   +---images
|   |   \---js
|   \---templates
|       \---orders
+---pizza
\---users
    +---migrations
    +---static
    |   \---css
    \---templates
        \---users

```

  

#### The ``Project3`` folder contains the following files:

- README.md
- requirements.txt > contains the required python packages for this project.
- resources.txt > contains the sources of images and other resources using for the website.
- db.sqlite3 > the local SQLite dabase for the project.

  

#### The ``orders`` folder, which is the main app, contains:

- ``migrations`` folder > contains all the applied database/model migrations performed on the app.
- ``static`` folder > 3 folders (css, images, js) that contain the (stylesheets, images, javascript) respectively.
- ``templates`` folder > contains all the html files related to the order app.
- admin.py > contains the definition of the models to be shown in the admin page of the webpage.
- forms.py > contains the forms used in website.
- models.py > contains all the models used in the webapp.
- urls.py > contains all the routing for the orders app.
- views.py > contains all the route views for the orders app.

#### The ``pizza`` folder contains the settings and urls for the webapp.

#### The ``users`` folder, which is the app that handles user registration, login and logout, contains:

- ``static`` folder > contains a css folder that contains the stylesheets for the users app relevant html pages.
- ``templates`` folder > that contains the html pages relevant to the users app.
- forms.py > contains the user registration form.
- views.py > contains the route views for the users app.

### Project3 requirements check list:

- [x]  **Menu:** 
	- Support all menu items available in [Pinocchio's Pizza & Subs](http://www.pinocchiospizza.net/menu.html). 
	- Models added to ``orders/models.py``

- [x]  **Adding Items:** 
	- Add,Update and Remove items through Django's Admin site.
	- Add all the items from Pinocchio's menu to the database.

- [x]  **Registration, Login, Logout:** 
	- Users can register using (Username, Password, First Name, Last Name and Email Address).
	- Users can login and logout of the website.

- [x]  **Shopping Cart:** 
	- Logged-in users see the menu representation, where they can add items to their cart (with toppings or extras).
	- Shopping cart is saved when a user closes the window or relogs.

- [x]  **Placing an Order:** 
	- Once there is at least one item in the cart, users can place the order.
	- Users are asked to confirm the order before finalizing it.

- [x]  **Viewing Orders:** Site administrators should have access to a page where they can view any orders that have already been placed.

- [x]  **Personal Touch:** 
	- Administrators can mark orders as (Preparing, On Route, Delivered).
	- Users can see the status of all their orders.
	- Popup window when adding items to a cart, where the user can choose (toppings, size and quantity) showing the sub-total price.


- [x] Python packages used to run the application included in ``requirements.txt``.

- [x]  ``README.md`` file containing:
	- [x] project description
	- [x] contents of each file
	- [x] (optional) any aditional info

# Project 2

CS50W - Web Programming with Python and JavaScript

This is project2's repo.
It contains the code and files for project2, which is a chat app project to practice the following:

- Javascript
- Handlebars
- Websockets (socketio)
- Flask-Socketio

### The project directory looks as follows:

```bash
───Project2
├───static
└───templates
```

#### The `Project2` folder contains the following files:

- README.md
- requirements.txt > contains the required python packages for this project.
- gitignore.txt > contains the folders/files to be ignored by Git.
- application.py > main app launching file.

#### The `static` folder contains:

- BSmod.css > contains css code to modify the standard bootstrap primary color.
- index.css > contains the css for the chat app page.
- index.js > contains the main Javascript code used for the chat app.

#### The `templates` folder contains:

- index.html > contain the main html code for the chat app page.

### Project1 requirements check list:

- [x] **Display Name:** User prompt to enter "Display Name" upon first visit, The chat app doesn't forget the "Display Name" if the page gets closed or refreshed.

- [x] **Channel Creation:** Any user can create a channel as long as it's name doesn't conflict with an existing one.

- [x] **Channel List:** Channel list with channels, clicking on a channel will allow the user to join it.

- [x] **Messages View:** User sees past message upon joining a page. Max number of messages per channel is 100.

- [x] **Sending Messages:** Once in a channel users can send messages to others in the same channel. Messages contain (Username, Time stamp & Message text). Viewing sent messages doesn't require page reload.

- [x] **Remembering the Channel:** If the user closes the chat app window and revisits the webpage, they will be put back on the same page they were on previously.

- [x] **Personal Touch:** The following personal touches were added: - Website is a Single Page App design. - Display Name shown at the top of the page. - User Logout button and functionality added. - User is alerted if they create a channel with a name that already exists. - Users in the channel are notified when; a user joins the room, leaves the room, joins the server to that specific channel, disconnects from the server while in that channel. - Active channel is highlighted in the channel list. - The chat window automatically scrolls down to the most recent message.

* [x] Python packages used to run the application included in `requirements.txt`.

* [x] `README.md` file containing

      	- [x] project description

      	- [x] contents of each file

      	- [x] (optional) any aditional info

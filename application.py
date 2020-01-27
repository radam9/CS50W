from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = "The Strongest Secret Key Ever!"
app.config["SESSION_TYPE"] = "filesystem"
socketio = SocketIO(app)


clist = {"General": [], "Introduction": [], "Hobbies": []}
users = {}


@app.route("/")
def main():
    rooms = clist.keys()
    return render_template("index.html", rooms=rooms)


@app.route("/logout")
def logout(username):
    users.pop(username)
    return render_template("logout.html")


@socketio.on("eventconnect")
def onconnect(username):
    users[username] = request.sid
    print(f"\n\n{username} has connected\n\n")
    data = [username, request.sid]
    send(data)


@socketio.on("join")
def join(room_join):
    username = room_join["username"]
    room = room_join["room"]
    join_room(room)
    send(username + " has joined the room.", room=room)


@socketio.on("leave")
def leave(room_leave):
    username = room_leave["username"]
    room = room_leave["room"]
    leave_room(room)
    send(username + " has left the room.", room=room)


if __name__ == "__main__":
    socketio.run(app, debug=True)

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send, join_room, leave_room
from collections import deque

app = Flask(__name__)
app.config["SECRET_KEY"] = "The Strongest Secret Key Ever!"
app.config["SESSION_TYPE"] = "filesystem"
socketio = SocketIO(app)


clist = {"General": deque([], maxlen=100)}
ulist = {}


@app.route("/")
def main():
    return render_template("index.html")


@socketio.on("onconnect")
def onconnect(data):
    user = data["username"]
    room = data["activechannel"]
    ulist[user] = request.sid
    time = data["time"]
    join_room(room)
    users = list(ulist)
    rooms = list(clist)
    if clist[room]:
        active = list(clist[room])
        emit(
            "connected",
            {"code": "1", "users": users, "rooms": rooms, "msgs": active},
            broadcast=False,
            room=request.sid,
        )
    else:
        emit(
            "connected",
            {"code": "0", "users": users, "rooms": rooms},
            broadcast=False,
            room=request.sid,
        )
    emit(
        "msgupdate",
        {"user": "Server", "msg": user + ", has joined the server!", "time": time,},
        room=room,
    )


@socketio.on("ondisconnect")
def ondisconnect(data):
    user = data["username"]
    room = data["activechannel"]
    time = data["time"]
    ulist.pop(user)
    leave_room(room)
    emit(
        "msgupdate",
        {
            "user": "Server",
            "msg": user + ", has disconneted from the server!",
            "time": time,
        },
        room=room,
    )


@socketio.on("sendmsg")
def handle_msg(data):
    user = data["username"]
    msg = data["msg"]
    time = data["time"]
    room = data["activechannel"]
    clist[room].append({"user": user, "msg": msg, "time": time})
    emit(
        "msgupdate",
        {"user": user, "activechannel": room, "msg": msg, "time": time,},
        room=room,
    )


@socketio.on("createchannel")
def createroom(data):
    if data["channel"] in clist:
        emit(
            "confirmcreate",
            {"code": "0", "msg": "A channel with that name already exists!"},
        )
    else:
        clist[data["channel"]] = deque([], maxlen=100)
        emit("confirmcreate", {"code": "1", "channel": data["channel"]}, broadcast=True)


@socketio.on("joinchannel")
def join(data):
    username = data["username"]
    room = data["activechannel"]
    oldroom = data["oldchannel"]
    time = data["time"]
    leave_room(oldroom)
    emit(
        "msgupdate",
        {
            "user": "Server",
            "oldchannel": oldroom,
            "msg": username + ", has left the channel!",
            "time": time,
        },
        room=oldroom,
    )
    join_room(room)
    active = list(clist[room])
    emit("joined", {"msgs": active}, room=request.sid)
    emit(
        "msgupdate",
        {
            "user": "Server",
            "activechannel": room,
            "msg": username + ", has joined the channel!",
            "time": time,
        },
        room=room,
    )


if __name__ == "__main__":
    socketio.run(app)

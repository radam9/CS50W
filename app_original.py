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
    users = list(ulist)
    rooms = list(clist)
    socketio.emit("connect", {"users": users, "rooms": rooms})
    return render_template("index.html")


@socketio.on("onconnect")
def onconnect(data):
    user = data["username"]
    room = data["activechannel"]
    ulist[user] = request.sid
    join_room(room)
    print(f"\n\n{user} has connected and joined {room}\n\n")
    print(ulist)
    users = list(ulist)
    rooms = list(clist)
    if clist[data["activechannel"]]:
        active = list(clist[data["activechannel"]])
        emit(
            "connected",
            {"code": "1", "users": users, "rooms": rooms, "msgs": active},
            broadcast=False,
        )
    else:
        emit(
            "connected", {"code": "0", "users": users, "rooms": rooms}, broadcast=False
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
            "username": user,
            "msg": user + "had disconneted from the server!",
            "time": time,
        },
    )


@socketio.on("sendmsg")
def handle_msg(data):
    clist[data["activechannel"]].append(
        {"user": data["username"], "msg": data["msg"], "time": data["time"]}
    )
    print(clist[data["activechannel"]])
    emit(
        "msgupdate",
        {
            "user": data["username"],
            "activechannel": data["activechannel"],
            "msg": data["msg"],
            "time": data["time"],
        },
        broadcast=True,
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
    leave_room(oldroom)
    emit(
        "msgupdate",
        {
            "user": username,
            "oldchannel": oldroom,
            "msg": username + ", has left the channel!",
            "time": data["time"],
        },
        room=oldroom,
    )
    join_room(room)
    active = list(clist[room])
    active.append(
        {
            "user": username,
            "activechannel": room,
            "msg": username + ", has joined the channel!",
            "time": data["time"],
        }
    )
    emit("joined", {"msgs": active}, room=room)


@socketio.on("leave")
def leave(room_leave):
    username = room_leave["username"]
    room = room_leave["room"]
    leave_room(room)
    send(username + " has left the room.", room=room)


if __name__ == "__main__":
    socketio.run(app)

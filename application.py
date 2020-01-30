from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, send, join_room, leave_room
from collections import deque

app = Flask(__name__)
app.config["SECRET_KEY"] = "The Strongest Secret Key Ever!"
app.config["SESSION_TYPE"] = "filesystem"
socketio = SocketIO(app)


clist = {"General": deque([], maxlen=100), "Internet": [], "Sports": []}
ulist = {}


@app.route("/")
def main():
    users = list(ulist)
    rooms = list(clist)
    socketio.emit("connect", {"users": users, "rooms": rooms})
    return render_template("index.html")


@socketio.on("onconnect")
def onconnect(data):
    ulist[data["username"]] = request.sid
    join_room(data["activechannel"])
    user = data["username"]
    c = data["activechannel"]
    print(f"\n\n{user} has connected and joined {c}\n\n")
    print(ulist)
    users = list(ulist)
    rooms = list(clist)
    if clist[data["activechannel"]]:
        active = list(clist[data["activechannel"]])
        emit("connected", {"code": "1", "users": users, "rooms": rooms, "msgs": active})
    emit("connected", {"code": "0", "users": users, "rooms": rooms})


@socketio.on("ondisconnect")
def ondisconnect(data):
    user = data["username"]
    ulist.pop(user)
    print(ulist)


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
    print("delay")


@socketio.on("createchannel")
def createroom(data):
    if data["channel"] in clist:
        emit(
            "confirmcreate",
            {"code": "0", "msg": "A channel with that name already exists!"},
        )
    else:
        clist[data["channel"]] = deque([], maxlen=100)
        emit("confirmcreate", {"code": "1", "channel": data["channel"]})


@socketio.on("join")
def join(room_join):
    username = room_join["username"]
    room = room_join["room"]
    join_room(room)
    emit("joined", username + " has joined the room.", room=room)


@socketio.on("leave")
def leave(room_leave):
    username = room_leave["username"]
    room = room_leave["room"]
    leave_room(room)
    send(username + " has left the room.", room=room)


if __name__ == "__main__":
    socketio.run(app, debug=True)

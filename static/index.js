// User login modal
if (
  !localStorage.getItem("username") &&
  !localStorage.getItem("activechannel")
) {
  var btnChat = document.getElementById("btnUser");
  var dn = document.getElementById("displayname");
  $("#myModal").modal({ backdrop: "static", keyboard: false });
  $("#displayname").trigger("focus");

  dn.onkeyup = e => {
    if (e.keyCode == 13 && dn.value.length > 0) {
      e.preventDefault();
      btnChat.click();
    } else {
      if (dn.value.length > 0) btnChat.disabled = false;
      else btnChat.disabled = true;
    }
  };
  // detect button click
  btnChat.onclick = () => {
    localStorage.setItem("username", dn.value);
    dn.value = "";
    localStorage.setItem("activechannel", "General");
    $("#myModal").modal("hide");
    chatapp();
  };
}
// main javascript script
function chatapp() {
  // setting the username as a variable
  var username = localStorage.getItem("username");
  // getting the channel create elements and send message elements and setting them as variables
  var btnCreate = document.getElementById("btncreate");
  var channelCreate = document.getElementById("channelcreate");
  var btnSend = document.getElementById("btnsend");
  var msgSend = document.getElementById("msgsend");
  // setting variable for channel tabs
  var chan = document.getElementById("chanlist");

  // disable create channel and send msg buttons
  btnCreate.disabled = true;
  btnSend.disabled = true;

  //start socket connection
  var socket = io.connect(
    location.protocol + "//" + document.domain + ":" + location.port
  );

  // upon establishing socket connection and receiving confimation from the server, run the login function to send credentials to the server.
  socket.on("connect", () => {
    login();
  });
  //server reply with channel and messages data
  socket.on("connected", data => {
    for (const e of data["rooms"]) {
      createchannel({ channel: e });
    }
    var activechannel = localStorage.getItem("activechannel");
    // set active highlight on the activechannel
    document.getElementById("list-" + activechannel).className += " active";
    //if messages exist in the activechannel
    if (data["code"] == "1") {
      for (const e of data["msgs"]) {
        createmsg(e);
      }
    }
  });

  // server reply for joining room
  socket.on("joined", data => {
    for (const e of data["msgs"]) {
      createmsg(e);
    }
  });

  // Channel Creating Section
  // enable the create button if there is content in the input field, and use the "enter" key to submit if there is content in the input field, then requesting from the server to create a new channel by pressing "Enter"
  channelCreate.onkeyup = e => {
    if (e.keyCode === 13 && channelCreate.value.length > 0) {
      e.preventDefault();
      // var channel = channelCreate.value;
      btnCreate.click();
    } else {
      if (channelCreate.value.length > 0) btnCreate.disabled = false;
      else btnCreate.disabled = true;
    }
  };

  // Requesting from the server to create a new channel by "clicking the button"
  btnCreate.onclick = () => {
    socket.emit("createchannel", {
      channel: channelCreate.value,
      username: username
    });
    channelCreate.value = "";
    btnCreate.disabled = true;
  };

  // Channel creating confirmation from the server (accepting or rejecting).
  socket.on("confirmcreate", data => {
    if (data["code"] == "0") {
      alert(data["msg"]);
    } else {
      //create html element
      createchannel(data);
    }
  });

  // Message Section

  // enable the send button if there is content in the input field, and use the "enter" key to submit if there is content in the input field, then sending the message to the server by pressing "Enter"
  msgSend.onkeyup = e => {
    if (e.keyCode == 13 && msgSend.value.length > 0) {
      e.preventDefault();
      // var message = msgSend.value;
      btnSend.click();
    } else {
      if (msgSend.value.length > 0) btnSend.disabled = false;
      else btnSend.disabled = true;
    }
  };

  // Sending the message to the server by "clicking the button"
  btnSend.onclick = () => {
    let time = new Date().toLocaleString();
    socket.emit("sendmsg", {
      msg: msgSend.value,
      username: username,
      activechannel: localStorage.getItem("activechannel"),
      time: time
    });
    msgSend.value = "";
    btnSend.disabled = true;
  };

  // receiving flask msg broadcast and displaying it in html (including when someone leaves the room)
  socket.on("msgupdate", data => {
    createmsg(data);
  });

  // Channel Joining Section

  // join channel
  chan.addEventListener("click", e => {
    var oldchannel = localStorage.getItem("activechannel");
    var newchannel = e.target.id;
    var activechannel = newchannel.slice(5);
    if (oldchannel === activechannel) {
    } else if (oldchannel != activechannel) {
      localStorage.setItem("activechannel", activechannel);
      var hash = "#";
      document.getElementById("ctitle").innerHTML = hash.concat(activechannel);
      document.getElementById("msglist").innerHTML = "";
      let time = new Date().toLocaleString();
      socket.emit("joinchannel", {
        oldchannel: oldchannel,
        activechannel: activechannel,
        username: username,
        time: time
      });
    }
  });
  // bootstrap for highlighting the clicked channel
  $("#chanlist a").on("click", function(e) {
    e.preventDefault();
    $(this).tab("show");
  });

  //Logout/disconnect
  document.querySelector("#btnlogout").onclick = () => {
    let time = new Date().toLocaleString();
    socket.emit("ondisconnect", {
      username: username,
      activechannel: localStorage.getItem("activechannel"),
      time: time
    });
    localStorage.clear();
    location.reload();
  };

  // funtion to login the user with username and channel
  function login() {
    var activechannel = localStorage.getItem("activechannel");
    //set the username in the sidebar
    document.getElementById("idusername").innerHTML = username;
    //set channel name ontop of chat
    var hash = "#";
    document.getElementById("ctitle").innerHTML = hash.concat(activechannel);
    //send the username and activechannel to the server
    let time = new Date().toLocaleString();
    socket.emit("onconnect", {
      username: username,
      activechannel: activechannel,
      time: time
    });
  }
  // function to create channel divs
  function createchannel(data) {
    const template = Handlebars.compile(
      document.getElementById("h-channels").innerHTML
    );
    const item = template(data);
    document.getElementById("chanlist").innerHTML += item;
  }
  // function to create message divs
  function createmsg(data) {
    const template = Handlebars.compile(
      document.getElementById("h-messages").innerHTML
    );
    const item = template(data);
    document.getElementById("msglist").innerHTML += item;
    const messagesWindow = document.querySelector("#msglist");
    messagesWindow.scrollTop = messagesWindow.scrollHeight;
  }
}

var username = localStorage.getItem("username");
if (username != null) {
  chatapp();
}

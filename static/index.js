loginpop();

// function for the login popup
function loginpop() {
  if (
    !localStorage.getItem("username") &&
    !localStorage.getItem("activechannel")
  ) {
    var username = prompt("Enter your desired display name: ");
    localStorage.setItem("username", username);
    localStorage.setItem("activechannel", "General");
  }
}

// const template = Handlebars.compile();

// Main eventlistener to start the
document.addEventListener("DOMContentLoaded", () => {
  // setting the username and activechannel as variables
  var username = localStorage.getItem("username");
  var activechannel = localStorage.getItem("activechannel");
  // getting the channel create elements and send message elements and setting them as variables
  var btnCreate = document.getElementById("btncreate");
  var channelCreate = document.getElementById("channelcreate");
  var btnSend = document.getElementById("btnsend");
  var msgSend = document.getElementById("msgsend");

  // disable create channel and send msg buttons
  btnCreate.disabled = true;
  btnSend.disabled = true;

  //start socket connection
  // var socket = io.connect(
  //   location.protocol + "//" + document.domain + ":" + location.port
  // );
  var socket = io.connect("http://127.0.0.1:5000");
  // upon establishing socket connection and receiving confimation from the server, run the login function to send credentials to the server.
  socket.on("connect", () => {
    login();
  });
  //server reply with channel and messages data
  socket.on("connected", data => {
    //if no messages exist in the activechannel
    if (data["code"] == "0") {
      for (const e of data["rooms"]) {
        createchannel({ channel: e });
      }
    } else if (data["code"] == "1") {
      for (const e of data["rooms"]) {
        createchannel({ channel: e });
      }
      // debugger;
      for (const e of data["msgs"]) {
        createmsg(e);
      }
    }
  });

  // Channel Creating Section
  // enable the create button if there is content in the input field, and use the "enter" key to submit if there is content in the input field, then requesting from the server to create a new channel by pressing "Enter"
  channelCreate.onkeyup = e => {
    if (e.keyCode == 13) {
      // var channel = channelCreate.value;
      if (channelCreate.value.length > 0) {
        socket.emit("createchannel", {
          channel: channelCreate.value,
          username: username
        });
        channelCreate.value = "";
        btnCreate.disabled = true;
      }
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
    if (e.keyCode == 13) {
      // var message = msgSend.value;
      if (msgSend.value.length > 0) {
        let time = new Date().toLocaleString();
        socket.emit("sendmsg", {
          msg: msgSend.value,
          username: username,
          activechannel: activechannel,
          time: time
        });
        msgSend.value = "";
        btnSend.disabled = true;
      }
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
      activechannel: activechannel,
      time: time
    });
    msgSend.value = "";
    btnSend.disabled = true;
  };

  // receiving flask msg broadcast and displaying it in html
  socket.on("msgupdate", data => {
    createmsg(data);
    console.log(data);
  });

  // // message sending event listener
  // document.querySelector("#btnsend").onclick = () => {
  //   let time = new Date().toLocaleString();
  //   socket.emit("sendmsg", {
  //     msg: document.querySelector("#msgsend").value,
  //     username: username,
  //     activechannel: activechannel,
  //     time: time
  //   });
  // };

  //Logout/disconnect
  document.querySelector("#btnlogout").onclick = () => {
    socket.emit("ondisconnect", {
      username: (username = localStorage.getItem("username"))
    });
    localStorage.clear();
    location.reload();
  };

  // funtion to login the user with username and channel
  function login() {
    //get username from localstorage
    var username = localStorage.getItem("username");
    //set the username in the sidebar
    document.querySelector("#idusername").innerHTML = username;
    //get the activechannel from localstorage
    var activechannel = localStorage.getItem("activechannel");
    //send the username and activechannel to the server
    socket.emit("onconnect", {
      username: (username = localStorage.getItem("username")),
      activechannel: activechannel
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
  }
});

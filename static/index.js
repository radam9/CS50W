// if (
//   !localStorage.getItem("username") &&
//   !localStorage.getItem("current_channel") &&
//   !localStorage.getItem("comment_stack")
// ) {
//   var username = prompt("Enter a display name ");
//   localStorage.setItem("username", username);
//   localStorage.setItem("current_channel", "general");
//   localStorage.setItem("comment_stack", JSON.stringify({ general: 110 }));
// }
if (
  !localStorage.getItem("username") &&
  !localStorage.getItem("activechannel")
) {
  var username = prompt("Enter your desired display name: ");
  localStorage.setItem("username", username);
  localStorage.setItem("activechannel", "General");
}

document.addEventListener("DOMContentLoaded", () => {
  var socket = io.connect(
    location.protocol + "//" + document.domain + ":" + location.port
  );
  var username = localStorage.getItem("username");
  document.querySelector("#username").innerHTML = username;

  socket.on("connect", () => {
    socket.emit("eventconnect", username);
  });
  socket.on("message", data => {
    console.log(`Connected as: ${data}`);
  });
});

function coloreditor(element) {
  e = element.innerText;
  if (e === "Order Received") {
    element.classList.add("received");
  } else if (e === "Preparing") {
    element.classList.add("preparing");
  } else if (e === "On Route") {
    element.classList.add("onroute");
  } else if (e === "Delivered") {
    element.classList.add("delivered");
  }
}

var cells = document.getElementsByClassName("column4");
Array.from(cells).forEach(c => {
  coloreditor(c);
});

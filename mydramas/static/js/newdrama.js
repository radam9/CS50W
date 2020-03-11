// Django documentation function to get csrftoken from cookies
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
// when "Fetch" is click, send request to get drama info and populate the form
document.getElementById("fetchdrama").addEventListener("click", () => {
  fetch("/api/fetchdrama/", {
    method: "get",
    credentials: "same-origin",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      Accept: "application/json",
      "Content-Type": "application/json",
      URL: document.getElementById("id_mdlurl").value
    }
  })
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      document.getElementById("id_title").value = data.title;
      document.getElementById("id_year").value = data.year;
      document.getElementById("id_epcount").value = data.epcount;
      document.getElementById("id_eplength").value = data.eplength;
      var n = document.getElementById("id_network");
      for (var i = 0; i < n.options.length; i++) {
        if (n.options[i].text == data.network) {
          n.selectedIndex = i;
          break;
        }
        document.getElementById("poster").src = data.image;
      }
    })
    .catch(function(ex) {
      console.log("parsing failed", ex);
    });
});

// Date Picker widget for "Watch Date" field
$(function() {
  $("#datetimepicker1").datetimepicker({
    format: "DD/MM/YYYY"
  });
});

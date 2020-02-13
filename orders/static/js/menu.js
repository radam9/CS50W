$(".additem").on("click", e => {
  var id = e.currentTarget.id.slice(5);
  console.log(id);
  $.ajax({
    type: "GET",
    url: "/modal/",
    data: { item: id },
    success: function(data) {
      $(".modalslot").append(data);
      $(".modal").modal({ backdrop: "static" });
      //delete modal html after it is closed.
      $(".modal").on("hidden.bs.modal", () => {
        $(".modalslot").empty();
      });
      //how should i submit the form from the modal?
      $("#sform").submit(() => {
        var x = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        $.ajax({
          headers: {
            "X-CSRFToken": x
          },
          type: "POST",
          url: "/modal/",
          data: $("#sform").serialize(),
          dataType: "json",
          error: function(newdata) {
            $(".modalslot").empty();
            $(".modalslot").append(newdata);
            $(".modal").modal("show");
          }
        });
      });
    }
  });
});

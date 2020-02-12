$(".additem").on("click", e => {
  var id = e.currentTarget.id;
  console.log(id);
  $.ajax({
    type: "GET",
    url: "/modal/",
    data: { item: id },
    success: function(data) {
      console.log("I received the data");
      console.log(data);
      $(".modalslot").append(data);
      $(".modal").modal({ backdrop: "static" });
      //delete modal html after it is closed.
      $(".modal").on("hidden.bs.modal", () => {
        $(".modalslot").empty();
      });
      //how should i submit the form from the modal?
      // $(".place").on("click", data =>{
      //   $.ajax({
      //     type: "POST",
      //     url: "/modal/",
      //     data: {item:id}
      //   })
      // });
    }
  });
});
